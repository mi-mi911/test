---

# 🚪 ESP32/ESP8266 Smart Door Lock with Blynk 🔒

## ✨ Giới thiệu

Dự án này là một hệ thống khóa cửa thông minh (Smart Door Lock) sử dụng vi điều khiển ESP32 hoặc ESP8266, tích hợp với nền tảng IoT Blynk để điều khiển và giám sát từ xa. Hệ thống cho phép người dùng đóng/mở cửa từ xa, kiểm soát việc nhập mật khẩu và nhận thông báo về trạng thái của cửa.

## 🚀 Tính năng chính

* **Điều khiển cửa từ xa:** Mở hoặc đóng cửa thông qua ứng dụng Blynk.
* **Kiểm soát quyền nhập mật khẩu:** Bật/tắt khả năng nhập mật khẩu trên thiết bị thông qua công tắc ảo trên Blynk.
* **Thông báo trạng thái cửa:** Nhận thông báo khi cửa mở và khi nhập sai mật khẩu quá nhiều lần.

## 🛠️ Phần cứng yêu cầu

* Vi điều khiển ESP32 hoặc ESP8266 (ví dụ: NodeMCU ESP32, ESP8266 Wemos D1 Mini, v.v.).
* Module khóa cửa điện tử (solenoid lock hoặc servo).
* Các cảm biến cần thiết (ví dụ: cảm biến trạng thái cửa, keypad cho nhập mật khẩu).
* Dây nối, Breadboard (nếu cần).
* Nguồn cấp phù hợp cho ESP và module khóa.

## ⚙️ Hướng dẫn cài đặt

[cite_start]Trước khi sử dụng, bạn cần làm theo các bước hướng dẫn sau:

### 1. Cấu hình Blynk Template ID, Template Name và Auth Token

[cite_start]Trong code của dự án, bạn cần nhập thông tin từ Blynk của bạn vào các khoảng trống tương ứng:

```cpp
#define BLYNK_TEMPLATE_ID   "..."
#define BLYNK_TEMPLATE_NAME "..."
#define BLYNK_AUTH_TOKEN    "..."
