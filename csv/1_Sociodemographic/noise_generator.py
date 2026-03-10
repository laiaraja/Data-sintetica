import pandas as pd
import numpy as np

# 1. Carregar dades
csv_path = 'C:/Users/LRAJAG/Desktop/Data_sintetica/csv/MOCK_DATA.csv' 
df = pd.read_csv(csv_path)

# 2. Definir valors i probabilitats reals (Cohort PADRIS-PRESTO)
# Molt baix (15.91%), Baix (50.88%), Moderat (32.27%), Alt (0.94%) 
opcions = ['Very Low', 'Low', 'Moderate/Middle', 'High']
pesos = [0.1591, 0.5088, 0.3227, 0.0094]

# 3. Omplir la columna amb la distribució real
df['Socioeconomic_levels'] = np.random.choice(opcions, size=len(df), p=pesos)

# 4. Aplicar el "buit" per deixar només el 85% de cobertura 
num_buits = int(len(df) * 0.15)
indexs_buits = np.random.choice(df.index, size=num_buits, replace=False)
df.loc[indexs_buits, 'Socioeconomic_levels'] = np.nan

# 5. Guardar
df.to_csv('MOCK_DATA_mod.csv', index=False)
print("Fet! Columna realista i amb 85% de cobertura generada.")
