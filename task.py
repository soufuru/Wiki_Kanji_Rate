#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import time
import unicodedata as ud

import matplotlib.font_manager
import matplotlib.pyplot as plt
import numpy as np

rm_process = __import__("remove_markup")

if __name__ == '__main__':

    # タイマースタート
    start = time.time()
    result = []

    for line in fileinput.input("-"):
        kanji = 0
        wordCount = 0

        dst, obj = rm_process.remove(line)

        # 漢字判定
        for ch in dst:
            if "CJK UNIFIED" in ud.name(ch, "error"):
                kanji += 1
            wordCount += 1

        # print(obj["title"] + format((kanji / chara), "1f"))
        result.append([obj["title"], float(format((kanji / wordCount), "1f"))])

    # 経過時間表示
    elapsed_time = time.time() - start
    print("\nelapsed_time:{0}".format(elapsed_time) + "[sec]")

    # グラフ表示関連

    result = dict(result)
    result = sorted(result.items(), key=lambda x: x[1])
    result.reverse()

    x = []
    y = []

    r = 30
    for i in range(r):
        x.insert(0, result[i][0])
        y.insert(0, result[i][1])

    plt.rcParams["figure.figsize"] = [18, 7]  # グラフのサイズを指定
    plt.rcParams['font.family'] = 'AppleGothic'  # 全体のフォントを設定
    fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Arial Unicode.ttf")
    plt.rcParams['font.size'] = 10

    plt.title(u"Wikipedia JSONデータの各記事における漢字を含む割合 TOP{}".format(r), fontproperties=fontprop)
    plt.barh(range(len(y)), y, height=0.4, align="center")
    y_loc = np.array(range(len(y)))

    fontsize = 250 / r
    plt.yticks(y_loc, x, rotation="horizontal", fontproperties=fontprop, fontsize=fontsize)

    plt.show()
