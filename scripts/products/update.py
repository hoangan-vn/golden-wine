import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_CSV_PATH = REPO_ROOT / ".data" / "products.csv"
OUTPUT_CSV_PATH = REPO_ROOT / ".data" / "products_updated.csv"
SKU_FIELD_NAME = "Variant SKU"


def load_csv_rows(csv_path: Path) -> tuple[list[dict], list[str]]:
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        sys.exit(1)
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    if not fieldnames:
        print("Could not read CSV header.")
        sys.exit(1)
    if SKU_FIELD_NAME not in fieldnames:
        print(f"Column '{SKU_FIELD_NAME}' not found in CSV.")
        sys.exit(1)
    return rows, fieldnames


def save_csv_rows(csv_path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def print_divider() -> None:
    print("-" * 80)


def print_row_fields(fieldnames: list[str], row: dict) -> None:
    print_divider()
    print("Fields and current values (enter number to update):")
    for index, field in enumerate(fieldnames, start=1):
        value = row.get(field, "")
        print(f"{index}. {field}: {value}")
    print_divider()


def select_index(prompt: str, min_value: int, max_value: int) -> int | None:
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "exit":
            return None
        if user_input.lower() == "quit":
            return -2
        if user_input.lower() in {"next"}:
            return -1
        if not user_input.isdigit():
            print("Please enter a valid number, 'next' to skip, 'exit' to save and exit, or 'quit' to exit without saving.")
            continue
        idx = int(user_input)
        if idx < min_value or idx > max_value:
            print(f"Please choose a number between {min_value}..{max_value}.")
            continue
        return idx


def choose_row_for_sku(rows: list[dict], fieldnames: list[str], sku: str) -> int | None:
    matched_indices: list[int] = [i for i, r in enumerate(rows) if (r.get(SKU_FIELD_NAME, "") or "").strip() == sku]
    if not matched_indices:
        print(f"SKU not found: {sku}")
        return None
    if len(matched_indices) == 1:
        return matched_indices[0]

    print_divider()
    print(f"Found {len(matched_indices)} rows for SKU '{sku}'. Choose a row to edit:")
    for choice, row_index in enumerate(matched_indices, start=1):
        row = rows[row_index]
        title = row.get("Title", "")
        handle = row.get("Handle", "")
        price = row.get("Variant Price", "")
        print(f"{choice}. Handle='{handle}', Title='{title}', Variant Price='{price}'")
    print_divider()

    selected = select_index("Enter row number: ", 1, len(matched_indices))
    if selected is None:
        return None
    if selected == -1:
        return None
    if selected == -2:
        return -2
    return matched_indices[selected - 1]


def edit_row_interactively(fieldnames: list[str], row: dict) -> str | None:
    while True:
        print_row_fields(fieldnames, row)
        print("Enter field number to update, 'next' to change SKU, 'exit' to save and exit, 'quit' to exit without saving.")
        selected = select_index("Your choice: ", 1, len(fieldnames))
        if selected is None:
            return "exit"
        if selected == -1:
            return "next"
        if selected == -2:
            return "quit"

        field = fieldnames[selected - 1]
        current_value = row.get(field, "")
        print(f"Field: {field}")
        print(f"Current value: {current_value}")
        new_value = input("Enter new value (leave empty to clear, type 'cancel' to skip): ").strip()
        if new_value.lower() == "cancel":
            continue
        row[field] = new_value
        print("Updated.")


def main() -> None:
    print("Loading data from CSV...")
    rows, fieldnames = load_csv_rows(INPUT_CSV_PATH)
    print(f"Loaded {len(rows)} rows. SKU column: '{SKU_FIELD_NAME}'.")

    save_on_exit = True
    while True:
        sku = input("Enter SKU to edit (type 'next' to skip, 'exit' to save and exit, 'quit' to exit without saving): ").strip()
        if not sku:
            continue
        if sku.lower() == "exit":
            break
        if sku.lower() == "quit":
            save_on_exit = False
            break
        if sku.lower() == "next":
            continue

        row_index = choose_row_for_sku(rows, fieldnames, sku)
        if row_index is None:
            continue
        if isinstance(row_index, int) and row_index == -2:
            save_on_exit = False
            break

        action = edit_row_interactively(fieldnames, rows[row_index])
        if action == "exit":
            break
        if action == "quit":
            save_on_exit = False
            break
        # if action == "next" then continue loop

    if save_on_exit:
        print("Saving updated file...")
        save_csv_rows(OUTPUT_CSV_PATH, rows, fieldnames)
        print(f"Saved: {OUTPUT_CSV_PATH}")
    else:
        print("Exited without saving changes.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nReceived interrupt signal. Exiting without saving changes.")
        sys.exit(130)


