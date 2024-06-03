p=str(input("Ingrese palabra: ")).lower()
if p.count(" ")>0:
    p=p[0:p.index(" ")]+p[p.index(" ")+1:len(p)]
l=len(p)
p2=""
for i in range (l):
    p2+=(p[(l-1)-i])
p2.lower()
if p2==p:
    print("Su palabra es un palindromo")
    print(f"Palabra Ingresada: {p}")
    print(f"Palabra al inverso: {p2}")
else: 
    print("Su palabra no es un palindromo")
    print(f"Palabra Ingresada: {p}")
    print(f"Palabra al inverso: {p2}")