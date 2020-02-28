# Helper To Add Template for csv2po.py
# Tool of csv2po.py
# By Tom CHEN <tomchen.org@gmail.com> (tomchen.org)

import re
from pathlib import Path
from getfilepaths import getFilePaths


def log(s):
	printHead = 'WARNING: '
	f = Path('logfile.txt').open(mode = 'a+', newline = '\n', encoding = 'UTF-8')
	f.write(printHead + s + '\n')
	f.close()
	print(printHead + s)


def checkLfLine(path, lineNumber, line):
	LfFound = re.findall('(?<!\r)\n', line)
	LfFoundNumber = len(LfFound)
	if LfFoundNumber != 0:
		log(str(LfFoundNumber) + ' LF found in line ' + str(lineNumber) + ' of file ' + str(path))


def checkLf(path): # check LF (non CRLF)
	f = path.open(mode = 'r', newline = '\r\n', encoding = None)
	for i, line in enumerate(f):
		checkLfLine(path, i+1, line)
	f.close()


def addTransTemplate(path, skipRowNumber, inputPath, outputPath): # skipRowNumber: skip first N line, e.g. 1: skip first (one) line
	f = path.open(mode = 'r', newline = '\r\n', encoding = 'cp1252')
	p2 = outputPath.joinpath(path.relative_to(inputPath))
	p2.parent.mkdir(parents = True, exist_ok = True)
	f2 = p2.open(mode = 'w', newline = '')

	regex = '(?<=\t)[^\t^\r]+(?=\t|\r\n|$)'
	regex2 = '(?<=^)[^\t^\r]+(?=\t|\r\n|$)'
	def repl(g):
		s = g.group(0)
		if re.match(r'^\d+$', s) != None or \
		re.match(r'^\s+$', s) != None or \
		re.match(r'^""$', s) != None:
			return s
		else:
			return '_(TRANS)_'

	for i, line in enumerate(f):
		checkLfLine(path, i+1, line)
		if i < skipRowNumber:
			newline = line
		else:
			newline = re.sub(regex, repl, line)
			newline = re.sub(regex2, repl, newline)
		f2.write(newline)
	f.close()
	f2.close()


def batchAddTransTemplate(inputPath, outputPath, extList='txt', skipRowDict={}):
	# extList can be one string or a list of strings
	filePathList = getFilePaths(inputPath, extList)

	# skipRowDict is a dictionary that contains
	# {file name : number of row to skip} pair
	# (if number of row to skip is 1, you don't need to specify here)
	skipRowFileNmeList = list(skipRowDict.keys())

	for filePath in filePathList:
		fileName = str(filePath)
		if fileName in skipRowFileNmeList:
			skipRow = skipRowDict[fileName]
		else:
			skipRow = 1
		addTransTemplate(filePath, skipRow, inputPath, outputPath)

batchAddTransTemplate(Path('input'), Path('output'), ['txt', 'str'])
