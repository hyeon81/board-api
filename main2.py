from fastapi import FastAPI, Body, UploadFile, File, Form

app = FastAPI()
user_data = []


@app.get("/user")
def user():
    return user_data


@app.post("/user")
def f(name=Form(...), age=Form(...), img: UploadFile = File(...)):
    for i in user_data:
        if i['name'] == name:
            return "동명이인이 존재합니다"
    user_data.append({
        "name": name,
        "age": age,
        "img": img.filename
    })
    return "유저가 생성되었습니다"

# @app.patch("/user/{user_name}")


@app.delete("/user/{user_name}")
def g(user_name):
    for i in user_data:
        if i['name'] == user_name:
            user_data.remove(i)
            return "제거 완료!"

@app.get("/user/{user_name}")
def g1(user_name):
    for i in user_data:
        if i['name'] == user_name:
            return i
    return "없는 유저"
