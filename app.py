from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    if not user_input:  # Check if user_input is None or empty
        return "I didn't understand that. Can you rephrase?"

    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")


@app.route("/", methods=["GET", "POST"])
def home():
    chatbot_reply = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")  # Get form input safely
        chatbot_reply = chatbot_response(user_input)

    return render_template("index.html", user_input=user_input, chatbot_response=chatbot_reply)

# **NEW: Add an API Route for Chatbot Responses**
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get JSON input
    user_input = data.get("message", "")  # Extract the "message" key
    response = chatbot_response(user_input)  # Process response
    return jsonify({"response": response})  # Return as JSON

if __name__ == "__main__":
    app.run(debug=True)
