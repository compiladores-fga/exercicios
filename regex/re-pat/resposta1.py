#!/usr/bin/env python3
import re

def replace_logic(matchobj):
	return f"{matchobj.group('day')}{matchobj.group('bar1')}{matchobj.group('month')}{matchobj.group('bar2')}{matchobj.group('year')}"

if __name__ == "__main__":
	with open("fake_text.txt") as fd:
		lorem = fd.read()

	brazil_date_lorem = re.sub(
		r"(?P<month>\d{2})(?P<bar1>/)(?P<day>\d{2})(?P<bar2>/)(?P<year>\d{4})",
		replace_logic,
		lorem)

	with open("fake_text.txt","w") as fd:
		fd.write(brazil_date_lorem)
