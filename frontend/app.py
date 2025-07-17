import httpx
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")

BACKEND_URL = "http://localhost:5001/greet"

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