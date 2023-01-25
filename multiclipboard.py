import sys
import clipboard
import json

SAVED_DATA_FILE = 'clipboard.json'


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


def clear_data(filepath):
    try:
        with open(filepath, 'w') as f:
            data = json.load(f)
            del data
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA_FILE)

    # check to make sure command is a valid command
    if command == "save":  # save current clipboard to a set "key"
        key = input("Enter a key to save: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA_FILE, data)
        print("Data Saved!")
    elif command == "load":  # load value associated with a set key onto your clipboard
        key = input("Enter a key to load:")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipbaord!')
        else:
            print("Please enter a valid key!")
    elif command == "list":  # list all values currently saved
        for d in data:
            print(d + ": " + data[d])
    elif command == "clear":  # clear clipboard
        clear_data(SAVED_DATA_FILE)
        print("Successfully cleared clipboard!")
    else:
        print("unknown command")
else:
    print("Please pass exactly one command.")
