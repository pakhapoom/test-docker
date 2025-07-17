from fastapi import FastAPI, Request


app = FastAPI()

@app.post("/greet")
async def greet(request: Request):
    data = await request.json()
    username = data.get("username", "Guest")
    return {"message": f"Hello, {username}!"}

# uvicorn backend.app:app --reload --port 5001