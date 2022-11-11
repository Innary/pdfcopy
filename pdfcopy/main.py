#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-11 11:29:23
@ LastEditors: Innary
@ LastEditTime: 2022-11-11 12:33:11
'''


from time import sleep
import pyperclip
 
def remove_empty_line(text):
    source_content = text.replace('\n','').replace('\r', '')
    return source_content


def main():
    while True:
        sleep(0.5)
        Content=remove_empty_line(pyperclip.paste())
        if Content != pyperclip.paste():
            pyperclip.copy(Content)
            print("now clipboard content:",Content[0:3],"~~~~~",Content[-2:])

if __name__ == '__main__':
    main()