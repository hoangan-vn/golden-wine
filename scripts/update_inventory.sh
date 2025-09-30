#!/bin/bash

# Đường dẫn đến file Python
SCRIPT_PATH="/scripts/inventory/update.py"

# File input và output
INPUT_FILE="inventory.csv"
OUTPUT_FILE="inventory_updated.csv"

# Số lượng tồn kho mới (tham số 1)
NEW_STOCK=$1

# Kiểm tra tham số đầu vào
if [ -z "$NEW_STOCK" ]; then
  echo "❌ Vui lòng nhập số lượng tồn kho mới."
  echo "Cách dùng: ./scripts/update_inventory.sh <so_luong>"
  exit 1
fi

# Chạy Python script
python3 "$SCRIPT_PATH" "$INPUT_FILE" "$OUTPUT_FILE" "$NEW_STOCK"
