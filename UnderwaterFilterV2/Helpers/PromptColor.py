"""
Just print stuff in blue and red in the terminal

2022.12.22  Originally created  Hyunjin Cho
"""

def StringInBlue(string):
    return ('%s'+ string +'%s') %('\033[34m','\033[0m')

def StringInRed(string):
    return ('%s'+ string +'%s') %('\033[31m','\033[0m')