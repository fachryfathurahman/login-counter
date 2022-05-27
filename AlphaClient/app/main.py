from typing import Union
from fastapi import FastAPI
import subprocess
import socket   

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/info")
def read_info():
    result = subprocess.run(['last'], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    result = result.split("\n")
    result = [i for i in result if i]
    result.pop()
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    return {"count": len(result), "hostname": hostname, "IPAddr": IPAddr}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
