from main import df
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Relatorio Loja", explorative=True)
profile.to_file("RelatorioLojaAtt.html")