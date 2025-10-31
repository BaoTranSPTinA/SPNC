# SPNC — Học thuật toán qua mô phỏng và trò chơi

Dự án gồm 2 phần:
- `spnc_backend/`: Backend Django + Django REST Framework (JWT login, API Thuật toán/Hướng dẫn/Trò chơi, ghi Điểm và Tiến độ)
- `web/`: Giao diện web tĩnh (HTML/CSS/JS) có thể mở trực tiếp bằng trình duyệt và gọi API backend

---

## 1) Yêu cầu môi trường
- Windows + PowerShell
- Python 3.9+ (đã kiểm tra 3.9.13)

Tuỳ chọn (nếu muốn nâng cấp UI bằng framework hiện đại): Node.js 18+ (không bắt buộc cho bản web tĩnh hiện tại).

---

## 2) Cài đặt và chạy Backend (Django)
Tại thư mục gốc dự án `SPNC`:

```powershell
# 2.1 Tạo môi trường ảo và cài gói
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install django djangorestframework djangorestframework-simplejwt

# 2.2 (Nếu cần) tạo project/app — đã có sẵn trong repo
# django-admin startproject spnc_backend
# cd spnc_backend; ..\..\.venv\Scripts\python manage.py startapp core

# 2.3 Chạy migrate
cd spnc_backend
..\.venv\Scripts\python manage.py migrate

# 2.4 Tạo tài khoản quản trị (lần đầu)
..\.venv\Scripts\python manage.py createsuperuser
# nếu trước đó có user admin không có mật khẩu, đặt lại:
# ..\.venv\Scripts\python manage.py changepassword admin

# 2.5 (Tuỳ chọn) Seed dữ liệu mẫu thuật toán/hướng dẫn/game
..\.venv\Scripts\python manage.py shell -c "from core.models import Algorithm,Tutorial,Game; \
Algorithm.objects.get_or_create(name='BFS', defaults={'description':'Duyệt theo chiều rộng','type':'graph'}); \
Algorithm.objects.get_or_create(name='DFS', defaults={'description':'Duyệt theo chiều sâu','type':'graph'}); \
Algorithm.objects.get_or_create(name='Dijkstra', defaults={'description':'Đường đi ngắn nhất','type':'graph'})"

# 2.6 Chạy server
..\.venv\Scripts\python manage.py runserver 0.0.0.0:8000
```

Backend mặc định chạy tại: `http://127.0.0.1:8000`

- Trang quản trị: `http://127.0.0.1:8000/admin/`
- Kiểm tra nhanh: `GET http://127.0.0.1:8000/api/health/` trả `{ "status": "ok" }`

---

## 3) API chính (JWT)
- Lấy token: `POST /api/auth/token/` body JSON: `{ "username": "<user>", "password": "<pass>" }`
- Làm mới token: `POST /api/auth/refresh/` body `{ "refresh": "<refresh_token>" }`

Các API mở (không cần token):
- `GET /api/algorithms/`
- `GET /api/tutorials/?algo=<id>`
- `GET /api/games/`

Các API yêu cầu Bearer token (đăng nhập):
- `GET/POST /api/progress/`  (lưu tiến độ học thuật toán)
- `GET/POST /api/attempts/`  (ghi lần chơi và điểm số)

Ví dụ gọi nhanh bằng PowerShell:
```powershell
# Lấy access token
$resp = Invoke-RestMethod -Method POST -Uri http://127.0.0.1:8000/api/auth/token/ -ContentType application/json -Body '{"username":"admin","password":"<PASSWORD>"}'
$TOKEN = $resp.access

# Lấy danh sách thuật toán
Invoke-RestMethod http://127.0.0.1:8000/api/algorithms/

# Ghi một lần chơi (cần token)
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:8000/api/attempts/ -Headers @{Authorization = "Bearer $TOKEN"} -ContentType application/json -Body '{"game_id":1, "score": 10, "time_spent": 30}'
```

---

## 4) Chạy giao diện `web/`
Phiên bản hiện tại là web tĩnh, không cần build. Chỉ cần mở file sau trên trình duyệt:
- `web/index.html`

Trang chính liên kết đến:
- `web/pages/algorithms.html` — danh sách thuật toán
- `web/pages/tutorials.html?algo=<id>` — hướng dẫn theo thuật toán
- `web/pages/games.html` — danh sách game (nút "Chơi thử" sẽ gọi API ghi điểm nếu đã đăng nhập)
- `web/pages/login.html` — đăng nhập, lưu token vào `localStorage`

Web tự động gọi API backend tại `http://127.0.0.1:8000/api`. Nếu backend chạy ở domain khác, cấu hình nhanh trong Console:
```js
localStorage.setItem('spnc_api', 'https://YOUR_BACKEND_DOMAIN/api')
```

---

## 5) Tuỳ biến và mở rộng
- Bổ sung model/serializer/view: sửa trong `spnc_backend/core/`
- Thêm endpoint mới: khai báo trong `spnc_backend/core/urls.py` và `views.py`
- Kết nối UI: sửa các trang trong `web/` và sử dụng helper `web/js/api.js`

---

## 6) Cấu trúc thư mục chính
```
SPNC/
  ├─ spnc_backend/
  │   ├─ core/                # models, serializers, views, urls
  │   ├─ spnc_backend/        # settings, root urls
  │   └─ manage.py
  └─ web/
      ├─ index.html
      ├─ styles.css
      ├─ js/
      │   ├─ api.js           # tiện ích gọi API + lưu token
      │   └─ data.js          # dữ liệu mẫu (fallback offline)
      └─ pages/
          ├─ login.html
          ├─ algorithms.html
          ├─ tutorials.html
          └─ games.html
```

---

## 7) Lỗi thường gặp
- "Unable to connect" khi gọi API: đảm bảo server Django đang chạy (`runserver`) và đúng cổng.
- 401 Unauthorized khi POST `/api/attempts/` hoặc `/api/progress/`: cần đăng nhập, kiểm tra header `Authorization: Bearer <access_token>`.
- Không thấy dữ liệu: chạy seed mẫu ở bước 2.5 hoặc tạo mới trong trang Admin.

---

Chúc bạn sử dụng vui vẻ! Nếu muốn mình triển khai lên hosting (Render/Railway) hoặc nâng cấp UI/UX, hãy nói nhé.
