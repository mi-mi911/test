<div align="center">
  <h1>🚪✨ Cửa thông minh dùng ESP32 và Blynk ✨🚪</h1>
  <p>💡 Kho lưu trữ mã nguồn cho dự án cửa thông minh sử dụng vi điều khiển ESP32 và giao tiếp với nền tảng Blynk.</p>
  <p>Kiểm soát và giám sát cửa nhà bạn từ xa một cách dễ dàng và tiện lợi.</p>

  <p>
    <img src="https://img.shields.io/badge/Vi%20%C4%91i%E1%BB%81u%20khi%E1%BB%83n-ESP32-blueviolet?style=for-the-badge&logo=espressif&logoColor=white" alt="ESP32 Badge">
    <img src="https://img.shields.io/badge/N%E1%BB%81n%20t%E1%BA%A3ng-Blynk-brightgreen?style=for-the-badge&logo=blynk&logoColor=white" alt="Blynk Badge">
    <img src="https://img.shields.io/badge/Ng%C3%B4n%20ng%E1%BB%AF-Arduino%20C%2B%2B-blue?style=for-the-badge&logo=arduino&logoColor=white" alt="Arduino C++ Badge">
  </p>

  ---

  <p>
    <a href="#🚀-tổng-quan">Tổng quan</a> •
    <a href="#📁-cấu-trúc-dự-án">Cấu trúc dự án</a> •
    <a href="#🛠️-hướng-dẫn-cài-đặt-và-sử-dụng">Hướng dẫn cài đặt và sử dụng</a> •
    <a href="#⚙️-cấu-hình-blynk">Cấu hình Blynk</a> •
    <a href="#💡-tính-năng-chính">Tính năng chính</a> •
    <a href="#🤝-đóng-góp">Đóng góp</a> •
    <a href="#📄-giấy-phép">Giấy phép</a>
  </p>

  ---
</div>

<br>

## 🚀 Tổng quan

Chào mừng bạn đến với kho lưu trữ **`ESP32_Smart_door`**!

Dự án này cung cấp một giải pháp hoàn chỉnh cho việc xây dựng một hệ thống cửa thông minh, cho phép bạn điều khiển đóng/mở và giám sát trạng thái của cửa từ bất cứ đâu thông qua ứng dụng di động Blynk. Sử dụng vi điều khiển ESP32 mạnh mẽ, dự án này là sự kết hợp giữa phần cứng và phần mềm để mang lại sự tiện lợi và an toàn cho ngôi nhà của bạn.

<br>

## 📁 Cấu trúc Dự án

Kho lưu trữ được tổ chức một cách rõ ràng để bạn dễ dàng tìm kiếm và phát triển:
<br>

## 🛠️ Hướng dẫn cài đặt và sử dụng

Để triển khai dự án này, bạn cần có các phần mềm và thành phần phần cứng sau:

### Yêu cầu phần mềm:
1.  **Arduino IDE:** Để biên dịch và upload mã nguồn lên ESP32.
2.  **Thư viện ESP32 Board trong Arduino IDE:** Cần cài đặt để lập trình cho ESP32.
3.  **Thư viện Blynk:** Cần cài đặt trong Arduino IDE để giao tiếp với nền tảng Blynk.
4.  **Ứng dụng Blynk (Android/iOS):** Để tạo giao diện điều khiển và giám sát.

### Yêu cầu phần cứng:
* ESP32 Development Board
* Module rơ le (Relay module)
* Cảm biến từ (Reed switch) hoặc cảm biến cửa khác
* Các dây jumper và breadboard (nếu cần)

### Các bước cơ bản:

1.  **Clone hoặc tải về** kho lưu trữ này về máy tính của bạn:
    ```bash
    git clone [https://github.com/your-username/ESP32_Smart_door.git](https://github.com/your-username/ESP32_Smart_door.git)
    ```
2.  **Mở dự án trong Arduino IDE:** Mở file `main.ino` trong thư mục `src/`.
3.  **Cài đặt các thư viện cần thiết:**
    * Trong Arduino IDE, đi tới `Sketch > Include Library > Manage Libraries...`
    * Tìm kiếm và cài đặt `Blynk by Volodymyr Shymanskyy`.
    * Đảm bảo bạn đã cài đặt board ESP32 trong `Tools > Board > Boards Manager...`.
4.  **Cấu hình thông tin Blynk và Wifi** (xem phần dưới).
5.  **Biên dịch và Upload mã nguồn** lên ESP32 của bạn.
6.  **Kết nối phần cứng** theo sơ đồ mạch (tham khảo thư mục `schematics/`).
7.  **Thiết lập ứng dụng Blynk** trên điện thoại (xem phần dưới).

<br>

## ⚙️ Cấu hình Blynk

Để dự án hoạt động, bạn cần cấu hình tài khoản và dự án Blynk của mình.

### 1. Tạo dự án mới trên Blynk Console
* Truy cập [Blynk Console](https://blynk.cloud/) và tạo một tài khoản (nếu chưa có).
* Tạo một **New Template** cho dự án "Smart Door".
* Ghi lại **Template ID** và **Template Name**.
* Khi tạo thiết bị mới từ Template này, bạn sẽ nhận được một **Auth Token**.

### 2. Cập nhật thông tin vào mã nguồn
Trong file `main.ino` (hoặc một file cấu hình riêng), bạn cần thay thế các placeholder sau bằng thông tin của mình:

```cpp
#define BLYNK_TEMPLATE_ID "YOUR_BLYNK_TEMPLATE_ID"
#define BLYNK_DEVICE_NAME "YOUR_BLYNK_TEMPLATE_NAME" // Tên thiết bị của bạn
#define BLYNK_AUTH_TOKEN "YOUR_BLYNK_AUTH_TOKEN"

char ssid[] = "YOUR_WIFI_SSID";     // Tên mạng Wifi của bạn
char pass[] = "YOUR_WIFI_PASSWORD"; // Mật khẩu Wifi của bạn
