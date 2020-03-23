#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform


Normal = '\033[0m'
Magenta = '\033[1;35m'
BoldRed = '\033[1;31m'
BoldWhite = '\033[1;37m'
BoldGreen = '\033[1;32m'


if platform.system() == 'Windows':
	from colorama import init
	init()


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

