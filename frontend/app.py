import os
import httpx
import logging
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
base_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=f"{base_dir}/templates")

BACKEND_URL = "http://backend:5001/greet"

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    logger.info("Received GET request for form")
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, username: str = Form(...)):
    logger.info(f"Received POST request with username: {username}")
    result = None
    try:
        async with httpx.AsyncClient() as client:
            logger.info(f"Calling backend at {BACKEND_URL} with username: {username}")
            resp = await client.post(BACKEND_URL, json={"username": username}, timeout=5)
            logger.info(f"Backend responded with status {resp.status_code}")
            if resp.status_code == 200:
                result = resp.json().get("message", "No message from backend.")
                logger.info(f"Backend message: {result}")
            else:
                result = f"Backend error: {resp.status_code}"
                logger.error(result)
    except Exception as e:
        result = f"Error contacting backend: {e}"
        logger.error(result)
    return templates.TemplateResponse("form.html", {"request": request, "result": result})
