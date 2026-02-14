import asyncio
from pathlib import Path
import sys

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse

APP_ROOT = Path(__file__).resolve().parent
UI_FILE = APP_ROOT / "web" / "index.html"
SRC_DIR = APP_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

app = FastAPI(
    title="AI Trend Bot Web App",
    description="Web wrapper for the Mastodon trend bot pipeline.",
    version="1.0.0",
)


@app.get("/", response_class=FileResponse)
async def index() -> FileResponse:
    if not UI_FILE.exists():
        raise HTTPException(status_code=404, detail="UI file not found.")
    return FileResponse(UI_FILE)


@app.post("/run-bot")
async def run_bot(
    dry_run: bool = Query(
        False,
        description="If true, generate and return the post without publishing to Mastodon.",
    )
) -> dict:
    try:
        from ai_trend_bot.pipeline import run_pipeline

        result = await asyncio.to_thread(run_pipeline, dry_run=dry_run)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pipeline failed: {exc}") from exc


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
