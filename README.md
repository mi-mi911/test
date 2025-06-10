<div align="center">
  <h1>🚪✨ Cửa thông minh dùng ESP32 và Blynk ✨🚪</h1>
  <p>💡 Kho lưu trữ mã nguồn cho dự án cửa thông minh sử dụng vi điều khiển ESP32 và giao tiếp với nền tảng Blynk.</p>
  <p>Kiểm soát và giám sát cửa nhà bạn từ xa một cách dễ dàng và tiện lợi.</p>

  <p>
    <img src="https://img.shields.io/badge/Vi%20%C4%91i%E1%BB%83u%20khi%E1%BB%83n-ESP32-blueviolet?style=for-the-badge&logo=espressif&logoColor=white" alt="ESP32 Badge">
    <img src="https://img.shields.io/badge/N%E1%BB%81n%20t%E1%BA%A3ng-Blynk-brightgreen?style=for-the-badge&logo=blynk&logoColor=white" alt="Blynk Badge">
    <img src="https://img.shields.io/badge/M%C3%B4i%20tr%C6%B0%E1%BB%9Dng-PlatformIO%20(VS%20Code)-orange?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="PlatformIO Badge">
    <img src="https://img.shields.io/badge/Ng%C3%B4n%20ng%E1%BB%AF-C%2B%2B-blue?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++ Badge">
  </p>

  ---

  <p>
    <a href="#🚀-tổng-quan">Tổng quan</a> •
    <a href="#📁-cấu-trúc-dự-án">Cấu trúc dự án</a> •
    <a href="#🛠️-hướng-dẫn-cài-đặt-và-sử-dụng">Hướng dẫn cài đặt và sử dụng</a> •
    <a href="#⚙️-cấu-hình-blynk">Cấu hình Blynk</a> •
    <a href="#💡-tính-năng-chính">Tính năng chính</a> •
  </p>

  ---
</div>

<br>

## 🚀 Tổng quan

Chào mừng bạn đến với kho lưu trữ **`ESP32_Smart_door`**!

Dự án này cung cấp một giải pháp hoàn chỉnh cho việc xây dựng một hệ thống cửa thông minh, cho phép bạn điều khiển đóng/mở và giám sát trạng thái của cửa từ bất cứ đâu thông qua ứng dụng di động Blynk. Sử dụng vi điều khiển ESP32 mạnh mẽ, dự án này là sự kết hợp giữa phần cứng và phần mềm để mang lại sự tiện lợi và an toàn cho ngôi nhà của bạn.

<br>

## 📁 Cấu trúc Dự án

Kho lưu trữ được tổ chức một cách rõ ràng để bạn dễ dàng tìm kiếm và phát triển. Cấu trúc này tuân theo tiêu chuẩn của PlatformIO:
<br>

## 🛠️ Hướng dẫn cài đặt và sử dụng

Để triển khai dự án này, bạn cần có các phần mềm và thành phần phần cứng sau:

### Yêu cầu phần mềm:
1.  **VS Code:** Môi trường phát triển tích hợp (IDE) khuyến nghị.
2.  **PlatformIO IDE Extension:** Tiện ích mở rộng cần thiết cho VS Code để làm việc với PlatformIO.
3.  **Tải thư viện Blynk:** PlatformIO sẽ tự động quản lý các thư viện dựa trên `platformio.ini`.
4.  **Ứng dụng Blynk (Android/iOS):** Để tạo giao diện điều khiển và giám sát.

### Yêu cầu phần cứng:
* ESP32
* Servo SG90 (Mô phỏng cửa)
* Ma trận phím 4x4
* Breadboard, dây cắm hoặc vẽ PCB và hàn mạch

### Các bước cơ bản:

1.  **Cài đặt VS Code và PlatformIO IDE Extension:**
    * Tải xuống và cài đặt [Visual Studio Code](https://code.visualstudio.com/).
    * Mở VS Code, đi tới phần Extensions (biểu tượng khối vuông ở thanh bên trái), tìm kiếm và cài đặt `PlatformIO IDE`.
2.  **Clone hoặc tải về** kho lưu trữ này về máy tính của bạn:
    ```bash
    git clone [https://github.com/your-username/ESP32_Smart_door.git](https://github.com/your-username/ESP32_Smart_door.git)
    ```
3.  **Mở dự án trong VS Code với PlatformIO:**
    * Trong VS Code, nhấp vào biểu tượng PlatformIO ở thanh bên trái.
    * Chọn "Open Project" và điều hướng đến thư mục `ESP32_Smart_door` mà bạn vừa clone/tải về.
    * PlatformIO sẽ tự động cài đặt các dependencies (thư viện) được định nghĩa trong `platformio.ini`, mở file src và vào main.c để chỉnh sửa code.
4.  **Cấu hình thông tin Blynk và Wifi** (xem phần dưới).
5.  **Biên dịch và Upload mã nguồn:**
    * Trong thanh công cụ PlatformIO ở dưới cùng của VS Code, nhấp vào biểu tượng "Build" (dấu tích) để biên dịch mã nguồn.
    * Sau khi biên dịch thành công, nhấp vào biểu tượng "Upload" (mũi tên phải) để tải chương trình lên ESP32 của bạn.
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
Trước khi sử dụng, bạn cần làm theo các bước hướng dẫn sau. Nhập thông tin trên Blynk của bạn vào khoảng trống. Tiếp theo nhập tên và mật khẩu Wifi.
Trong file `src/main.cpp` (hoặc một file cấu hình riêng), bạn cần thay thế các placeholder sau bằng thông tin của mình:

```cpp
#define BLYNK_TEMPLATE_ID "YOUR_BLYNK_TEMPLATE_ID"
#define BLYNK_DEVICE_NAME "YOUR_BLYNK_TEMPLATE_NAME" // Tên thiết bị của bạn
#define BLYNK_AUTH_TOKEN "YOUR_BLYNK_AUTH_TOKEN"

char ssid[] = "YOUR_WIFI_SSID";     // Tên mạng Wifi của bạn
char pass[] = "YOUR_WIFI_PASSWORD"; // Mật khẩu Wifi của bạn
```
<div align="center">
<img src="data:image/jpeg;base64,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" alt="Thiết lập Datastreams trên Blynk">
</div>

💡 Tính năng chính
* Điều khiển từ xa: Đóng/mở cửa thông qua ứng dụng Blynk.
* Giám sát trạng thái: Nhận thông báo về trạng thái đóng/mở của cửa.
* Cảnh báo an ninh: Nhận cảnh báo khi có sự cố (ví dụ: cửa mở trái phép, nhập sai mật khẩu quá nhiều lần - nếu có tích hợp khóa số).
* Kết nối Wifi: Sử dụng ESP32 để kết nối với mạng Wifi nhà bạn.
&lt;br>
