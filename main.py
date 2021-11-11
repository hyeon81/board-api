from fastapi import FastAPI, Body, UploadFile, File

app = FastAPI()
# 소괄호를 열고 닫아야 객체가 형성됨

user = ["user1", "성빈", "대학", "갈까"]
day = 0


# 파일을 저장하면 업로드 하는 ?
@app.post("/upload/")
def upload(file: UploadFile = File(...)):
    b = file.file.read()
    # 파일 쓸 준비 -> "쓸 파일" 객체를 f에 저장
    # f는 파일을 쓰는 역할을 할 아이
    if len(b) > 100000:
        return "너무 큰 파일입니다!"
    f = open("./" + file.filename, "wb")
    # "받을 파일" 읽어서 그 내용을 b에 저장
    # wb.  byte로 쓰겠다.
    # "쓸 파일" f에 내용 b를 쓰기
    # b 실제 파일을 읽을 거다. byte의 인수들을 b에다 저장할 것이다?
    # f는 b를 쓴다.
    f.write(b)
    # "쓸 파일" f에 쓸 것 다 썼으니 저장. close = 저장
    f.close()
    # len(b) = 파일의 길이를 반환.
    return file.filename, len(b)
