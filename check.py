#!/usr/bin/env python3

import requests as rq
import os

env = os.environ
L7URL = env['L7URL'] if 'L7URL' in env else 'https://www.naver.com'
ERROR_FILE = env['ERROR_FILE'] if 'ERROR_FILE' in env else 'error.txt'

ERROR_MESSAGE = 'unknown error'

try:
    result = rq.get(L7URL)
    if result.status_code == 200:
        print(f"URL[{L7URL}] work well")
        exit(0)
    else:
        ERROR_MESSAGE = f"returned code : {result.status_code}"
except Exception as ex:
    ERROR_MESSAGE = str(ex)
    pass

with open(ERROR_FILE, "wt") as wf:
    print(ERROR_MESSAGE, file=wf)
    print(f"URL[{L7URL}] has following problem")
    print(ERROR_MESSAGE)

exit(1)
