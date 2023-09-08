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
print('Valores (Muesta inicial) : ',Inicial)
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
print('Lista de muestra inicial en binario ↓ ')
for w in Inicial:
  T=format(w,"b").zfill(4)
  Ib.append(T)
print(Ib)
print()
H1=0
H2=0
numr1=random.randint(0,29)
numr2=random.randint(0,29)
H1=Ib[numr1]
H2=Ib[numr2]
print('Padres tomados aleatoriamente : ',H1,H2)
print()
#paso 4 cruza

s1=H1[3:]+H2[:3]
s2=H1[:3]+H2[3:]
print('Hijos combinados : ',s1,s2)

#paso 5 mutacion
ms1=0
ms2=0
probmuta=0.3
prob=random.random()
if probmuta<prob:
    index=random.randint(0,3)
    tempo =list(s1)
    if tempo[index] == '0':
        tempo[index] = '1'
    else:
        tempo[index] = '0'
    ms1 = "".join(tempo)
else:
    ms1=s1

if probmuta<prob:
    index=random.randint(0,3)
    tempo=list(s2)
    if tempo[index] == '0':
        tempo[index] = '1'
    else:
        tempo[index] = '0'
    ms2 = "".join(tempo)
else:
    ms2=s2
print('Hijos mutados  : ',ms1,ms2)