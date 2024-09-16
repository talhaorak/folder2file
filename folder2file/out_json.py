import json


def format_json(data, no_newline):
    if no_newline:
        return json.dumps(data, separators=(',', ':'))
    return json.dumps(data, indent=2)
