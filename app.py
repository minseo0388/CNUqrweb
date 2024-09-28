from flask import Flask, jsonify, g
import qr
import qrcode

app = Flask(__name__)

@app.route('/')
@app.route('/cnuqr')
def CNUqrhome():
    return '/cnuqr/학번 형식으로 접속해주세요. System Operational.'
    
@app.route('/cnuqr/<ID>', methods=['GET'])
def CNUqr(ID):
    return qr.qrmaker(ID).load("result.png")

# @app.route('/cnuqr/getid', methods=['GET'])
# def getID():
#    if hasattr(g, 'studentID'):
#        return f"Stored student ID is: {g.studentID}"
#    else:
#        return "No student ID stored."
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
