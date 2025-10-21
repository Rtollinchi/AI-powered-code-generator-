import os
import gradio as gr
import openai
import pyperclip
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

def generate_code(user_query, programming_language):
    """Generate code based on what the user asks for"""

    #check if user actually typed something
    if not user_query.strip():
        return "⚠️ Please enter what you want to create!"

    try:
      # Step 1: Create a simple prompt
        prompt = f"Write {programming_language} code for: {user_query}"

        # Step 2: Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Step 3: Get the response
        code = response.choices[0].message.content
        return code

    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

def explain_code(code_to_explain, language):
    """Explain what the code does in simple terms"""

    print("🔍 EXPLAIN function was called!")  # So you can see when it runs

    print(f"📦 VALUE received in code_to_explain:")
    print(f"   Type: {type(code_to_explain)}")
    print(f"   Length: {len(code_to_explain)} characters")
    print(f"   First 50 chars: {code_to_explain[:50]}...")
    print(f"📦 VALUE received in language: '{language}'")

    # Check if there's actually code to explain
    if not code_to_explain.strip():
        return "⚠️ Generate some code first, then I can explain it!"

    try:
        # Create a prompt asking GPT to explain
        prompt = f"""
Explain this {language} code in simple terms that a beginner can understand:

{code_to_explain}

Break it down step by step.
"""

        print(f"📤 Asking GPT to explain...")

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a patient teacher who explains code clearly."},
                {"role": "user", "content": prompt}
            ]
        )

        explanation = response.choices[0].message.content
        print("✅ Got explanation!")
        return explanation

    except Exception as e:
        return f"❌ Couldn't explain: {str(e)}"

def copy_to_clipboard(code):
    """Copy code to clipboard"""
    try:
        pyperclip.copy(code)
        return "✅ Code copied to clipboard!"
    except:
        return "❌ Couldn't copy to clipboard"

def save_to_file(code, language, filename):
    """Save the generated code to a file with custom filename"""

    print("💾 SAVE function was called!")
    print(f"📝 Filename requested: '{filename}'")
    print(f"💻 Language: '{language}'")

    # Check if there's code to save
    if not code.strip():
        return "⚠️ No code to save! Generate some code first."

    # Check if filename is provided
    if not filename.strip():
        filename = "generated_code"  # Default if empty

    try:
        # File extension mapping
        extensions = {
            "python": "py",
            "javascript": "js",
            "java": "java"
        }

        # Get the right extension
        ext = extensions.get(language, "txt")

        # Build full filename
        full_filename = f"{filename}.{ext}"

        print(f"📁 Full filename: '{full_filename}'")

        # Write to file
        with open(full_filename, "w") as f:
            f.write(code)

        print("✅ File saved successfully!")
        return f"✅ Code saved as '{full_filename}' in your current folder!"

    except Exception as e:
        print(f"❌ Error saving: {e}")
        return f"❌ Couldn't save file: {str(e)}"

# Style
custom_css = """
.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
"""

# Simple UI
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# 🚀 Simple Code Generator")

    # Inputs
    query = gr.Textbox(label="What code do you want?", lines=3)
    language = gr.Dropdown(["python", "javascript", "java"], value="python")
    filename_input = gr.Textbox(
        label="📁 Filename (optional)",
        placeholder="my_code",
        value="generated_code"
    )

    # Buttons
    generate_btn = gr.Button("Generate Code")
    copy_btn = gr.Button("📋 Copy Code")  # NEW!
    explain_btn = gr.Button("💡 Explain Code")  # ← NEW!
    save_btn = gr.Button("💾 Save Code")  # ← NEW!

    # Outputs
    output = gr.Code(label="Your Code")
    explanation_output = gr.Textbox(label="📖 Explanation", lines=8)  # ← NEW!
    status = gr.Textbox(label="Status", interactive=False)  # NEW!

    # Connect buttons
    generate_btn.click(
        fn=generate_code,
        inputs=[query, language],
        outputs=output
    )

    copy_btn.click(  # NEW!
        fn=copy_to_clipboard,
        inputs=[output],
        outputs=status
    )

    explain_btn.click(
        fn=explain_code,
        inputs=[output, language],
        outputs=explanation_output
    )

    save_btn.click(
    fn=save_to_file,
    inputs=[output, language, filename_input],  # ← Added filename_input
    outputs=status
)


# Launch the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False
    )
