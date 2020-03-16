#!/usr/bin/env python
#  my_stack.py - Demonstrates implementation of a simple stack in Python3, Version 1.0
#  Copyright (c) 2020 ArdeshirV@protonmail.com, Licensed under GPLv3+
# -*- coding: utf-8 -*-
import sys
import platform


def main(args):
	Normal = '\033[0m'
	Magenta = '\033[1;35m'
	BoldRed = '\033[1;31m'
	BoldWhite = '\033[1;37m'
	BoldGreen = '\033[1;32m'

	if platform.system() == 'Windows':
		from colorama import init
		init()

	print_title_and_copyright()

	s = my_stak()  # Call my_stack contructor to create a new instance of my_stack.
	
	if len(args) > 1:
		for index in range(1, len(args)):
			try:
				f = float(args[index])  # Test the command line argument.
			except:                     # if it wasn't a number then show error message.
				message = ('{0}Error: The \'{1}{2}{3}\' is not a number!' +
					'\nPlease specify only numbers as command line arguments.{4}')
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
			free(old_root)
		self.num -= 1
		return data
		
	def free(self, node):  # We need free method to free resources from specified node
		pass  # There is nothing to do here!
		
	def peek(self):
		return self.root.data
		
	def is_empty(self):
		return self.num <= -1


def print_title_and_copyright():
    blnColor = True  # False if (platform.system() == 'Windows') else True
    strAppName = "my_stack"
    strAppYear = "2020"
    strAppDescription = "Demonstrates implementation of a simple stack in Python3"
    strVersion = "1.0"
    strLicense = "GPLv3+"
    strCopyright = "ArdeshirV@protonmail.com"
    print(FormatTitle(strAppName, strAppDescription, strVersion, blnColor))
    print(FormatCopyright(strAppYear, strCopyright, strLicense, blnColor))


def FormatTitle(strAppName, strAppDescription, strVersion, blnColor):
    NoneColored = "{} - {} Version {}\n"
    Colored = "\033[1;33m{}\033[0;33m - {} \033[1;33mVersion {}\033[0m"
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppName, strAppDescription, strVersion)


def FormatCopyright(strAppYear, strCopyright, strLicense, blnColor):
    NoneColored = "Copyright (c) {} {}, Licensed under {}\n\n"
    Colored = ("\033[0;33mCopyright (c) \033[1;33m{} \033[1;34m{}" +
               "\033[0;33m, Licensed under \033[1;33m{}\033[0m\n")
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppYear, strCopyright, strLicense)


if __name__ == '__main__':
	from sys import argv
	sys.exit(main(argv))
