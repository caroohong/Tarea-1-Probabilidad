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
PREGUNTA 3: Dispersion math y verbal (lunch-test preparation)------------------
"""
data['verbal']= (data['writing']+data['reading'])/2 #crear nueva columna con promedio entre reading-writing
#fig,ax=plt.subplots(1,2, figsize=(10,10))
fig, ax= plt.subplots()
comparacion=['lunch', 'preparation']
for i in range(2):
    sns.scatterplot(data=data, x='math', y='verbal', hue=comparacion[i], alpha=0.5) #alpha es opacidad, hue distingue por colores según categoria
    plt.xlabel('Math Score')
    plt.ylabel('Verbal Score')
    plt.title('Math Score vs Verbal Score')
    plt.show()
