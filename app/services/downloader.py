import yt_dlp
import os
from app.core.config import settings
from app.core.exceptions import DownloadError

class AudioDownloader:
    @staticmethod
    async def download(url: str) -> str:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(settings.DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                audio_filename = os.path.splitext(filename)[0] + '.mp3'
            return audio_filename
        except Exception as e:
            raise DownloadError(f"Failed to download audio: {str(e)}")
