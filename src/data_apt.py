import pandas as pd
import numpy as np

# Configuración
n = 1000
atc_list = ['N03', 'N05', 'N06']
#N03 (Antiepileptics)', 'N05 (Psycholeptics)', 'N06 (Psychoanaleptics)

# Generación de datos estadísticos
primary_care = np.clip(np.random.normal(6.3, 8.57, n), 0, 1227).astype(int)
days_spent = np.clip(np.random.exponential(0.75, n), 0, 366).astype(int)
atc_choices = np.random.choice(atc_list, n)
# Intensidad: 124.91 media ± 137.68 SD
counts = np.clip(np.random.normal(124.91, 137.68, n), 1, 1309).astype(int)

# Crear el CSV
df = pd.DataFrame({
    'id': range(1, n + 1),
    'primary_care_visits': primary_care,
    'days_spent': days_spent,
    'prescriptions_atc': atc_choices,
    'prescriptions_count': counts
})

df.to_csv('VISITS_ATC.csv', index=False)
print("Archivo 'VISITS_ATC.csv' generado correctamente.")