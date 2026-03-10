import pandas as pd
import numpy as np

# NATIONALITY
# 1. Carregar dades
csv_path = 'C:\\Users\\LRAJAG\\Desktop\\Data_sintetica\\csv\\1_Sociodemographic\\MOCK_DATA_mod.csv' 
df = pd.read_csv(csv_path)

# 2. Definir valors i probabilitats reals (Cohort PADRIS-PRESTO)
# Nationality: Espanyola (83.8%), Estrangera (16.2%) 
options_n = ['Spanish', 'Non-spanish']
weights_n = [0.775, 0.225]

# 3. Omplir la columna amb la distribució real
df['nationality'] = np.random.choice(options_n, size=len(df), p=weights_n)

# 4. Aplicar el "buit" per deixar només el 95.95% de cobertura 
num_buits_n = int(len(df) * 0.0005)
indexs_buits_n = np.random.choice(df.index, size=num_buits_n, replace=False)
df.loc[indexs_buits_n, 'nationality'] = np.nan

# AGE

# 2. Definir els rangs d'edat i les probabilitats (Cohort PADRIS-PRESTO)
rangs_age = ['0-14', '15-19', '20-34', '35-64', '>65']
weights_age = [0.095, 0.119, 0.161, 0.458, 0.167]

# 3. Omplir la columna 'age' amb la distribució real
df['age'] = np.random.choice(rangs_age, size=len(df), p=weights_age)

# 4. Aplicar el buidatge (si vols mantenir la coherència del 85% de cobertura)
# Tot i que l'edat sol tenir una cobertura alta (98-100%), apliquem un soroll del 5% per realisme [cite: 238]
num_buits_age = int(len(df) * 0.05)
indexs_buits_age = np.random.choice(df.index, size=num_buits_age, replace=False)
df.loc[indexs_buits_age, 'age'] = np.nan

# 5. Guardar el fitxer
output_path = 'C:/Users/LRAJAG/Desktop/Data_sintetica/csv/1_Sociodemographic/MOCK_DATA_N_age_mod.csv'
df.to_csv(output_path, index=False)

print("Fet! Columnes 'Nationality' i 'age' modificades amb els rangs realistes:")