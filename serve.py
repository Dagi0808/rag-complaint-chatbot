from flask import Flask, send_file

app = Flask(__name__)

@app.route("/data")
def data():
    return send_file(
        "/home/dag-dagne/rag-complaint-chatbot/data/raw/complaints.csv"
    )

print("Server running on port 5000...")
app.run(host="0.0.0.0", port=5000)