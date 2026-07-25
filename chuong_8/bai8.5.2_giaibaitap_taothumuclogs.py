import os
from datetime import datetime
import time

now = datetime.now()
thu_muc = os.path.join("logs", now.strftime("%Y-%m-%d"))

# tạo thư mục
os.makedirs(thu_muc, exist_ok=True)

duong_dan = os.path.join(thu_muc, "event.log")

print(duong_dan)

with open(duong_dan, "a", encoding="utf-8") as f:
    for msg in ["App khởi động", "User đăng nhập", "App thoát"]:
        ts = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        f.write(f"[{ts}] {msg}\n")
print(f"Đã ghi log vào {duong_dan}")


