#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-11 11:29:23
@ LastEditors: Innary
@ LastEditTime: 2022-11-11 13:40:34
'''

import argparse
from time import sleep
import pyperclip
 
def get_args_parser():
    parser = argparse.ArgumentParser('PDF copy-paste', add_help=False)
    parser.add_argument('--remove_r_only', '-r', action='store_true')
    parser.add_argument('--remove_n_only', '-n', action='store_true')
    return parser
def remove_empty_line(text, type=None):
    if type == 'r':
        source_content = text.replace('\r','')
    elif type =='n':
        source_content = text.replace('\n','')
    else:
        source_content = text.replace('\n','').replace('\r', '')
    return source_content

def main():
    parser = get_args_parser()
    args = parser.parse_args()
    type = None
    if args.remove_r_only:
        type = 'r'
    elif args.remove_n_only:
        type = 'n'
    elif args.remove_r_only and args.remove_n_only:
        raise ValueError
    while True:
        sleep(0.5)
        Content=remove_empty_line(pyperclip.paste(), type)
        if Content != pyperclip.paste():
            pyperclip.copy(Content)
            print("now clipboard content:",Content[0:3],"~~~~~",Content[-2:])

if __name__ == '__main__':
    main()