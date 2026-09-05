from datetime import datetime
from pydantic import BaseModel


class GameResult(BaseModel):
    patientId: str
    gameId: str
    sessionId: str

    score: float
    accuracy: float
    reactionTime: float
    mistakes: int
    attempts: int

    difficulty: int
    duration: int
    timestamp: datetime
