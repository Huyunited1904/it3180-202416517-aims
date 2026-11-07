# Trả lời câu hỏi Lab 01

## 1. Vì sao dùng git mv?

git mv giúp di chuyển hoặc đổi tên file và đưa thay đổi vào
staging trong một lệnh. Trong bài này, em dùng lệnh để chuyển
dvd.py và cart.py vào thư mục aims.

Git nhận diện việc đổi tên dựa trên sự tương đồng nội dung.
Em có thể dùng git log --follow để xem lịch sử file qua lần
di chuyển.

## 2. release/lab01 có phải baseline không?

Có. Khi được chọn làm phiên bản thống nhất để nộp bài,
trạng thái trên release/lab01 đóng vai trò baseline của Lab 01.
Đây là mốc để kiểm tra và so sánh với các phiên bản sau.

Nhánh vẫn có thể thay đổi, nên khi sửa bài đã nộp cần tuân thủ
quy trình hotfix và Pull Request.

## 3. Vì sao không commit thẳng master dù làm một mình?

Làm trên nhánh riêng giúp tách phần đang thay đổi khỏi nhánh
chính. Pull Request giúp xem lại code, ghi rõ mục đích và
kết quả kiểm thử trước khi merge.

Cách làm này giúp truy vết thay đổi và rèn quy trình làm việc
nhóm. Các commit trực tiếp ban đầu là bước khởi tạo theo lab;
sau đó các thay đổi được đưa vào master qua Pull Request.