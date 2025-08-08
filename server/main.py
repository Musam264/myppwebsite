from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# 프로젝트 내 static 폴더를 /static 경로로 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates 폴더에 index.html 위치
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # 템플릿 렌더링하며 request 전달
    return templates.TemplateResponse("index.html", {"request": request})
