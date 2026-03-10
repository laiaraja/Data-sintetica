import pandas as pd
import numpy as np

# 1. Cargar el archivo
df = pd.read_csv('C:\Users\LRAJAG\Desktop\Data sintetica\csv\COMORBIDITIES.csv')

#2. Definir coberturas
df.loc[df.sample(frac=0.15).index, 'Socioeconomic_levels'] = np.nan

# 4. Guardar el archivo "sucio"
df.to_csv('COMORBIDITIES_dirty.csv', index=False)