# Changelog

Tất cả thay đổi đáng chú ý của dự án AIMS-mini được ghi lại tại đây.

## [Unreleased]
### Fixed
- Sửa lỗi tìm kiếm DVD theo tên không phân biệt chữ hoa và chữ thường (v1.0.1).

## [1.1.0] - 2026-11-07

### Added
- Thêm chức năng sắp xếp giỏ hàng theo tên DVD.
- Thêm chức năng sắp xếp giỏ hàng theo giá DVD.
- Thêm chức năng tìm kiếm DVD theo thể loại.

## [1.0.0] - 2026-11-07

### Added
- Chức năng quản lý DVD trong giỏ hàng.
- Tìm kiếm DVD theo tiêu đề bằng `search_by_title()`.
- Hiển thị thông tin giỏ hàng bằng `Cart.print_cart()`.
- Tính tổng tiền và áp dụng giảm giá bằng `total_cost_with_discount()`.
- Bổ sung unit tests cho các chức năng của Cart.

### Fixed
- Sửa lỗi giỏ hàng cho phép thêm DVD thứ 21 khi đã đạt giới hạn 20 DVD.
- Sửa lỗi tính toán số tiền sau khi giảm giá.