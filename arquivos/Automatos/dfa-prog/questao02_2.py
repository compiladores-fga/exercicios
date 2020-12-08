def afd(delta, q, F, w):
	for s in w:
		try:
			q = delta[(q, s)]
		except:
			return False
	if q in F:
		return True
	return False

delta = {('A', 'b'): 'B',
		('B', 'a'): 'B',
		('B', 'b'): 'D',
		('B', 'c'): 'C',
		('C', 'a'): 'B',
		('D', 'b'): 'A'}

if afd(delta, 'B', ['C'], input()):
	print("Aceito")
else:
	print("Rejeitado")
