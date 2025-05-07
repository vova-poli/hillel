import json
import os
import logging

# Шляхи до JSON-файлів
json_folder = "../ideas_for_test/work_with_json"
json_files = [
    "swagger.json",
    "localizations_en.json",
    "localizations_ru.json",
    "login.json"
]

# Налаштування логування
log_dir = "logs"
log_file = "json__Polishchuk.log"
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, log_file)

logging.basicConfig(
    filename=log_path,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Перевірка кожного JSON-файлу
def validate_json_files(folder, filenames):
    for filename in filenames:
        full_path = os.path.join(folder, filename)
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"{filename} is not valid JSON. Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error with {filename}: {e}")

# Виклик функції
if __name__ == "__main__":
    validate_json_files(json_folder, json_files)
    print(f"Validation complete. Check '{log_path}' for errors.")
