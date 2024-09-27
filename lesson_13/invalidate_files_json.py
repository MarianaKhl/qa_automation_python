import os
import json
import logging

# logging
logging.basicConfig(filename='json__khlivnenko.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_json_files(directory):
    # go through all the files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # checks if the filename ends on .json
            # creates the full path to the file by combining the directory and filename
            filepath = os.path.join(directory, filename)
            try:
                # open and check JSON file
                with open(filepath, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"{filename} - valid JSON file")
            except json.JSONDecodeError as e:
                logging.error(f"Error in the file {filename}: {str(e)}")
                print(f"{filename} - Invalid JSON file")

json_directory = '/Users/marianna/PycharmProjects/demo/automation_qa/ideas_for_test/work_with_json'
validate_json_files(json_directory)
