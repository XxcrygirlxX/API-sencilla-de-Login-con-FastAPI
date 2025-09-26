from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class login(BaseModel):
    username: str
    pwd: str

user_database = {
    "username":"xcrygirlx",
    "pwd":"hotdog1234"
}

@app.post("/login")
def login(user: login):
    if user.username == user_database["username"]:
        if user.pwd == user_database["pwd"]:
            return {"message": "login successful 👌"}
        else:
            return {"message": "incorrect password, try again :("}
    else:
        return {"message": "username not found"}
