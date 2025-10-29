import pandas as pd
from pathlib import Path
import sys

# Xác định đường dẫn gốc của dự án
REPO_ROOT = Path(__file__).resolve().parents[1]

# Xác định đường dẫn đến các tệp input và output
INPUT_CSV_PATH = REPO_ROOT / ".data" / "products.csv"
OUTPUT_EXCEL_PATH = REPO_ROOT / ".data" / "products.xlsx"

def convert_csv_to_excel(csv_path: Path, excel_path: Path):
    """
    Đọc một tệp CSV và chuyển đổi nó thành một tệp Excel (.xlsx).

    Args:
        csv_path (Path): Đường dẫn đến tệp CSV đầu vào.
        excel_path (Path): Đường dẫn để lưu tệp Excel đầu ra.
    """
    try:
        # Kiểm tra xem tệp CSV có tồn tại không
        if not csv_path.is_file():
            print(f"❌ Lỗi: Không tìm thấy tệp CSV tại '{csv_path}'")
            sys.exit(1)

        print(f"🔄 Đang đọc tệp CSV từ: '{csv_path}'...")
        # Đọc tệp CSV bằng pandas
        df = pd.read_csv(csv_path)

        print(f"✍️ Đang ghi ra tệp Excel tại: '{excel_path}'...")
        # Ghi DataFrame ra tệp Excel, không bao gồm cột chỉ mục (index) của pandas
        df.to_excel(excel_path, index=False)

        print(f"✅ Chuyển đổi thành công! Đã lưu tệp tại: '{excel_path}'")

    except Exception as e:
        print(f"❌ Đã xảy ra lỗi trong quá trình chuyển đổi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Chạy hàm chuyển đổi
    convert_csv_to_excel(INPUT_CSV_PATH, OUTPUT_EXCEL_PATH)
