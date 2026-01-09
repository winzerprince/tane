from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pathlib

app = FastAPI()

index_path = pathlib.Path("public/index.html")
acoustic_path = pathlib.Path("public/acoustic.html")
electric_path = pathlib.Path("public/electric.html")
bass_path = pathlib.Path("public/bass.html")

@app.get("/")
def server_index(response_class=HTMLResponse):
    content = index_path.read_text()
    return response_class(content=content)

@app.get("/acoustic")
def server_acoustic(response_class=HTMLResponse):
    content = acoustic_path.read_text()
    return response_class(content=content)

@app.get("/electric")
def serve_electric(response_class=HTMLResponse):
    content = electric_path.read_text()
    return response_class(content=content)

@app.get("/bass")
def serve_bass(response_class= HTMLResponse):
    content = bass_path.read_text()
    return response_class(content=content)
    
