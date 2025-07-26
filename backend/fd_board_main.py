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