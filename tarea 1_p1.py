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
PREGUNTA 1: {all, female, male} x {mejores, peores}---------------------------
"""
#MEJORES 10 NOTAS DE TODOS LOS ESTUDIANTES------------------------------------
top=data.sort_values(by='total', ascending=False) #ordenar datos descendiente por el total
r, w, m=[], [], []
for i in top['math']:
    m.append(i)
m=m[:10] #da los primeros 10 elementos del top 10 en math
for i in top['reading']:
    r.append(i)
r=r[:10] #da los primeros 10 elementos del top 10 en reading
for i in top['writing']:
    w.append(i)
w=w[:10] #da los primeros 10 elementos del top 10 en writing
label=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,m, wide, label='math', color='gold')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,r, wide, label='reading', color='mediumturquoise')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,w, wide, label='writing', color='chocolate')#coordenadas, valores, ancho
ax.set_title('Top estudiantes con mejor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()

#TOP PEORES 10----------------------------------------------------------------
bottom=data.sort_values(by='total')
re, wr, ma=[], [], []
for i in bottom['math']:
    ma.append(i)
ma=ma[:10] #da los primeros 10 elementos del top 10 en math
for i in bottom['reading']:
    re.append(i)
re=re[:10] #da los primeros 10 elementos del top 10 en reading
for i in bottom['writing']:
    wr.append(i)
wr=wr[:10] #da los primeros 10 elementos del top 10 en writing
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,ma, wide, label='math', color='darkseagreen')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,re, wide, label='reading', color='peru')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,wr, wide, label='writing', color='rosybrown')#coordenadas, valores, ancho
ax.set_title('Top estudiantes con peor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()
print('Gráfico 2:\n-ojo: la estudiante 1, tuvo en matematica un 0')

#POR GENERO--------------------------------------------------------------------
female=data[data['gender']=='female']
male=data[data['gender']=='male']

#MEJORES NOTAS-----------------------------------------------------------------
topf= female.sort_values(by='total', ascending=False) #top female
topm= male.sort_values(by='total', ascending=False) #top male

rf,wf,mf =[],[],[] #reading female, writing female, math female
rm,wm,mm =[],[],[] #reading male, writing male, math male

for i in topf['math']:
    mf.append(i)
mf=mf[:10] #da los primeros 10 elementos del top 10 en math
for i in topf['reading']:
    rf.append(i)
rf=rf[:10] #da los primeros 10 elementos del top 10 en reading
for i in topf['writing']:
    wf.append(i)
wf=wf[:10] #da los primeros 10 elementos del top 10 en writing
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,mf, wide, label='math', color='plum')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,rf, wide, label='reading', color='turquoise')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,wf, wide, label='writing', color='pink')#coordenadas, valores, ancho
ax.set_title('Top mujeres con mejor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()

for i in topm['math']:
    mm.append(i)
mm=mm[:10] #da los primeros 10 elementos del top 10 en math
for i in topm['reading']:
    rm.append(i)
rm=rm[:10] #da los primeros 10 elementos del top 10 en reading
for i in topm['writing']:
    wm.append(i)
wm=wm[:10] #da los primeros 10 elementos del top 10 en writing
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,mm, wide, label='math', color='darkslateblue')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,rm, wide, label='reading', color='lightseagreen')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,mm, wide, label='writing', color='khaki')#coordenadas, valores, ancho
ax.set_title('Top hombres con mejor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()
#PEORES NOTAS-----------------------------------------------------------------
bottomf= female.sort_values(by='total') #bottom female
bottomm= male.sort_values(by='total') #bottom male

rfb,wfb,mfb =[],[],[] #reading female, writing female, math female BOTTOM
rmb,wmb,mmb =[],[],[] #reading male, writing male, math male BOTTOM

for i in bottomf['math']:
    mfb.append(i)
mfb=mfb[:10] #da los primeros 10 elementos del top 10 en math
for i in bottomf['reading']:
    rfb.append(i)
rfb=rfb[:10] #da los primeros 10 elementos del top 10 en reading
for i in bottomf['writing']:
    wfb.append(i)
wfb=wfb[:10] #da los primeros 10 elementos del top 10 en writing
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,mfb, wide, label='math', color='plum')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,rfb, wide, label='reading', color='turquoise')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,wfb, wide, label='writing', color='pink')#coordenadas, valores, ancho
ax.set_title('Top mujeres con peor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()

for i in bottomm['math']:
    mmb.append(i)
mmb=mmb[:10] #da los primeros 10 elementos del top 10 en math
for i in bottomm['reading']:
    rmb.append(i)
rmb=rmb[:10] #da los primeros 10 elementos del top 10 en reading
for i in bottomm['writing']:
    wmb.append(i)
wmb=wmb[:10] #da los primeros 10 elementos del top 10 en writing
fig, ax= plt.subplots()
wide=0.3
ax.bar(np.arange(10)-wide/2,mmb, wide, label='math', color='darkslateblue')#coordenadas, valores, ancho
ax.bar(np.arange(10)+wide/2,rmb, wide, label='reading', color='lightseagreen')#coordenadas, valores, ancho
ax.bar(np.arange(10)+2*wide/2,mmb, wide, label='writing', color='khaki')#coordenadas, valores, ancho
ax.set_title('Top hombres con peor puntaje acumulado')
ax.set_ylabel('Nota de cada asignatura')
ax.set_xticks(np.arange(10))
ax.set_xticklabels(label)
plt.legend()
