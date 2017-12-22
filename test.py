#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import fileinput

rm_process = __import__("remove_markup")

if __name__ == '__main__':

    for line in fileinput.input("-"):

        dst, obj = rm_process.remove(line)

        if obj["title"] == "イギリス":
            print(dst)
