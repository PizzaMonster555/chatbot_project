import openai
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Use environment variable for OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(user_input):
    if not user_input:
        return "I didn't get that. Can you repeat?"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "Oops! Something went wrong. Try again later."

@app.route("/", methods=["GET", "POST"])
def home():
    chatbot_reply = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        chatbot_reply = chatbot_response(user_input)

    return render_template("index.html", user_input=user_input, chatbot_response=chatbot_reply)

if __name__ == "__main__":
    app.run(debug=True)
