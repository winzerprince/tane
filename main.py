from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pathlib

app = FastAPI()
index_path = pathlib.Path("public/index")

@app.get("/")
def server_index(response_class=HTMLResponse):
    content = index_path.read_text()
    return HTMLResponse(content=content)
    
