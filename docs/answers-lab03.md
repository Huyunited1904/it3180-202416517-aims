# Lab 03 – Bugfix Flow, Merge Conflict và Hoàn tác

## 1. Bugfix Flow
- Tạo Issue để ghi nhận lỗi giới hạn số lượng DVD trong giỏ hàng.
- Tạo nhánh `bugfix/cart-limit-off-by-one` để sửa lỗi.
- Viết unit test, sửa code và tạo Pull Request.
- Sử dụng `Fixes #8` để liên kết commit với Issue.

## 2. Bugfix từ Feature Branch
- Tạo nhánh `feature/discount`.
- Tạo nhánh `bugfix/discount-calculation` để sửa công thức giảm giá.
- Merge bugfix vào feature, sau đó merge feature vào master.

## 3. Merge Conflict
- Tạo hai nhánh thay đổi cùng một dòng trong `aims/cart.py`.
- Xử lý xung đột bằng cách kết hợp thông báo tiếng Việt với tên DVD.
- Chạy unit test và hoàn tất merge.

## 4. Reset và Reflog
- `git reset --soft`: Bỏ commit nhưng giữ thay đổi trong Staging Area.
- `git reset --mixed`: Bỏ staging, giữ thay đổi trong Working Directory.
- `git reset --hard`: Đưa nhánh và thư mục làm việc về commit được chỉ định.
- `git reflog`: Tìm và khôi phục commit đã bị reset.

## 5. Revert
- Tạo nhánh `bugfix/revert-show-added-title`.
- Sử dụng `git revert -m 1` để hoàn tác merge commit PR #13.
- Tạo Pull Request và merge vào master mà không viết lại lịch sử.

## 6. Kiểm thử
Chạy lệnh:

`python -m unittest discover -s tests -v`

Kết quả hiện tại: 2 tests – OK.

## 7. Kết luận
Đã thực hành quy trình sửa lỗi, giải quyết xung đột và hoàn tác thay đổi bằng Git/GitHub. Phân biệt được reset và revert, đồng thời hiểu vai trò của Pull Request trong việc quản lý lịch sử thay đổi.