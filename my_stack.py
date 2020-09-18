#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  my_stack.py - Demonstrates implementation of a simple stack in Python3, Version 1.0
#  Copyright (c) 2020 ArdeshirV@protonmail.com, Licensed under GPLv3+
from color import *


def main(args):
    print_title_and_copyright()
    s = my_stak()  # Call my_stack contructor to create a new instance of my_stack.

    if len(args) > 1:
        for index in range(1, len(args)):
            try:
                f = float(args[index])  # Test the command line argument.
            except:                     # if it wasn't a number then show error message.
                message = ('{0}Error: The \'{1}{2}{3}\' is not a number!' +
                    '\n       Please specify only numbers as command line arguments.{4}')
                print(message.format(BoldRed, BoldGreen,
                    args[index], BoldRed, BoldWhite))
                sys.exit(0)
            s.push(args[index])
    else:
        # if there is not commad line arguments then use below sample data.
        s.push(2)  # Each push method puts a new data top of stack.
        s.push(4)
        s.push(6)
        s.push(8)

    print('{0}{1}{2}{3}{4}'.format(
        BoldWhite, 'List: ', BoldGreen, s.get_list_as_string(), Normal))

    result = 0.0
    output = ''
    while not s.is_empty():
        data = s.pop()  # pop() method returns data top of stack and then remove it.
        result += float(data)
        output = '{0}{1}{2}'.format(output, data, ' + ')
    output = output[0:-3]
    print('{0}{1} = {2}{3}{4}'.format(BoldWhite, output, Magenta, result, Normal))

    return 0


class node:
    def __init__(self, data, node):
        self.data = data
        self.node = node


class my_stak:
    def __init__(self):
        self.num = -1
        self.root = None

    def get_list_as_string(self):
        n = self.root
        output = ''
        while n is not None:
            output += '{0}{1}'.format(n.data, ', ')
            n = n.node
        output = output[0:-2] + '.'
        return output

    def push(self, data):
        self.root = node(data, self.root)
        self.num += 1

    def pop(self):
        data = None
        if self.root != None:
            data = self.root.data
            old_root = self.root
            self.root = self.root.node
            self.free(old_root)
        self.num -= 1
        return data

    def free(self, node):  # We need free method to free resources from specified node
        pass  # There is nothing to do here!

    def peek(self):
        return self.root.data

    def is_empty(self):
        return self.num <= -1


if __name__ == '__main__':
    from sys import argv, exit
    exit(main(argv))
