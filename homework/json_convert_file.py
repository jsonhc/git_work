#!/usr/bin/python3

import json
info = {"name": "wadeson","passwd": "redhat"}
with open("json_convert_file.txt","w") as f:
        json.dump(info,f)
