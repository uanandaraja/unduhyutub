from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title="settings.PROJECT_NAME", version=settings.PROJECT_VERSION)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
