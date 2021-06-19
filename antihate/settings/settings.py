import string
import json


def get_parm(name: string):
    with open("../antihate/settings/settings.json", "r") as read_file:
        try:
            json_file = json.load(read_file)
            return json_file[name]
        except KeyError:
            return None


def set_parm(key: string, value: string):
    with open("../antihate/settings/settings.json", "r") as read_file:
        json_file = json.load(read_file)
        json_file[key] = value
        with open('../antihate/settings/settings.json', 'w') as f:
            json.dump(json_file, f, indent=4)
            return None


