from fastapi import FastAPI
from app.routers import auth, sessions, patients, recommendations

app = FastAPI(title="SmritiCare API", version="0.1.0")
app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(patients.router)
app.include_router(recommendations.router)

@app.get("/health")
async def health():
    return {"status": "ok"}