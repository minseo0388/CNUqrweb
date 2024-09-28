# 여기에 코드를 입력하세요.

# 충남대학교 도서관 어플리케이션과 충남대학교 공식 앱에 뜨는
# 본인 확인용 QR코드 생성 코드입니다.

# 이미지가 다운로드 되면 성공입니다.

# 제작자 : 화학과 24 최민서

# 필요한 라이브러리를 import합니다.
import base64
import time, datetime
import qrcode

# 교번 또는 학번을 입력받습니다.

# 코드 형식 조합
def qrmaker(studentID):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    newMonth = month.rjust(2,'0')
    newDay = day.rjust(2,'0')
    newHour = hour.rjust(2,'0')
    newMinute = minute.rjust(2,'0')
    newSecond = second.rjust(2,'0')
    timeStamp = str(year + newMonth + newDay + newHour + newMinute + newSecond)
    rawCode = str(studentID+"^"+timeStamp)
    rawCode = str(studentID+"^"+timeStamp)
    encodedCode = rawCode.encode('UTF-8')
    resultCode = base64.b64encode(encodedCode)
    resultCodeString = resultCode.decode('ascii')
    image = qrcode.make(resultCodeString)
    return image