<div align="center">
  <h1>🚪 Cửa thông minh dùng ESP và Blynk ✨</h1>
  <p>💡 Dự án hệ thống cửa thông minh tích hợp vi điều khiển ESP và nền tảng Blynk để điều khiển và giám sát từ xa.</p>

  <p>
    <img src="https://img.shields.io/badge/N%E1%BB%81n%20t%E1%BA%A3ng-ESP32%2FESP8266-blueviolet?style=for-the-badge&logo=espressif&logoColor=white" alt="ESP Badge">
    <img src="https://img.shields.io/badge/Giao%20ti%E1%BA%BFp-Blynk-brightgreen?style=for-the-badge&logo=blynk&logoColor=white" alt="Blynk Badge">
    <img src="https://img.shields.io/badge/Ng%C3%B4n%20ng%E1%BB%AF-C%2B%2B-blue?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++ Badge">
  </p>

  ---

  <p>
    <a href="#🚀-tổng-quan">Tổng quan</a> •
    <a href="#🛠️-hướng-dẫn-cài-đặt-và-sử-dụng">Hướng dẫn cài đặt và sử dụng</a> •
    <a href="#🤝-đóng-góp">Đóng góp</a> •
    <a href="#📄-giấy-phép">Giấy phép</a>
  </p>

  ---
</div>

<br>

## 🚀 Tổng quan

Chào mừng bạn đến với dự án **Cửa thông minh dùng ESP và Blynk**!

Dự án này cung cấp một giải pháp tự động hóa cửa, cho phép bạn điều khiển và giám sát cửa từ xa thông qua ứng dụng Blynk trên điện thoại di động hoặc trình duyệt web. Nó kết hợp sức mạnh của vi điều khiển ESP (ESP32/ESP8266) với sự tiện lợi của nền tảng Blynk để tạo ra một hệ thống an toàn và linh hoạt.

<br>

## 🛠️ Hướng dẫn cài đặt và sử dụng

Để triển khai và sử dụng dự án này, bạn cần thực hiện các bước cấu hình dưới đây:

### 1. Cấu hình thông tin Blynk

[cite_start]Trước khi sử dụng, bạn cần làm theo các bước hướng dẫn sau. [cite_start]Bạn cần nhập thông tin Template ID, Template Name và Auth Token của dự án Blynk của bạn vào các khoảng trống trong mã code.

```cpp
#define BLYNK_TEMPLATE_ID "YOUR_BLYNK_TEMPLATE_ID"    // Nhập Template ID của bạn
#define BLYNK_TEMPLATE_NAME "YOUR_BLYNK_TEMPLATE_NAME"  // Nhập Template Name của bạn
#define BLYNK_AUTH_TOKEN "YOUR_BLYNK_AUTH_TOKEN"     // Nhập Auth Token của bạn

2. Cấu hình thông tin Wifi
Tiếp theo, nhập tên và mật khẩu Wifi. Bạn cần nhập tên và mật khẩu Wifi mà thiết bị ESP sẽ kết nối vào các biến ssid và pass.

C++

char ssid[] = "tên Wifi";         // Nhập tên Wifi của bạn
char pass[] = "mật khẩu Wifi";    // Nhập mật khẩu Wifi của bạn
3. Thiết lập Datastreams trên Blynk
Bạn cần thiết lập các Datastreams (luồng dữ liệu) trên Blynk như sau:

Control Door:

ID: 1
Name: Control Door
Pin: V0
Data Type: Integer
Mục đích: Thiết lập công tắc ảo Control Door để đóng mở cửa từ xa.
Control Pass:

ID: 2
Name: Control Pass
Pin: V1
Data Type: Integer
Mục đích: Thiết lập công tắc ảo Control Pass để điều khiển việc cho phép và không cho phép nhập mật khẩu.
4. Thiết lập Events & Notifications trên Blynk
Bạn cần thiết lập để nhận thông báo khi cửa mở và khi nhập sai mật khẩu quá nhiều lần.

door_warning:

ID: 4
Name: door_warning
Code: door_warning
Type: Warning
Mục đích: Nhận thông báo khi cửa mở.
infor_log:

ID: 5
Name: infor_log
Code: infor_log
Type: Info
Mục đích: Nhận thông báo khi nhập sai mật khẩu quá nhiều lần.
&lt;br>

🤝 Đóng góp
Mọi đóng góp để cải thiện dự án đều được hoan nghênh! Nếu bạn có bất kỳ ý tưởng, đề xuất hoặc phát hiện lỗi nào, vui lòng tạo một pull request hoặc mở một vấn đề (issue) trên GitHub.
