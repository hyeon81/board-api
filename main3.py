from typing import Optional

from fastapi import FastAPI, Body, UploadFile, File, Form
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
post_data = []

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/post/")
def get_post_all():
    return post_data


@app.post("/post/")
def create_post(title=Form(...), content=Form(...)):
    res = {
        "title": title,
        "content": content,
        "created_at": datetime.now(),
        "modified_at": datetime.now()
    }
    post_data.append(res)
    return res


@app.get("/post/{post_id}/")
def get_post(post_id: int):
    return post_data[post_id]


@app.patch("/post/{post_id}/")
def update_post(post_id, title: Optional[str] = Form(...), content: Optional[str] = Form(...)):
    if title is None and content is None:
        return "아무것도 바뀌지 않았다"

    # if title is not None and content is None:
    #     post_data[post_id].title = title
    #     return post_data[post_id]
    #
    # if title is None and content is not None:
    #     post_data[post_id].content = content
    #     return post_data[post_id]
    #
    # if title is not None and content is not None:
    #     post_data[post_id].title = title
    #     post_data[post_id].content = content
    #     return post_data[post_id]
    if title is not None:
        post_data[post_id].title = title
    if content is not None:
        post_data[post_id].content = content
    return post_data[post_id]


@app.delete("/post/{post_id}/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


@app.post("/post/{post_id}/comment/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


@app.get("/post/{post_id}/comment/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


@app.get("/post/{post_id}/comment/{comment_id}/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


@app.put("/post/{post_id}/comment/{comment_id}/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


@app.delete("/post/{post_id}/comment/{comment_id}/")
def delete_post(post_id):
    post_data.remove(post_id)
    return "게시글이 삭제되었습니다"
