
"""
충남대학교 도서관 및 공식 앱 본인 확인용 QR코드 생성기
제작자: 화학과 24 최민서
"""

import base64
import datetime
import qrcode

def qrmaker(studentID: str):
    """
    Generate a QR code image for the given student ID.
    The QR code encodes the student ID and a timestamp, base64-encoded.
    """
    now = datetime.datetime.now()
    timeStamp = now.strftime("%Y%m%d%H%M%S")
    rawCode = f"{studentID}^{timeStamp}"
    resultCodeString = base64.b64encode(rawCode.encode("utf-8")).decode("ascii")
    image = qrcode.make(resultCodeString)
    return image