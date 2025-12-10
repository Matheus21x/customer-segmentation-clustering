import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'C:\Users\Matheus\Downloads\shopping_behavior_updated.csv')

colunas_analisadas = ['Age', 'Gender', 'Category', 'Purchase Amount (USD)','Review Rating', 'Previous Purchases', 'Frequency of Purchases', 'Subscription Status','Shipping Type', 'Discount Applied', ]
df_cluster = df[colunas_analisadas].copy()

frequency_map = {
    'Weekly': 52,
    'Bi-Weekly': 26,
    'Fortnightly': 26,
    'Monthly': 12,
    'Every 3 Months': 4,
    'Quarterly': 4,
    'Annually': 1
}
df_cluster['Frequency of Purchases'] = df_cluster['Frequency of Purchases'].map(frequency_map)

colunas_texto = ['Gender', 'Category', 'Subscription Status', 'Discount Applied', 'Shipping Type']
le = LabelEncoder()
for coluna in colunas_texto:
    df_cluster[coluna] = le.fit_transform(df_cluster[coluna])

print(df_cluster.info())