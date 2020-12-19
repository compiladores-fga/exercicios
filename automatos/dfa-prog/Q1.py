#!/usr/bin/env python3
if __name__ == "__main__":
	ent = input("digite a string que vai passar pelo automato\n")

	automato = {
		('A', 'b'): 'B',
		('B', 'c'): 'C',
		('B', 'b'): 'D',
		('B', 'a'): 'B',
		('C', 'a'): 'B',
		('D', 'b'): 'A'
	}

	init = 'A'
	fin = 'D'
	try:
		for x in ent:
			init = automato[(init, x)]
		if init == fin:
			print("Aceito")
		else:
			print("Rejeitado")
	except:
		print("Rejeitado")
