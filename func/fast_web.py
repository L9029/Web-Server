from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [9, 0, 2, 9]

@app.get("/home", response_class=HTMLResponse)
def get_list():
    return """
<h1>Hola Mundo</h1>
<p>Hellou World</p>"""