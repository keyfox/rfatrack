import json


def load_progress(path, default=lambda: {}):
    try:
        with open(path) as f:
            p = json.load(f)
    except FileNotFoundError:
        p = default()
    return p


def save_progress(progress, path):
    with open(path, "w") as f:
        json.dump(progress, f)
