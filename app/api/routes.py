from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from app.models import VideoRequest
from app.services import AudioDownloader
import os
from starlette.background import BackgroundTask

router = APIRouter()

def remove_file(path: str) -> None:
    try:
        os.unlink(path)
    except Exception as e:
        print(f"Error while deleting file {path}: {e}")

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/download_audio")
async def download_audio(video_request: VideoRequest, downloader: AudioDownloader = Depends(AudioDownloader)):
    try:
        filename = await downloader.download(str(video_request.url))

        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(
            path=filename,
            filename=os.path.basename(filename),
            media_type="audio/mpeg",
            background=BackgroundTask(remove_file, filename)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
