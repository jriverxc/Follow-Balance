from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
import csv
from io import StringIO

from .services.unfollow import InvalidInstagramDataError, calculate_non_followers

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def _render_home(request: Request, result: dict | None = None, error: str | None = None) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result,
            "error": error,
        },
    )


@router.get("/favicon.ico", include_in_schema=False)
async def favicon() -> RedirectResponse:
    return RedirectResponse(url="/static/favicon-v4.png")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return _render_home(request)


@router.post("/", response_class=HTMLResponse)
async def analyze_files(
    request: Request,
    followers_file: UploadFile = File(...),
    following_file: UploadFile = File(...),
) -> HTMLResponse:
    if not followers_file.filename or not following_file.filename:
        return _render_home(request, error="Debes subir ambos archivos JSON.")

    if not followers_file.filename.lower().endswith(".json"):
        return _render_home(request, error="El archivo de seguidores debe ser .json.")

    if not following_file.filename.lower().endswith(".json"):
        return _render_home(request, error="El archivo de seguidos debe ser .json.")

    followers_bytes = await followers_file.read()
    following_bytes = await following_file.read()

    try:
        result = calculate_non_followers(followers_bytes, following_bytes)
    except InvalidInstagramDataError as exc:
        return _render_home(request, error=str(exc))

    return _render_home(request, result=result)


@router.post("/download-csv")
async def download_csv(non_followers: list[str] = Form(default=[])) -> Response:
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Usuario"])

    for username in non_followers:
        writer.writerow([username])

    content = csv_buffer.getvalue()
    headers = {"Content-Disposition": 'attachment; filename="non_followers.csv"'}
    return Response(content=content, media_type="text/csv; charset=utf-8", headers=headers)
