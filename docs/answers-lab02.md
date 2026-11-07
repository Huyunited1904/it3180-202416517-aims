# Trả lời thảo luận Lab 02

## 1. Vì sao phải đồng bộ master trước khi tạo PR?

Để kiểm tra tính năng với code mới nhất và xử lý xung đột sớm.
Nhánh càng lâu không đồng bộ thì càng dễ phát sinh xung đột.

## 2. Khi nào không nên rebase?

Không rebase các commit đã chia sẻ mà người khác đang dựa vào,
vì rebase tạo mã commit mới và làm thay đổi lịch sử chung.

## 3. feature/* khác topic/* thế nào?

feature/* dùng để phát triển tính năng.
topic/* dùng cho các công việc hỗ trợ như tài liệu và cấu hình.

## 4. Ba kiểu merge khác nhau thế nào?

- Merge commit: giữ các commit của nhánh và tạo commit gộp.
- Squash and merge: gộp thay đổi của nhánh thành một commit.
- Rebase and merge: đưa các commit lên đầu nhánh đích,
  tạo lịch sử tuyến tính và mã commit mới.

## 5. Vì sao cần review lại sau khi push thêm commit?

Vì code sau lần push đã khác code được duyệt trước đó.
Cần kiểm tra lại để bảo đảm phiên bản cuối đủ điều kiện merge.