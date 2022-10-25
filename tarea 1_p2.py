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
PREGUNTA 2: Percentiles por grupos---------------------------------------------
"""
#horizontal
fig, ax = plt.subplots()
for i in data.columns[-4:-1]:
    sns.boxplot(x=data[i], y=data['ethnicity'])
    plt.title('Percentiles')
    plt.show()
