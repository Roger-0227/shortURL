# [ShortURL](http://54.95.125.250:8000/)（請點選標題）

- 縮短您的網址
- 可以取得網頁簡單資訊，例如：標題、描述
- 勾選是否啟用該短網址，未啟用則無法使用短網址
- 產生短網址 QRcode
- 或點擊 icon，將複製到剪貼簿

<div align="center">
    <img src="cover.png" alt="Image1" width="400">
    <img src="cover1.png" alt="Image2" width="400">
</div>

## 使用技術

- 後端：Python、Django、Alpine.js
- 部署：AWS EC2
- 套件：
  - django-tailwind
  - django-browser-reload
  - django-qr-code
  - beautifulsoup4

### 執行環境

1. poetry shell 虛擬環境
2. poetry install 下載 python 相應套件
