from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

AWS_REGION = os.getenv("AWS_REGION")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")
print("AWS Region:", AWS_REGION)
print("DynamoDB Table:", DYNAMODB_TABLE)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    if not name or not email or not message:
        return "Error: All fields are required!", 400

    return f"""
        <h1>Thank you, {name}!</h1>
        <p>Your email: {email}</p>
        <p>Your message: {message}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)



