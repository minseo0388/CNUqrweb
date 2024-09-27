from flask import Flask, jsonify
from qr import image
import studentinfo

app = Flask(__name__)

@app.route('/')
@app.route('/cnuqr')
def cnuqrhome():
    return '/cnuqr/학번 형식으로 접속해주세요. System Operational.'
    
@app.route('/cnuqr/<ID>', methods=['GET'])
def handleCNUqr(ID):
    studentinfo.setStudentID(ID)
    return image.load("result.png")
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
 
# 설정시 다시 작동.