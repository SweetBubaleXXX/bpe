import json
import os
import sys
from datetime import datetime


def update_time(obj: dict):
    def _update_field(_obj: dict):
        if "updated" in _obj:
            _obj["updated"] = cur_time
        for sub_obj in _obj.values():
            if isinstance(sub_obj, dict):
                _update_field(sub_obj)

    cur_time = datetime.now().isoformat()
    _update_field(obj)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No path specified", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    with open(path, "r+") as f:
        content = json.load(f)
        update_time(content)
        f.seek(0, os.SEEK_SET)
        f.truncate(0)
        json.dump(content, f, indent=2)
