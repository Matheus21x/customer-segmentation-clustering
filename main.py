import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Matheus\Downloads\shopping_behavior_updated.csv')

colunas_analisadas = ['Age', 'Gender', 'Category', 'Purchase Amount (USD)','Review Rating', 'Previous Purchases', 'Frequency of Purchases', 'Subscription Status','Shipping Type', 'Discount Applied', ]
df_cluster = df[colunas_analisadas].copy()

#transformar tudo em anos
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

scaler = StandardScaler()
dados_escalados = scaler.fit_transform(df_cluster)
df_escalado = pd.DataFrame(dados_escalados, columns=df_cluster.columns)

#analisar quantos clusters eram necessesarios 
errorK = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(df_escalado)
    errorK.append(kmeans.inertia_)
#plt.plot(range(1, 10), errorK)
#plt.show() 5 clusters foi a melhor opçao

kmeans_final = KMeans(n_clusters=5, random_state=0, n_init="auto").fit_predict(df_escalado)
df['Cluster'] = kmeans_final
df_cluster['Cluster'] = kmeans_final

#print(df['Cluster'].value_counts())
#print(df.groupby('Cluster')[['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']].mean())
print(df_cluster.groupby('Cluster')[['Subscription Status', 'Discount Applied', 'Frequency of Purchases', 'Gender']].mean())