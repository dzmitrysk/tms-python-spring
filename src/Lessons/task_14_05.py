"""Задание 14.05
Создать скрипт, который принимает имя папки и создает ее рядом со скриптом"""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--folder-name', required=True)
parser.add_argument()
args = parser.parse_args()

print('Folder name:', args.folder_name)

os.mkdir(args.folder_name)
