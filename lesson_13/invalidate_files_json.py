import os
import json
import logging
import requests

# logging
logging.basicConfig(filename='json__khlivnenko.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# download file from GitHub
json_urls = [
    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_json/localizations_en.json',
    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_json/localizations_ru.json',
    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_json/login.json',
    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_json/swagger.json'
]

def validate_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"{filepath} - valid JSON file")
    except json.JSONDecodeError as e:
        logging.error(f"Error in the file {filepath}: {str(e)}")
        print(f"{filepath} - Invalid JSON file")


for url in json_urls:
    filename = url.split('/')[-1]
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            validate_json_file(filename)
