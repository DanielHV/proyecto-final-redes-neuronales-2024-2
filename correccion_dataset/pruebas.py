import pandas as pd

dataset = pd.read_csv('correccion_dataset/malicious_phish.csv')
label_counts = dataset['type'].value_counts()

print(label_counts)