
from flask import Flask, Response, abort
import qr
import uuid
import os

app = Flask(__name__)

TEMP_DIR = "temp"

@app.route("/")
@app.route("/cnuqr")
def cnuqr_home():
    return "/cnuqr/학번 형식으로 접속해주세요. System Operational."

@app.route("/cnuqr/<ID>", methods=["GET"])
def cnuqr(ID):
    if not ID or not ID.isdigit():
        abort(400, description="Invalid student ID format.")

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    qr_path = os.path.join(TEMP_DIR, f"{uuid.uuid4()}.png")
    try:
        qr.qrmaker(ID).save(qr_path)
        with open(qr_path, "rb") as qr_file:
            qr_data = qr_file.read()
    finally:
        if os.path.exists(qr_path):
            os.remove(qr_path)

    return Response(qr_data, mimetype="image/png")

if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
