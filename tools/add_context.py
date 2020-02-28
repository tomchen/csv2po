# Batch Add Context
# Tool of csv2po.py
# By Tom CHEN <tomchen.org@gmail.com> (tomchen.org)

import re
from pathlib import Path
from getfilepaths import getFilePaths


def addContext(inputPath, outputPath, encoding, context):
	f = inputPath.open(mode = 'r', encoding = encoding, newline = '', errors = "strict")
	content = f.read()
	f.close()
	content = content.replace("_(TRANS)_", "_(TRANS_CONTEXT:'" + context + "')_")
	outputPath.parent.mkdir(parents = True, exist_ok = True)
	fout = outputPath.open(mode = 'w', encoding = encoding, newline = '', errors = "strict")
	content = fout.write(content)
	fout.close()


def batchAddContext(inputPath, extension, encoding, outputPath, filePathToContextFunc):
	for p in getFilePaths(inputPath, extension = extension):
		addContext(inputPath = p, outputPath = outputPath.joinpath(p.relative_to(inputPath)), encoding = encoding, context = filePathToContextFunc(p))


def fn2c(filePath):
	fileName = filePath.name.lower()
	ext = filePath.suffix.lower()
	stem = filePath.stem.lower()
	if ext == '.txt':
		return stem
	else:
		return fileName

batchAddContext(inputPath = Path('template_without_context'), extension = ['txt', 'str', 'ini'], encoding = 'UTF-8', outputPath = Path('.'), filePathToContextFunc = fn2c)
