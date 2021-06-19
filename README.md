# Codegrepper Crawler

Đồ án môn học Truy Tìm Thông Tin 2021

## Crawl dữ liệu

### 1. Cài đặt Scrapy

Cài đặt Scrapy

`pip install scrapy`

### 2. Chạy Scrapy Spider

Di chuyển vào thư mục codegreppercrawler

`cd codegreppercrawler`

Chạy spider

`scrapy crawl code -o <file_name.json>`

**Lưu ý: Chỉnh sửa url trong start_urls của Scrapy Spider và hàm parse_answer để có đúng tag framework**

## Index dữ liệu

Phiên bản elasticsearch được sử dụng 7.12 hoặc 7.13.\
Chạy lần lượt các cell trong file codegrepper.ipynb để index, thiết lập mapping, analysis
