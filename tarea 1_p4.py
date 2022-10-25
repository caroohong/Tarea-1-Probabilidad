import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
data = pd.read_csv('StudentsPerformance.csv', sep=',')#funciona si el csv esta en la misma carpeta q el python
#renombrar columnas: codigo de Ching-Chun Yeh de Students Performance in Exams
data.rename(columns={"race/ethnicity":"ethnicity","parental level of education":"parent_education",
                     "math score":"math","reading score":"reading","writing score":"writing",
                     "test preparation course":"preparation"},inplace=True)
data['total']= data['math']+data['reading']+data['writing']#crear nueva columna que indica la suma de las 3 notas
"""
PREGUNTA 4: tabla de frecuencias + histograma: math, reading, writing
"""
#datos en total:
datom=[]
dator=[]
datow=[]
for i in range(len(data['math'])):
    datom.append(data['math'].iloc[i])
for i in range(len(data['reading'])):
    dator.append(data['reading'].iloc[i])
for i in range(len(data['writing'])):
    datow.append(data['writing'].iloc[i])
datom.sort()
dator.sort()
datow.sort()

#frecuencias:
fmath= pd.value_counts(data['math']).sort_index() #frecuencia en math, sort.index lo hace de forma creciente
freading= pd.value_counts(data['reading']).sort_index() #frecuencia en reading
fwriting= pd.value_counts(data['writing']).sort_index() #frecuencia en writing

#frecuencia absoluta: o cantidad de datos
Fam=sum(fmath)#frecuencia absoluta en math = 1000
Far=sum(freading)#frecuencia absoluta en reading = 1000
Faw=sum(fwriting)#frecuencia absoluta en writing = 1000

#cantidad de frecuencias
cfmath= len(fmath) #81
cfreading= len(freading) #72
cfwriting= len(fwriting) #77

#numero de las frecuencias (index): los entrega en una lista
mfri= fmath.index
rfri= freading.index
wfri= fwriting.index
#fmath.loc[100]= 7 : para la nota 100, hay una frecuencia de 7

#valor de cada frecuencia: los entrega en una lista
mfrv, rfrv, wfrv=[],[],[]
for i in range(len(fmath)):
    mfrv.append(fmath.loc[mfri[i]])
for i in range(len(freading)):
    rfrv.append(freading.loc[rfri[i]])
for i in range(len(fwriting)):
    wfrv.append(fwriting.loc[wfri[i]])
"""TABLA FRECUENCIAS MATEMATICAS: codigo de google colaboratory Ayudantía 7"""
plt.hist(data['math'], bins=11, color='coral',ec='black')
plt.title('Histogram Math')
plt.xlabel('Scores')
plt.ylabel('Frecuency')
plt.show()
import math
q = cfmath-1
R = (mfri[-1]- mfri[0])
ni = round(1+3.32*math.log10(len(datom))) #numero de intervalos
i = round(R/ni) #77
Nr = ni*i 
Ri = Nr/i #rango del intervalo =8

int1,int2,int3,int4,int5,int6,int7,int8, int9, int10 = [],[],[],[],[],[],[],[],[],[]

for i in datom:
    if datom[0] <= i <= (datom[0] + Ri):
        int1.append(i)
    if (datom[0] + Ri) < i <= (datom[0] + 2*Ri):
        int2.append(i)
    if (datom[0] + 2*Ri) < i <=(datom[0] + 3*Ri):
        int3.append(i)
    if (datom[0] + 3*Ri) < i <= (datom[0] + 4*Ri):
        int4.append(i)
    if (datom[0] + 4*Ri) < i <= (datom[0] + 5*Ri):
        int5.append(i)
    if (datom[0] + 5*Ri) < i <= (datom[0] + 6*Ri):
        int6.append(i)
    if (datom[0] + 6*Ri) < i <= (datom[0] + 7*Ri):
        int7.append(i)
    if (datom[0] + 7*Ri) < i <= (datom[0] + 8*Ri):
        int8.append(i)
    if (datom[0] + 8*Ri) < i <= (datom[0] + 9*Ri):
        int9.append(i)
    if (datom[0] + 9*Ri) < i <= (datom[0] + 10*Ri):
        int10.append(i)
    
notas = [(datom[0], (datom[0] + Ri)),((datom[0] + Ri),(datom[0] + 2*Ri)),
         ((datom[0] + 2*Ri),(datom[0] + 3*Ri)),((datom[0] + 3*Ri),(datom[0] + 4*Ri)),
         ((datom[0] + 4*Ri),(datom[0] + 5*Ri)),((datom[0] + 5*Ri),(datom[0] + 6*Ri)), 
         ((datom[0] + 6*Ri),(datom[0] + 7*Ri)),((datom[0] + 7*Ri),(datom[0] + 8*Ri)),
         ((datom[0] + 8*Ri),(datom[0] + 9*Ri)),((datom[0] + 9*Ri),(datom[0] + 10*Ri))] 
#frecuencias
f =[len(int1),len(int2),len(int3),len(int4),len(int5),len(int6),len(int7),len(int8),len(int9), len(int10)]
#FRECUENCIA ACUMULADA
Fac=[] 
frec=0
for i in f:
    frec+=i
    Fac.append(frec)
#FRECUENCIA RELATIVA
ld= len(datom)
fr=[f[0]/ld,f[1]/ld,f[2]/ld,f[3]/ld,f[4]/ld,f[5]/ld, f[6]/ld, f[7]/ld, f[8]/ld, f[9]/ld]
#FRECUENCIA RELATIVA ACUMULADA
Fra=[]
frec=0
for i in fr:
    frec+=i
    Fra.append(frec)    
#FRECUENCIA RELATIVA PORCENTUAL
frp=[fr[0]*100,fr[1]*100,fr[2]*100,fr[3]*100,fr[4]*100,fr[5]*100,fr[6]*100, fr[7]*100, fr[8]*100, fr[9]*100]

#FRECUENCIA RELATIVA ACUMULADA PORCENTUAL
Frp=[]
frec=0
for i in frp:
    frec+=i
    Frp.append(frec)
tags={"Math Scores":notas, "f":f, "F": Fac, "fr": fr, "Fr": Fra, "frp": frp,"Frp": Frp}
tablam = pd.DataFrame(tags, columns =["Math Scores","f","F","fr","Fr","frp","Frp"])
print(f"\n{tablam}")

""""TABLA FRECUENCIAS READING: codigo de google colaboratory Ayudantía 7"""
plt.hist(data['reading'], bins=8, color='slateblue',ec='black')
plt.title('Histogram Reading')
plt.xlabel('Scores')
plt.ylabel('Frecuency')
plt.show()
q = cfreading-1
R = (rfri[-1]- rfri[0])
ni = round(math.ceil(1+3.32*math.log10(len(dator)))) #numero de intervalos=11
i = round(R/ni) #8
Nr = ni*i #88
Ri = Nr/i #rango del intervalo =11

rint1,rint2,rint3,rint4,rint5,rint6,rint7,rint8 = [],[],[],[],[],[],[],[]

for i in dator:
    if dator[0] <= i <= (dator[0] + Ri):
        rint1.append(i)
    if (dator[0] + Ri) < i <= (dator[0] + 2*Ri):
        rint2.append(i)
    if (dator[0] + 2*Ri) < i <=(dator[0] + 3*Ri):
        rint3.append(i)
    if (dator[0] + 3*Ri) < i <= (dator[0] + 4*Ri):
        rint4.append(i)
    if (dator[0] + 4*Ri) < i <= (dator[0] + 5*Ri):
        rint5.append(i)
    if (dator[0] + 5*Ri) < i <= (dator[0] + 6*Ri):
        rint6.append(i)
    if (dator[0] + 6*Ri) < i <= (dator[0] + 7*Ri):
        rint7.append(i)
    if (dator[0] + 7*Ri) < i <= (dator[0] + 8*Ri):
        rint8.append(i)
    
notas = [(dator[0], (dator[0] + Ri)),((dator[0] + Ri),(dator[0] + 2*Ri)),
         ((dator[0] + 2*Ri),(dator[0] + 3*Ri)),((dator[0] + 3*Ri),(dator[0] + 4*Ri)),
         ((dator[0] + 4*Ri),(dator[0] + 5*Ri)),((dator[0] + 5*Ri),(dator[0] + 6*Ri)), 
         ((dator[0] + 6*Ri),(dator[0] + 7*Ri)),((dator[0] + 7*Ri),(dator[0] + 8*Ri))] 
#frecuencias
f =[len(rint1),len(rint2),len(rint3),len(rint4),len(rint5),len(rint6),len(rint7),len(rint8)]
#FRECUENCIA ACUMULADA
rFac=[] 
frec=0
for i in f:
    frec+=i
    rFac.append(frec)
#FRECUENCIA RELATIVA
ld= len(dator)
rfr=[f[0]/ld,f[1]/ld,f[2]/ld,f[3]/ld,f[4]/ld,f[5]/ld, f[6]/ld, f[7]/ld]
#FRECUENCIA RELATIVA ACUMULADA
rFra=[]
frec=0
for i in rfr:
    frec+=i
    rFra.append(frec)    
#FRECUENCIA RELATIVA PORCENTUAL
rfrp=[rfr[0]*100,rfr[1]*100,rfr[2]*100,rfr[3]*100,rfr[4]*100,rfr[5]*100,rfr[6]*100, rfr[7]*100]

#FRECUENCIA RELATIVA ACUMULADA PORCENTUAL
rFrp=[]
frec=0
for i in rfrp:
    frec+=i
    rFrp.append(frec)
rtags={"Reading Scores":notas, "f":f, "F": rFac, "fr": rfr, "Fr": rFra, "frp": rfrp,"Frp": rFrp}
tablar = pd.DataFrame(rtags, columns =["Reading Scores","f","F","fr","Fr","frp","Frp"])
print(f"\n{tablar}")

"""TABLA FRECUENCIAS WRITING: codigo de google colaboratory Ayudantía 7"""
plt.hist(data['writing'], bins=11, color='turquoise',ec='black')
plt.title('Histogram Writing')
plt.xlabel('Scores')
plt.ylabel('Frecuency')
plt.show()
q = cfwriting-1 #76
R = (wfri[-1]- wfri[0]) #100-10=90
ni = round(math.ceil(1+3.32*math.log10(len(datow)))) #numero de intervalos=11
i = round(R/ni) #8
Nr = ni*i #88
Ri = Nr/i #rango del intervalo =11

wint1,wint2,wint3,wint4,wint5,wint6,wint7,wint8,wint9 = [],[],[],[],[],[],[],[],[]

for i in datow:
    if datow[0] <= i <= (datow[0] + Ri):
        wint1.append(i)
    if (datow[0] + Ri) < i <= (datow[0] + 2*Ri):
        wint2.append(i)
    if (datow[0] + 2*Ri) < i <=(datow[0] + 3*Ri):
        wint3.append(i)
    if (datow[0] + 3*Ri) < i <= (datow[0] + 4*Ri):
        wint4.append(i)
    if (datow[0] + 4*Ri) < i <= (datow[0] + 5*Ri):
        wint5.append(i)
    if (datow[0] + 5*Ri) < i <= (datow[0] + 6*Ri):
        wint6.append(i)
    if (datow[0] + 6*Ri) < i <= (datow[0] + 7*Ri):
        wint7.append(i)
    if (datow[0] + 7*Ri) < i <= (datow[0] + 8*Ri):
        wint8.append(i)
    if (datow[0] + 8*Ri) < i <= (datow[0] + 9*Ri):
        wint9.append(i)
    
notas = [(datow[0], (datow[0] + Ri)),((datow[0] + Ri),(datow[0] + 2*Ri)),
         ((datow[0] + 2*Ri),(datow[0] + 3*Ri)),((datow[0] + 3*Ri),(datow[0] + 4*Ri)),
         ((datow[0] + 4*Ri),(datow[0] + 5*Ri)),((datow[0] + 5*Ri),(datow[0] + 6*Ri)), 
         ((datow[0] + 6*Ri),(datow[0] + 7*Ri)),((datow[0] + 7*Ri),(datow[0] + 8*Ri)), 
         ((datow[0] + 8*Ri),(datow[0] + 9*Ri))] 
#frecuencias
f =[len(wint1),len(wint2),len(wint3),len(wint4),len(wint5),len(wint6),len(wint7),len(wint8),len(wint9)]
#FRECUENCIA ACUMULADA
wFac=[] 
frec=0
for i in f:
    frec+=i
    wFac.append(frec)
#FRECUENCIA RELATIVA
ld= len(datow)
wfr=[f[0]/ld, f[1]/ld, f[2]/ld, f[3]/ld, f[4]/ld, f[5]/ld, f[6]/ld, f[7]/ld, f[8]/ld]
#FRECUENCIA RELATIVA ACUMULADA
wFra=[]
frec=0
for i in wfr:
    frec+=i
    wFra.append(frec)    
#FRECUENCIA RELATIVA PORCENTUAL
wfrp=[wfr[0]*100,wfr[1]*100,wfr[2]*100,wfr[3]*100,wfr[4]*100,wfr[5]*100,wfr[6]*100, wfr[7]*100,wfr[8]*100]

#FRECUENCIA RELATIVA ACUMULADA PORCENTUAL
wFrp=[]
frec=0
for i in wfrp:
    frec+=i
    wFrp.append(frec)
wtags={"Writing Scores":notas, "f":f, "F": wFac, "fr": wfr, "Fr": wFra, "frp": wfrp,"Frp": wFrp}
tablaw = pd.DataFrame(wtags, columns =["Writing Scores","f","F","fr","Fr","frp","Frp"])
print(f"\n{tablaw}\n")

"""
PREGUNTA 5: media, moda, mediana, desv.estandar, coeficiente de variacion, sesgo, asimetria)
"""
math=tablam.describe()
reading=tablar.describe()
writing=tablaw.describe()
#math.iloc[2,:] == [numero de fila, columnas], si uno pone ':' significa todas las columnas
print('_____CALCULO DE LAS MEDIAS_____')
print(f'---MATH---\n{math.iloc[2,:]}\n')
print(f'---READING---\n{reading.iloc[2,:]}\n')
print(f'---WRITING---\n{writing.iloc[2,:]}\n')
