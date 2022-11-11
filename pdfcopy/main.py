#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-11 11:29:23
@ LastEditors: Innary
@ LastEditTime: 2022-11-11 23:30:30
'''

import argparse
from time import sleep
import pyperclip
import copy
def get_args_parser():
    parser = argparse.ArgumentParser('PDF copy-paste', add_help=False)
    parser.add_argument('--split', '-s', action='store_true')
    return parser


def spilt_sentence(text):
    source_content = text.replace('. ','. \n  ').replace('。','。\n  ')
    return source_content


def remove_empty_line(text, split=False):
    source_content = text.replace('\r','\\').replace('\n','\\').replace('\\\\', ' ')
    if split:
        source_content = spilt_sentence(source_content)
        
    return source_content


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    cache = remove_empty_line(pyperclip.paste(), args.split)
    while True:
        sleep(0.5)
        if cache != pyperclip.paste():
            content=remove_empty_line(pyperclip.paste(), args.split)
            cache = content
            pyperclip.copy(content)
            print("clipboard content INFO    ",content[:7],"  ......  ",content[-7:])

if __name__ == '__main__':
    main()