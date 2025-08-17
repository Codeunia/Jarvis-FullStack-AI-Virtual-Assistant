import threading
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .core import taskExecution, get_log_stream
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

background_thread = None

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    global background_thread
    if background_thread is None or not background_thread.is_alive():
        background_thread = threading.Thread(target=taskExecution, daemon=True)
        background_thread.start()
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/stream")
async def stream_logs():
    async def event_generator():
        async for line in get_log_stream():
            yield f"data: {line}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

