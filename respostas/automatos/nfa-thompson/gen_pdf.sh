#!/bin/bash
if latexmk -lualatex && latexmk -c; then
	echo "OK!"
else
	echo "FAIL!"
fi
