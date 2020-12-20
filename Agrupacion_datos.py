import pandas as pd

name = 'Datos_mensuales.xlsx'
df = pd.read_excel(name, 'QL_1', index_col=0)
estaciones = df.columns
print(estaciones)

est = 23097030

serie = df[est]
print(serie)

data = pd.DataFrame(serie)
print(data)

data['year'] = df.index.year
data['month'] = df.index.month

df_g = data.pivot(index='year', columns='month', values=est)

xls = pd.ExcelWriter('Datos_agrupados.xlsx')
df_g.to_excel(xls, sheet_name='est')

xls.save()
