from backend.auth_utils import verify_id_token
from fastapi import Request, HTTPException

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fd_board_mock_data import get_mock_fd_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fd-summary")
def read_fd_summary():
    return get_mock_fd_data()

    @app.get("/verify-token")
async def verify_token(request: Request):
    id_token = request.headers.get("Authorization")
    if not id_token:
        raise HTTPException(status_code=401, detail="Missing token")

    user_info = verify_id_token(id_token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return {"status": "verified", "email": user_info.get("email")}
