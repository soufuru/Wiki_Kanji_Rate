#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re


def remove(line):
    obj = json.loads(line)

    dst = str(obj["text"]).replace(" ", "").replace(r"[", "").replace(r"]", "").replace(r"{", "")
    dst = re.sub(r"<.*>", "", dst)
    dst = re.sub(r"==+", "", dst)

    return dst, obj
