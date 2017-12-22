#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import re
import time

rm_process = __import__("remove_markup")

if __name__ == '__main__':
    # タイマースタート
    start = time.time()
    result = []

    for line in fileinput.input("-"):
        kanji = 0
        chara = 0

        dst, obj = rm_process.remove(line)

        for ch in dst:
            matchOB = re.match('[一-龥]', ch)
            if matchOB:
                kanji += 1
            chara += 1
        # print(obj["title"] + format((kanji / chara), "1f"))
        # result.append([obj["title"], format((kanji / chara), "1f")])

    # 経過時間表示
    elapsed_time = time.time() - start
    print("\nelapsed_time:{0}".format(elapsed_time) + "[sec]")
