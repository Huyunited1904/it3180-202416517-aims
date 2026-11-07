# Báo cáo thực hành Lab 04 – Release Management

## 1. Chuẩn bị phiên bản v1.0.0

- Tạo nhánh `topic/prepare-release-1.0.0` từ `master`.
- Khai báo `__version__ = "1.0.0"` trong `aims/__init__.py`.
- Hiển thị phiên bản ứng dụng trong `main.py`.
- Tạo `CHANGELOG.md` để theo dõi thay đổi giữa các phiên bản.
- Tạo Pull Request và merge vào `master`.

## 2. Quản lý nhánh release và tag

- Tạo và push nhánh `release/lab04`.
- Tạo các annotated tag `v0.1.0`, `v0.2.0`, `v0.3.0` và `v1.0.0`.
- Các tag cũ tham chiếu tới các nhánh release tương ứng.
- Tạo GitHub Release `v1.0.0` với tiêu đề `AIMS-mini v1.0.0`.

## 3. Phát triển tính năng sau khi phát hành

- Tạo nhánh `feature/sort-cart`.
- Bổ sung hai phương thức `sort_by_title()` và `sort_by_cost()` cho lớp `Cart`.
- Viết thêm hai bài kiểm thử tương ứng.
- Chạy bộ kiểm thử gồm 6 tests, kết quả thành công.
- Cập nhật phần `[Unreleased]` trong `CHANGELOG.md`.
- Merge tính năng vào `master`.

## 4. Kiểm tra release baseline

Kiểm tra mã nguồn tại tag `v1.0.0` và nhánh `master`:

- Tag `v1.0.0` chứa thông tin phiên bản `1.0.0`.
- Tag `v1.0.0` chưa chứa các phương thức sắp xếp giỏ hàng.
- Nhánh `master` đã có các phương thức sắp xếp.

Điều này cho thấy phiên bản phát hành được giữ nguyên, trong khi nhánh phát triển tiếp tục nhận tính năng mới.

## 5. Branch Protection

Cấu hình ruleset `protect-release-branches` với pattern `release/*`:

- Hạn chế xóa nhánh.
- Chặn force push.
- Yêu cầu Pull Request trước khi merge.
- Required approvals: 0, do dự án được thực hiện cá nhân.

Lưu ý: Hiệu lực thực tế của ruleset phụ thuộc vào chính sách GitHub áp dụng cho repository và tài khoản.

## 6. Status Accounting

Các thành phần cấu hình đã được quản lý và theo dõi:

| Thành phần | Trạng thái |
|---|---|
| `master` | Nhánh phát triển chính |
| `release/lab04` | Nhánh lưu mốc phát hành Lab 04 |
| `v0.1.0` | Tag Lab 01 |
| `v0.2.0` | Tag Lab 02 |
| `v0.3.0` | Tag Lab 03 |
| `v1.0.0` | Tag phiên bản phát hành chính thức |
| `CHANGELOG.md` | Theo dõi lịch sử thay đổi |
| `feature/sort-cart` | Đã merge vào `master` |

## 7. Kết luận

Lab 04 giúp thực hành quy trình quản lý phát hành phần mềm bằng Git và GitHub, bao gồm quản lý phiên bản, nhánh release, annotated tag, GitHub Release, kiểm soát thay đổi và theo dõi trạng thái cấu hình.