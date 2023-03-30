troom,tcond=map(int,input().split())
r=input()
if (r=='freeze' and troom>=tcond) or (r=='heat' and troom<=tcond):
	print(tcond)
if (r=='heat' and troom>tcond) or (r=='freeze' and troom<tcond):
	print(troom)
if r=='auto':
	print(tcond)
if r=='fan':
	print(troom)