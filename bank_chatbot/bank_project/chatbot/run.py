from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Flask setup
app = Flask(__name__)

# ChatterBot setup
bot = ChatBot(
    "BankingBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {"import_path": "chatterbot.logic.BestMatch"}
    ],
)

# Train the bot if no database exists
if not os.path.exists("db.sqlite3"):
    trainer = ListTrainer(bot)
    for file in os.listdir("data"):
        with open(f"data/{file}", "r") as f:
            conversation = f.readlines()
            trainer.train(conversation)

@app.route("/api/get_response", methods=["GET"])
def get_bot_response():
    user_message = request.args.get("message")
    if user_message:
        response = str(bot.get_response(user_message))
        return jsonify({"response": response})
    return jsonify({"response": "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
