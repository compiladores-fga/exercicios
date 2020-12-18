#!/usr/bin/env python3
import re

if __name__ == "__main__":
	with open("fake.html") as fd:
		lorem = fd.read()
	patern = re.compile(r"<\s*img .*src=\".+\.gif\"")

	gifs = re.findall(
		patern,
		lorem)

	print("qtd de gifs", len(gifs))