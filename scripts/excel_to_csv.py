import pandas as pd
from pathlib import Path
import sys

# Xác định đường dẫn gốc của dự án
REPO_ROOT = Path(__file__).resolve().parents[1]

# Xác định đường dẫn đến các tệp input và output
INPUT_EXCEL_PATH = REPO_ROOT / ".data" / "products.xlsx"
OUTPUT_CSV_PATH = REPO_ROOT / ".data" / "product_convert.csv"

def convert_excel_to_csv(excel_path: Path, csv_path: Path):
    """
    Đọc một tệp Excel (.xlsx) và chuyển đổi nó thành một tệp CSV.
    Nếu tệp CSV đã tồn tại, nó sẽ được ghi đè.

    Args:
        excel_path (Path): Đường dẫn đến tệp Excel đầu vào.
        csv_path (Path): Đường dẫn để lưu tệp CSV đầu ra.
    """
    try:
        # Kiểm tra xem tệp Excel có tồn tại không
        if not excel_path.is_file():
            print(f"❌ Lỗi: Không tìm thấy tệp Excel tại '{excel_path}'")
            sys.exit(1)

        print(f"🔄 Đang đọc tệp Excel từ: '{excel_path}'...")
        # Đọc tệp Excel bằng pandas (mặc định sẽ đọc sheet đầu tiên)
        df = pd.read_excel(excel_path)

        print(f"✍️ Đang ghi ra tệp CSV tại: '{csv_path}'...")
        # Ghi DataFrame ra tệp CSV, không bao gồm cột chỉ mục (index) của pandas
        df.to_csv(csv_path, index=False, encoding='utf-8')

        print(f"✅ Chuyển đổi thành công! Đã lưu tệp tại: '{csv_path}'")

    except Exception as e:
        print(f"❌ Đã xảy ra lỗi trong quá trình chuyển đổi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Chạy hàm chuyển đổi
    convert_excel_to_csv(INPUT_EXCEL_PATH, OUTPUT_CSV_PATH)
