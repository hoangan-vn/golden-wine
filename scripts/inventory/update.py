import pandas as pd

# Nhập file gốc
input_file = ".data/inventory.csv"
output_file = ".data/inventory_updated.csv"

# Nhập số lượng tồn kho mới
new_stock = int(input("Nhập số lượng tồn kho mới: "))

# Đọc file CSV
df = pd.read_csv(input_file)

# Cập nhật cột "On hand (new)" với giá trị mới
df["On hand (new)"] = new_stock

# Xuất ra file CSV mới
df.to_csv(output_file, index=False)

print(f"✅ File đã được cập nhật và lưu thành '{output_file}'")
