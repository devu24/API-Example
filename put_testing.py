from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35},
    4: {"name": "David", "age": 28},
    5: {"name": "Eve", "age": 22}
}

class User(BaseModel):
    name: str
    age: int

@app.put("/user/{user_id}")
def user_update(user_id: int, user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/from_db/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")