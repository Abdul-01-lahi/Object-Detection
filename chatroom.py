from flask import Flask, render_template, request, redirect
from datetime import datetime
from models.message import Message
import os



app = Flask(__name__)

messages = []

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        user_name = request.form["user-name"]
        user_message = request.form["user-message"]
        messages.insert(
            0,
            Message(
                sender=user_name,
                message=user_message, 
                time=datetime.utcnow().time().strftime("%H:%M")
            ),
        )
        return redirect("/")

    return render_template("index.html", messages = messages)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False, threaded=True)
    