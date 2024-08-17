import json
import os


def save_json(content, file_path):        
    with open(file_path, 'w') as file:
        file.write(json.dumps(content, ensure_ascii=False, indent=2))
    print("Write to %s successfully." % file_path)


def save_file(content, file_path):
    # if file does not exist, create it
    if not os.path.exists(os.path.dirname(file_path)):
        print("Creating directory %s" % os.path.dirname(file_path))
        os.makedirs(os.path.dirname(file_path))
        with open(file_path, 'w') as file:
            file.write(content)
        print("Write to %s successfully." % file_path)


def open_file(file_path):
    # if file does not exist, create it
    if not os.path.exists(file_path):
        print("Creating file %s" % file_path)
        with open(file_path, 'w') as file:
            file.write("[]")
            file.close()

    with open(file_path, 'r') as file:
        return file.read()


def open_json(file_path):
    return json.loads(open_file(file_path))