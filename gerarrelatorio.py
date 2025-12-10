from main import df, df_cluster
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Relatorio Loja", explorative=True)
profile.to_file("RelatorioLoja.html")