import re
from datetime import datetime

def analyze_heartbeat_log(input_file_path, output_log_path, key="Key TSTFEED0300|7E3E|0400"):
    timestamp_pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")
    timestamps = []

    # Зчитування файлу та фільтрація за ключем
    with open(input_file_path, "r") as file:
        lines = file.readlines()
        filtered_lines = [line for line in lines if key in line]

    # Витягнення та парсинг часових міток
    for line in filtered_lines:
        match = timestamp_pattern.search(line)
        if match:
            time_str = match.group(1)
            try:
                timestamps.append(datetime.strptime(time_str, "%H:%M:%S"))
            except ValueError:
                continue  # Пропускаємо некоректні часові мітки

    # Аналіз інтервалів
    log_entries = []
    for i in range(len(timestamps) - 1):
        delta = (timestamps[i] - timestamps[i + 1]).total_seconds()
        event_time = timestamps[i].strftime("%H:%M:%S")

        if 31 < delta < 33:
            log_entries.append(f"[{event_time}] WARNING: Heartbeat delay {delta:.0f} seconds\n")
        elif delta >= 33:
            log_entries.append(f"[{event_time}] ERROR: Heartbeat delay {delta:.0f} seconds\n")

    # Запис у лог-файл
    with open(output_log_path, "w") as log_file:
        log_file.writelines(log_entries)

    print(f"Результати збережено в {output_log_path}")


# Приклад виклику функції:
if __name__ == "__main__":
    input_log = "data/hblog.txt"      # Вхідний лог-файл
    output_log = "logs/hb_test.log"     # Вихідний лог для помилок
    analyze_heartbeat_log(input_log, output_log)
