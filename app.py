from flask import Flask, request, render_template
import os
from google import genai
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Initialize the client properly
client = genai.Client()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    user_prompt = ""

    # Check if the form was submitted using POST
    if request.method == "POST":
        # Get the input value from request.form (sent via POST)
        user_prompt = request.form.get("userInput_ai")
        
        if user_prompt:
            # Generate content using the Gemini client
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt,
            )
            response_text = response.text

    return render_template("index.html", response=response_text, prompt=user_prompt)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)