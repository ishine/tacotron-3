
# -*- coding: utf-8 -*-  

import os
import argparse
import shutil
import re
import platform
import sys
pattern='^\d{6}'

def FilePathDelimiter():
	if (platform.system() == 'Windows'):
		return '\\'
	elif (platform.system() == 'Linux'):
		return '/'
	else:
		print('unknow OS')
		sys.exit(0)
		

def make_tacotron2_text(SrcFile,TxtPath,count):	
	frd=open(SrcFile,'r')
	rdLines = frd.readlines()
	fwt = open(TxtPath,'w')
	num = 0
	for mLine in rdLines:
		ret = re.search(pattern,mLine,flags=0)		
		if ret == None:			
			if f_name == '':
				print(mLine + ' is error\n')
				continue
			sname = mLine.split('\t')
			print(sname)
			inStr = f_name + '|' + sname[1]
			fwt.write(inStr)
			num += 1
			if num >= count:
				break
		else:
			sname = mLine.split('\t')
			f_name = sname[0]
	frd.close()
	fwt.close()
#针对标贝开源数据,提取word层的文本,形成tacotron2的训练文本
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--src_file', '-wd', required=True)
	parser.add_argument('--csv_file', '-td', required=True)
	parser.add_argument('--count','-count', required=True)
	args = parser.parse_args()	
	SrcFile = args.src_file
	CsvFile = args.csv_file
	count = int(args.count)
	make_tacotron2_text(SrcFile,CsvFile,count)
