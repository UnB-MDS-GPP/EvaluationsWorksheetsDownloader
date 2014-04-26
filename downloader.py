#!/usr/bin/env python

import os

list_2007 = open("link_list/link_list_2007.txt")
list_2010 = open("link_list/link_list_2010.txt")

for line in list_2007.readlines():
	file_name, file_href = line.split(";")
	os.system("wget -O ./2007/%s %s" % (file_name, file_href))

for line in list_2010.readlines():
	file_name, file_href = line.split(";")
	os.system("wget -O ./2010/%s %s" % (file_name, file_href))
