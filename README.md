
# Spotify API Clone 🎵

Đây là một dự án xây dựng RESTful API mô phỏng lại một phần chức năng của Spotify, bao gồm quản lý bài hát, nghệ sĩ, playlist, album, yêu thích,... Dự án sử dụng Django REST Framework, PostgreSQL, và tích hợp upload file lên AWS S3.

## 🚀 Các chức năng chính

- Đăng ký / Đăng nhập người dùng
- Quản lý bài hát (Song)
- Quản lý nghệ sĩ (Artist)
- Quản lý album và thêm bài hát vào album
- Tạo playlist và thêm bài hát vào playlist
- Yêu thích bài hát
- Upload ảnh / nhạc lên AWS S3
- Xác thực bằng JWT

---

## 🧰 Công nghệ sử dụng

| Công nghệ | Mô tả |
|----------|-------|
| Python 3.10 | Ngôn ngữ lập trình chính |
| Django & Django REST Framework | Xây dựng API |
| PostgreSQL | Cơ sở dữ liệu quan hệ |
| AWS S3 | Lưu trữ ảnh và nhạc |
| JWT | Xác thực và phân quyền |
| Docker & Docker Compose | Triển khai và môi trường phát triển |

---

## 🗂️ Cấu trúc thư mục

```
spotify-api/
├── api/                  # Các view, serializer, models
├── spotify_api/          # Cấu hình chính của project
├── media/                # File media (nếu lưu local)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Cài đặt & chạy ứng dụng

### 🔧 1. Clone dự án
```bash
git clone https://github.com/your-username/spotify-api.git
cd spotify-api
```

### 🐍 2. Tạo môi trường ảo và cài package (nếu không dùng Docker)
```bash
python -m venv env
source env/bin/activate    # hoặc .\env\Scripts\activate với Windows
pip install -r requirements.txt
```

### 🐳 3. Chạy bằng Docker
```bash
docker-compose up --build
```

> Truy cập API: http://localhost:8000/

---

## 🧪 Kiểm thử API

- Sử dụng Postman hoặc Swagger UI tại: `http://localhost:8000/swagger/` (nếu có cấu hình).
- Thực hiện các thao tác:
  - Đăng ký: `POST /users/register/`
  - Đăng nhập: `POST /users/login/`
  - Thêm bài hát: `POST /songs/`
  - Tạo playlist: `POST /playlists/`

---

## 📸 Hình ảnh minh họa

> (Thêm ảnh chụp Swagger, ERD, UI nếu có)

---

## 👥 Thành viên thực hiện

| Họ tên | Vai trò |
|--------|---------|
| Nguyễn Văn A | Backend & JWT Auth |
| Trần Thị B | AWS S3 & Media Upload |
| Lê Văn C | API Playlist & Album |
| Phạm Thị D | Testing & Viết báo cáo |

---

## 📚 Tài liệu tham khảo

- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT.io](https://jwt.io/)
- [AWS S3 Docs](https://docs.aws.amazon.com/s3/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

---

## 📌 Ghi chú

> Đây là đồ án mô phỏng API Spotify đơn giản cho mục đích học tập.
