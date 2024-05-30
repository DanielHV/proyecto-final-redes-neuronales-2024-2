import pandas as pd

urls = pd.read_csv('correccion_dataset/malicious_phish.csv')
phishstorm = pd.read_csv('correccion_dataset/phishstorm.csv')

phishstorm = phishstorm.iloc[:, [0, -1]]
phishstorm['label'] = phishstorm['label'].replace({1.0: 'phishing', 0.0: 'benign'})
phishstorm = phishstorm.rename(columns={'domain': 'url', 'label': 'type'})

update_dict = phishstorm.set_index('url')['type'].to_dict()

urls['type'] = urls.apply(lambda row: update_dict.get(row['url'], row['type']), axis=1)

urls.to_csv('correccion_dataset/malicious_phish_updated.csv', index=False)