# Báo cáo Lab 05 – Hotfix và Cherry-pick

## 1. Mục tiêu

Thực hành quy trình phát hành phiên bản, sửa lỗi khẩn cấp (hotfix) và đồng bộ bản sửa lỗi giữa các nhánh bằng `git cherry-pick -x`.

## 2. Chuẩn bị phiên bản 1.1.0

- Bổ sung chức năng tìm kiếm DVD theo thể loại `search_by_category()`.
- Hoàn thiện các chức năng sắp xếp giỏ hàng.
- Cập nhật `CHANGELOG.md` và `__version__` thành `1.1.0`.
- Tạo nhánh `release/lab05` để chuẩn bị phát hành.

## 3. Phát hiện và sửa lỗi

Phát hiện hàm `search_by_title()` phân biệt chữ hoa và chữ thường, khiến từ khóa `"lion"` không tìm được DVD `"The Lion King"`.

Đã tạo nhánh `hotfix/search-case-insensitive` từ `release/lab04`, sửa hàm tìm kiếm và bổ sung unit test.

Commit sửa lỗi gốc:

`7baceb2e55668709e66b3c130bf064a1fd90d7c2`

Sau khi kiểm thử thành công, cập nhật phiên bản `1.0.1`, tạo Pull Request vào `release/lab04` và phát hành tag `v1.0.1`.

## 4. Đồng bộ bản sửa lỗi

Sử dụng `git cherry-pick -x` để đưa commit sửa lỗi sang hai nhánh:

- `master`: commit `1ce25d4`.
- `release/lab05`: commit `394eb52`.

Trong quá trình cherry-pick đã xảy ra xung đột tại `tests/test_search.py` do cả hai nhánh đều có bài kiểm thử riêng.

Đã giải quyết xung đột bằng cách giữ lại cả bài test tìm kiếm theo thể loại và bài test tìm kiếm không phân biệt chữ hoa/thường.

## 5. Kiểm thử

| Phiên bản | Số bài kiểm thử | Kết quả |
|---|---:|---|
| `v1.0.1` | 5 | OK |
| `v1.1.0` | 8 | OK |
| `master` | 8 | OK |

## 6. Kết quả

- Hoàn thành hotfix cho phiên bản `1.0.0`.
- Phát hành thành công tag `v1.0.1` và `v1.1.0`.
- Đồng bộ bản sửa lỗi sang `master` và `release/lab05`.
- Giải quyết merge conflict khi cherry-pick.
- Kiểm thử thành công trên cả ba phiên bản.

## 7. Bài học rút ra

Hotfix cần được tạo từ nhánh chứa phiên bản bị lỗi. Khi đồng bộ bản sửa sang các nhánh phát triển khác, `git cherry-pick -x` giúp chỉ lấy commit cần thiết và lưu lại nguồn gốc của commit. Khi có conflict, cần kết hợp các thay đổi phù hợp thay vì chỉ giữ một phía.