# 🚗 Waze HUD Custom Studio Pro

Web Studio tùy biến giao diện, mô phỏng HUD và nạp Firmware trực tuyến (WebSerial API + Web Bluetooth API) cho các dòng phần cứng ESP32 Waze HUD:
- **ESP32-2432S024 (CYD 2.4" 320x240 ngang)**: Chế độ Hắt Kính Lái (Windshield Mirror Mode), Big-Hero HUD, đổi chiều cổng sạc $180^\circ$, cảnh báo Onboard RGB LED.
- **ESP32-2424S012 (GC9A01 240x240 tròn)**: Chế độ HUD tròn siêu sáng, lật gương kính lái.

## 🌐 Trải nghiệm trực tuyến:
👉 **[https://nhoxboo.github.io/waze-hud-studio/](https://nhoxboo.github.io/waze-hud-studio/)**

## ✨ Tính năng chính:
- **WebSerial 1-Click Flasher**: Nạp trực tiếp file firmware All-in-One qua cáp Type-C trong trình duyệt Chrome / Edge (Baudrate 921600).
- **Web Bluetooth (BLE) Live Sync**: Kết nối không dây trực tiếp với thiết bị HUD để tùy biến màu sắc neon, tên hiển thị cá nhân hóa `[⚡ HOÀI NAM]`, ngưỡng cảnh báo quá tốc độ, bù trừ sai số GPS.
- **HUD Driving Simulator**: Bộ mô phỏng tốc độ, biển báo, camera phạt nguội và mũi tên ngã rẽ trực quan.
- **Nền tảng bảo mật HTTPS**: Chạy 100% trên GitHub Pages bảo mật, hỗ trợ đầy đủ Web Serial & Web Bluetooth API.
