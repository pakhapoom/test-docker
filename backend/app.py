import logging
from fastapi import FastAPI, Request


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/greet")
async def greet(request: Request):
    logger.info("Received POST request at /greet")
    data = await request.json()
    username = data.get("username", "Guest")
    logger.info(f"Extracted username: {username}")
    message = f"Hello, {username}!"
    logger.info(f"Sending response: {message}")
    return {"message": message}

# uvicorn backend.app:app --reload --port 5001