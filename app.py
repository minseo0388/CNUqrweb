from flask import Flask, jsonify, g, Response
import qr
import uuid
import os

app = Flask(__name__)

@app.route('/')
@app.route('/cnuqr')
def CNUqrhome():
    return '/cnuqr/학번 형식으로 접속해주세요. System Operational.'
    
@app.route('/cnuqr/<ID>', methods=['GET'])
def CNUqr(ID):
    qr_path = 'temp/' + str(uuid.uuid4()) + '.png'

    qr.qrmaker(ID).save(qr_path)
    
    qr_file = open(qr_path, "rb")
    qr_data = qr_file.read()
    qr_file.close()

    os.remove(qr_path)

    return Response(qr_data, mimetype="image/png")
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
