# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from checker import Gm

app = FastAPI(title="Gmail Checker API")

class EmailRequest(BaseModel):
    email: str

@app.post("/check")
def check_email(req: EmailRequest):
    result = Gm(req.email).check()
    if result is None:
        raise HTTPException(status_code=400, detail="Failed to get response")
    return result