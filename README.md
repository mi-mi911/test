<div align="center">
  <h1>🌱 Hệ Thống Giám Sát & Điều Khiển Cây Trồng Thông Minh - ESP32 🌤️</h1>
  <p>✨ Dự án tích hợp cảm biến và điều khiển tự động hệ thống nông nghiệp nhỏ với <strong>ESP32</strong> và <strong>Dashboard + App điện thoại</strong>.</p>
  <p>Hệ thống có thể theo dõi <strong>nhiệt độ, độ ẩm, ánh sáng</strong> và điều khiển <strong>tưới cây, quạt tránh ẩm, mái che</strong> một cách thông minh.</p>

  <p>
    <img src="https://img.shields.io/badge/ESP32-Microcontroller-brightgreen?style=for-the-badge&logo=espressif&logoColor=white" alt="ESP32 Badge">
    <img src="https://img.shields.io/badge/Ngôn ngữ-Arduino C++-blue?style=for-the-badge&logo=arduino&logoColor=white" alt="Arduino Badge">
    <img src="https://img.shields.io/badge/Giám sát-App%20điện%20thoại%20+%20Web-orange?style=for-the-badge&logo=firebase&logoColor=white" alt="App Badge">
  </p>

---

  <p>
    <a href="#🚀-tổng-quan">Tổng quan</a> •
    <a href="#🛠️-hướng-dẫn-sử-dụng">Hướng dẫn sử dụng</a> •
    <a href="#⚙️-chi-tiết-chức-năng">Chi tiết chức năng</a> •
    <a href="#📷-giao-diện-dashboard">Giao diện Dashboard</a>
  </p>

---
</div>

<br>

## 🚀 Tổng quan

Dự án này mô phỏng **hệ thống giám sát và điều khiển môi trường cây trồng** thông minh dựa trên **ESP32**. Hệ thống có khả năng:

- **Đọc dữ liệu** từ cảm biến nhiệt độ, độ ẩm, và ánh sáng.
- **Hiển thị thời gian thực** trên **dashboard web/app điện thoại** (Firebase).
- **Tự động điều khiển** tưới cây, bật quạt, đóng/mở mái che dựa theo điều kiện cài đặt.
- Cho phép **điều khiển thủ công** qua app từ xa.

<br>

## 🛠️ Hướng dẫn Sử dụng

### 🔧 Yêu cầu phần mềm
1. Arduino IDE / PlatformIO – Biên dịch và nạp mã nguồn vào ESP32.

2. Firebase Realtime Database – Lưu trữ và đồng bộ dữ liệu giám sát.

3. App điện thoại / Dashboard Web – Điều khiển từ xa.

### 📥 Các bước triển khai
1. Tải dự án:
   
2. Mở thư mục bằng Arduino IDE hoặc PlatformIO và cấu hình:
   ```bash
  WiFi SSID & password
  Firebase host & token
  ```

5. Nạp chương trình vào ESP32.

6. Mở dashboard/index.html trên trình duyệt hoặc điện thoại để giám sát và điều khiển.

7. Quan sát dữ liệu nhiệt độ, độ ẩm, ánh sáng hiển thị và kiểm soát thiết bị bằng nút.

<br>
⚙️ Chi tiết chức năng
| Thành phần        | Chức năng                                                    |
|-------------------|--------------------------------------------------------------|
| Nhiệt độ / Độ ẩm  | Đọc bằng cảm biến DHT11 / DHT22                              |
| Ánh sáng          | Đọc bằng cảm biến quang trở / LDR                            |
| Tưới cây          | Tự động bật khi độ ẩm dưới ngưỡng / Điều khiển từ app       |
| Quạt thông gió    | Bật khi độ ẩm quá cao / Điều khiển thủ công                 |
| Mái che           | Đóng/mở khi ánh sáng quá gắt hoặc theo lệnh người dùng       |
| Dashboard Web/App | Hiển thị dữ liệu và gửi lệnh điều khiển (qua Firebase)      |
<br>
📷 Giao diện Dashboard
🌤️ Màn hình giám sát


📱 Giao diện trên điện thoại


⚠️ Bạn có thể tùy chỉnh giao diện theo ý muốn bằng cách sửa file dashboard/index.html.

<div align="center"> <br> <p>💚 Cảm ơn bạn đã ghé repo! Nếu bạn thấy dự án này hữu ích, hãy ⭐ và fork để phát triển thêm nhé!</p> </div> ```
