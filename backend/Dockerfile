FROM python:3.11-slim AS build_base

WORKDIR /app
COPY ./app.py .

RUN pip install uv
RUN uv init
RUN uv add fastapi==0.116.1 httpx==0.28.1 jinja2==3.1.6 python-multipart==0.0.20 uvicorn==0.35.0
# RUN source .venv/bin/activate

EXPOSE 5001

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]
