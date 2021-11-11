from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
post_data = []
# 포스트아이디(int) -> 코멘트 리스트
comment_data = {}
# {
#     0: [
#         {
#             "text": "댓글 내용",
#             "password": "1234"
#         },
#         {
#             "text": "댓글 내용",
#             "password": "1234"
#         },
#         {
#             "text": "댓글 내용",
#             "password": "1234"
#         }],
#     100: [{
#         "text": "댓글 내용",
#         "password": "1234"
#     }]
# }

# comment_data[0]  # 댓글 리스트가 반환된다

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
    comment_data[len(post_data)] = []
    post_data.append(res)
    return res


@app.get("/post/{post_id}/")
def get_post(post_id: int):
    if post_id >= len(post_data) or post_id < 0:
        return "찾을 수 없습니다."
    return post_data[post_id]


@app.put("/post/{post_id}/")
def update_post(post_id: int, title: Optional[str] = Form(None), content: Optional[str] = Form(None)):
    # form(none) = 아무것도 없는 게 기본값이다. (...) -> 필수
    if title is None and content is None:
        return "아무것도 바뀌지 않았다"
    if title is not None:
        post_data[post_id]['title'] = title
        # dictionary이기 때문에 ['']로 넣어준다. 리스트처럼 .이 아니야
    if content is not None:
        post_data[post_id]['content'] = content
    post_data[post_id]["modified_at"] = datetime.now()
    return post_data[post_id]


@app.delete("/post/{post_id}/")
def delete_post(post_id: int):
    if post_id >= len(post_data) or post_id < 0:
        return "찾을 수 없습니다."
    del post_data[post_id]
    # post_data.remove(post_id)
    return "게시글이 삭제되었습니다"


# ----

@app.get("/post/{post_id}/comment/")
def create_comment(post_id: int):
    return comment_data[post_id]


@app.post("/post/{post_id}/comment/")
def create_comment(post_id: int, text=Form(...), password=Form(...)):
    # 중괄호는 dictionary
    res = {
        "text": text,
        "password": password,
    }

    comment_list = comment_data[post_id]
    comment_list.append(res)

    # comment_data[post_id].append(res)
    return res


@app.delete("/post/{post_id}/comment/{comment_id}/")
def delete_comment(post_id: int, comment_id: int):
    # 기본이 문자다
    comment_list = comment_data[post_id]

    if len(comment_list) <= comment_id:
        return "없는 코멘트"

    del comment_list[comment_id]
    return "댓글이 삭제되었습니다"


@app.put("/post/{post_id}/comment/{comment_id}/")
def update_comment(post_id: int, comment_id: int, text: Optional[str] = Form(...), password: str = Form(...)):
    comment_list = comment_data[post_id]
    if password != comment_list[comment_id]["password"]:
        return "패스워드가 틀렸습니다"

    comment_list[comment_id]["text"] = text
    return comment_list[comment_id]

    # if text is None and password is None:
    #     return "아무것도 바뀌지 않았다"
    # if text is not None:
    #     comment_data[post_id].text = text
    # if password is not None:
    #     comment_data[post_id].password = password
    # return comment_data[post_id]
