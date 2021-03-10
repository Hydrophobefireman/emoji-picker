import json
import requests
from pathlib import Path

URL = "https://raw.githubusercontent.com/amio/emoji.json/master/emoji.json"
loc = "./src/data/emoji.json"


def get_emojis():
    print(f"Fetching: {URL}")
    return requests.get(URL).json()


def generate():
    ret = []
    for i in get_emojis():
        if i["group"].lower() == "component":
            continue
        obj = {}
        obj["emoji"] = i["char"]
        obj["description"] = i["name"]
        obj["category"] = i["group"]
        obj["tags"] = [*i["name"].split(), *i["subgroup"].split("-")]
        ret.append(obj)
    Path(loc).write_text(json.dumps(ret))
    print(f"Saved to {loc}")


if __name__ == "__main__":
    generate()