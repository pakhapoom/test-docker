from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import os


app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")

BACKEND_URL = "http://localhost:5001/greet"

HTML_FORM = """
<!doctype html>
<title>Greet User</title>
<style>
    body { display: flex; justify-content: center; align-items: center; height: 100vh; }
    .center-container { text-align: center; }
</style>
<div class="center-container">
    <h2>Enter your name:</h2>
    <form method="post">
        <input type="text" name="username" required>
        <input type="submit" value="Log in">
    </form>
    {% if result %}
        <h3>{{ result }}</h3>
    {% endif %}
</div>
"""

os.makedirs("frontend/templates", exist_ok=True)
with open("frontend/templates/form.html", "w") as f:
    f.write(HTML_FORM)

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, username: str = Form(...)):
    result = None
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(BACKEND_URL, json={"username": username}, timeout=5)
            if resp.status_code == 200:
                result = resp.json().get("message", "No message from backend.")
            else:
                result = f"Backend error: {resp.status_code}"
    except Exception as e:
        result = f"Error contacting backend: {e}"
    return templates.TemplateResponse("form.html", {"request": request, "result": result})

# uvicorn frontend.app:app --reload --port 5000