#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import json
import re
import time
import unicodedata as ud

if __name__ == '__main__':

    # タイマースタート
    start = time.time()
    result = []

    for line in fileinput.input("-"):
        kanji = 0
        chara = 0

        obj = json.loads(line)

        dst = str(obj["text"]).replace(" ", "").replace(r"[", "").replace(r"]", "").replace(r"{", "")
        dst = re.sub(r"<.*>", "", dst)
        dst = re.sub(r"==+", "", dst)

        for ch in dst:
            name = ud.name(ch, "error")
            if "CJK UNIFIED" in name:
                kanji += 1
            chara += 1

        result.append([obj["title"], format((kanji / chara), "1f")])

    # 経過時間表示
    elapsed_time = time.time() - start
    print("\nelapsed_time:{0}".format(elapsed_time) + "[sec]")

    # result.sort()
    result = dict(result)
