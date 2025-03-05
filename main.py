from typing import Union

from fastapi import FastAPI
from models.Bases import Item
from models.Bases import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(id: int, q: Union[str, int] = None):
    return {"item_id": id}

@app.get("/blogs/{id}")
def add(id:int,name:str):
    return{"id":id,"name":name}
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.put("/users")
def userfunc(mtumiaji:User):
    return{"name":mtumiaji.name,"age":mtumiaji.age}