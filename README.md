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
![Image](https://github.com/user-attachments/assets/fcbd7521-018a-412e-ab2a-13345259e6de)
</div>

💡 Tính năng chính
* Điều khiển từ xa: Đóng/mở cửa thông qua ứng dụng Blynk.
* Giám sát trạng thái: Nhận thông báo về trạng thái đóng/mở của cửa.
* Cảnh báo an ninh: Nhận cảnh báo khi có sự cố (ví dụ: cửa mở trái phép, nhập sai mật khẩu quá nhiều lần - nếu có tích hợp khóa số).
* Kết nối Wifi: Sử dụng ESP32 để kết nối với mạng Wifi nhà bạn.
&lt;br>
