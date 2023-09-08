import random
Inicial=[]
Aptos=[]
Ib=[]
N=30
M=0
G=0
#primer paso
for i in range(1, N+1):
    Inicial.append(random.randint(0,15))
print('Valores : ',Inicial)
print()
#segundo paso
for x in Inicial:
    M = (x**2)+2
    Aptos.append(M)
print('Aptitud : ',Aptos)
print()
#tercer paso
maxAP=Aptos[0]
for y in Aptos:
    if y > maxAP:
      maxAP = y
#paso intermedio
maxG=Inicial[0]
for z in Inicial:
    if z > maxG:
      maxG = z
print('Evaluación del Más apto  : ',maxAP, ' Genotipo  : ',maxG)
print()
#cuarto paso
#decimal a binario

for w in Inicial:
  T=format(w,"b")
  Ib.append(T)
print(Ib)
print()
H1=0
H2=0
numr1=random.randint(0,30)
numr2=random.randint(0,30)
H1=Ib[numr1]
H2=Ib[numr2]
print('Valores aleatorios seleccionados : ',H1,H2)

