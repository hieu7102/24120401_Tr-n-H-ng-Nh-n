# Text Generation API using GPT-2 (Hugging Face Inference API)

## Thông tin sinh viên

* Họ và tên: **Trần Hùng Nhân**
* MSSV: **24120401**
* Môn học: **Tư duy tính toán**

---

## Mô hình sử dụng

* Tên mô hình: **openai-community/gpt2**
* Nguồn: Hugging Face
* Link: https://huggingface.co/openai-community/gpt2

---
## Mô tả hệ thống

Hệ thống xây dựng một Web API sử dụng FastAPI để sinh văn bản từ mô hình GPT-2.

Thay vì tải model về máy, hệ thống sử dụng Hugging Face Inference API để thực hiện suy luận trực tuyến, giúp giảm tài nguyên và tăng tốc độ triển khai.

---

## Cài đặt thư viện

### Bước 1: Tạo môi trường

```bash
python -m venv venv
```

### Bước 2: Kích hoạt môi trường

```bash
venv\Scripts\activate
```

### Bước 3: Cài thư viện

```bash
pip install -r requirements.txt
```

---

## Hướng dẫn chạy chương trình

Chạy server bằng lệnh:

```bash
uvicorn main:app --reload
```

Sau khi chạy thành công, truy cập:

```text
http://127.0.0.1:8000/docs
```

để sử dụng giao diện Swagger UI.

---

## Hướng dẫn gọi API

### 1. API kiểm tra hệ thống

```http
GET /
```

**Response:**

```json
{
  "message": "Text Generation API (Online Model)"
}
```

---

### 2. API kiểm tra trạng thái

```http
GET /health
```

**Response:**

```json
{
  "status": "ok"
}
```

---

### 3. API sinh văn bản

```http
POST /generate
```

**Request:**

```json
{
  "prompt": "AI will change the world because"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "input": "AI will change the world because",
    "output": "AI will change the world because..."
  }
}
```

---

## Example Output

**Input:**

```json
{
  "prompt": "Explain AI"
}
```

 **Output:**

```json
{
  "success": true,
  "data": {
    "input": "Explain AI",
    "output": "Explain AI in modern society..."
  }
}
```
---
## Cấu trúc project

```bash
Lab_API/
├── main.py
├── test_api.py
├── requirements.txt
└── README.md
```

---

## Demo Video

[![Watch Demo](https://img.icons8.com/ios-filled/100/000000/video.png)](https://drive.google.com/uc?export=download&id=1eYyVq_OC6UGxBw3B6mJOFUl-ef1rZLr3)


