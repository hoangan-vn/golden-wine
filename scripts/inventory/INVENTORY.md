# INVENTORY CSV – Shopify

File CSV này được sử dụng để quản lý và cập nhật tồn kho trên Shopify.

## Cấu trúc cột

* **Handle**
  Định danh duy nhất của sản phẩm, trùng với slug trong URL.
  Ví dụ: `the-glenlivet-21y`.

* **Title**
  Tên sản phẩm hiển thị trong Shopify Admin.
  Ví dụ: `THE GLENLIVET 21Yo`.

* **Option1 Name / Option1 Value**
  Thuộc tính biến thể 1 (ví dụ: Size, Color).
  Nếu chỉ có một biến thể thì thường là `Title / Default Title`.

* **Option2 Name / Option2 Value**
  Thuộc tính biến thể 2 (nếu có).

* **Option3 Name / Option3 Value**
  Thuộc tính biến thể 3 (nếu có).

* **SKU**
  Mã SKU (Stock Keeping Unit) để quản lý tồn kho.

* **HS Code**
  Mã HS cho mục đích hải quan khi vận chuyển quốc tế.

* **COO** (Country of Origin)
  Quốc gia sản xuất sản phẩm.

* **Location**
  Tên kho lưu trữ hàng hóa. Phải trùng với tên kho trong Shopify.
  Ví dụ: `Go Vap`.

* **Bin name**
  Mã ô/kệ trong kho (tuỳ chọn).

* **Incoming (not editable)**
  Số lượng hàng đang trên đường nhập kho. Shopify tự động tính, không chỉnh sửa bằng CSV.

* **Unavailable (not editable)**
  Số lượng không khả dụng (ví dụ đang bị khóa). Shopify tự động tính.

* **Committed (not editable)**
  Số lượng đã được đặt trong đơn hàng nhưng chưa giao. Shopify tự động tính.

* **Available (not editable)**
  Số lượng khả dụng thực tế để bán = On hand – Committed. Shopify tự động tính.

* **On hand (current)**
  Số lượng hiện có trong hệ thống tại thời điểm export CSV.

* **On hand (new)**
  Số lượng mới muốn cập nhật. Khi import lại vào Shopify, hệ thống sẽ overwrite tồn kho bằng giá trị này.

## Lưu ý khi cập nhật

* Chỉ chỉnh sửa cột **On hand (new)** để thay đổi tồn kho.
* Các cột "not editable" không được sửa vì Shopify sẽ bỏ qua.
* Nếu để trống **On hand (new)** thì tồn kho sẽ không thay đổi.
* Có thể xuất file CSV từ Shopify Admin, cập nhật giá trị, rồi import lại.
