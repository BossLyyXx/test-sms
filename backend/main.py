from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from cutsun_api import send_sms

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/send")
async def send_api(phone: str = Form(...), amount: int = Form(...)):
    try:
        await send_sms(phone, amount)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
