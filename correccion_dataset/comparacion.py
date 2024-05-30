import pandas as pd

urls = pd.read_csv('correccion_dataset/malicious_phish.csv')
urls_updated = pd.read_csv('correccion_dataset/malicious_phish_updated.csv')

# Unir los dos dataframes en base a la columna 'url'
merged_df = pd.merge(urls, urls_updated, on='url', how='outer', suffixes=('_urls', '_urls_updated'), indicator=True)

# Filtrar las filas donde las columnas 'type' son diferentes o donde existe en uno pero no en el otro
diff_df = merged_df[(merged_df['type_urls'] != merged_df['type_urls_updated']) | (merged_df['_merge'] != 'both')]

# Mostrar las filas diferentes
diff_df.to_csv('comparacion.csv', index=False)