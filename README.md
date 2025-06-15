<div align="center">
  <h1>🚦 Đèn Giao Thông Ngã Tư - PIC16F887 🚦</h1>
  <p>✨ Dự án mô phỏng hệ thống đèn giao thông ngã tư thông minh sử dụng vi điều khiển <strong>PIC16F887</strong>.</p>
  <p>Hỗ trợ 3 chế độ hoạt động linh hoạt: tự động, điều khiển tay và cảnh báo ban đêm.</p>

  <p>
    <img src="https://img.shields.io/badge/PIC16F887-Vi%20x%E1%BB%AD%20l%C3%BD-brightgreen?style=for-the-badge&logo=microchip&logoColor=white" alt="PIC16F887 Badge">
    <img src="https://img.shields.io/badge/Ng%C3%B4n%20ng%E1%BB%AF-CCS%20C-blue?style=for-the-badge&logo=c&logoColor=white" alt="CCS C Badge">
    <img src="https://img.shields.io/badge/M%C3%B4%20ph%E1%BB%8Fng-Proteus-orange?style=for-the-badge&logo=proteus&logoColor=white" alt="Proteus Badge">
  </p>

---

  <p>
    <a href="#🚀-tổng-quan">Tổng quan</a> •
    <a href="#📁-cấu-trúc-dự-án">Cấu trúc dự án</a> •
    <a href="#🛠️-hướng-dẫn-sử-dụng">Hướng dẫn sử dụng</a> •
    <a href="#⚙️-chi-tiết-chức-năng">Chi tiết chức năng</a>
  </p>

---
</div>

<br>

## 🚀 Tổng quan

Đây là mô phỏng hệ thống **đèn giao thông tại một ngã tư** sử dụng **vi điều khiển PIC16F887**. Hệ thống hỗ trợ **3 chế độ hoạt động** linh hoạt được lựa chọn thông qua nút nhấn hoặc công tắc.

Mỗi chế độ đều mô phỏng chính xác cách vận hành của đèn giao thông thực tế:

1. **Chế độ 1 - Tự động:** Đèn đỏ, vàng, xanh luân phiên theo chu kỳ.
2. **Chế độ 2 - Điều khiển bằng tay:** Người dùng dùng nút nhấn để bật đèn thủ công.
3. **Chế độ 3 - Cảnh báo ban đêm:** 4 đèn vàng chớp tắt liên tục để cảnh báo.

<br>

## 📁 Cấu trúc Dự án

```bash
Den_Giao_Thong_Nga_Tu/
│
├── Code/
│   └── den_giao_thong.c       # Mã nguồn CCS C
│
├── Proteus/
│   └── den_giao_thong.pdsprj  # File mô phỏng Proteus
│
└── README.md                  # Mô tả dự án
<br>
