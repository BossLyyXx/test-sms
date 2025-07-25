from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
# สมมติว่าฟังก์ชัน send_sms_to_number อยู่ในไฟล์นี้หรือ import มา
from main import send_sms_to_number # หรือชื่อไฟล์อื่นที่มีฟังก์ชันนี้

app = FastAPI()

# ตั้งค่าให้สามารถใช้ไฟล์ HTML จากโฟลเดอร์ templates
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    แสดงหน้าเว็บ index.html เมื่อผู้ใช้เข้ามาที่ URL หลัก
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send")
async def handle_send_sms(phone: str = Form(...), amount: int = Form(...)):
    """
    รับข้อมูลจากฟอร์มและเรียกใช้ฟังก์ชันส่ง SMS
    """
    print(f"กำลังส่ง SMS ไปยัง {phone} จำนวน {amount} ครั้ง")
    # เรียกใช้ฟังก์ชันส่ง SMS ของคุณ
    # หมายเหตุ: คุณอาจจะต้องปรับเปลี่ยนการเรียกใช้ฟังก์ชัน send_sms_to_number
    # ให้เหมาะสมกับโปรเจคของคุณ (เช่น การรันใน background task)
    send_sms_to_number(phone, amount)

    # ส่งกลับไปยังหน้าแรกพร้อมข้อความยืนยัน (ตัวเลือก)
    return RedirectResponse(url="/?status=success", status_code=303)

# ส่วนนี้สำหรับการรันทดสอบบนเครื่องของคุณ (Local)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
