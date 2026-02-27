import pandas as pd
import numpy as np

# 1. Cargar el archivo
df = pd.read_csv('MOCK_DATA.csv')

# 3. Añadir Outliers (Valores fuera de rango) manuales
# Cambiamos la edad de los registros 12 al 19 a valores absurdos
df.loc[12:19, 'age'] = 999 

# 4. Guardar el archivo "sucio"
df.to_csv('MOCK_DATA_mod.csv', index=False)