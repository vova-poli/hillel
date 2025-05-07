import xml.etree.ElementTree as ET
import logging
import os

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Шлях до XML-файлу
xml_path = "../ideas_for_test/work_with_xml/groups.xml"

# Функція пошуку incoming за номером групи
def get_incoming_by_group_number(group_number: int):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and int(number.text) == group_number:
                incoming = group.find("timingExbytes/incoming")
                if incoming is not None:
                    logging.info(f"group {group_number} incoming: {incoming.text}")
                    return incoming.text
                else:
                    logging.info(f"group {group_number} has no incoming value.")
                    return None

        logging.info(f"group {group_number} not found.")
        return None

    except ET.ParseError as e:
        logging.error(f"Error parsing XML: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Приклад виклику
if __name__ == "__main__":
    get_incoming_by_group_number(2)
