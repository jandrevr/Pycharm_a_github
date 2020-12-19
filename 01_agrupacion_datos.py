import pandas as pd

name = 'Datos_mensuales.xlsx'
df = pd.read_excel(name, 'QL_1', index_col=0)

estaciones = df.columns

xls = pd.ExcelWriter('01_Datos_agrupados_y_vs_m.xlsx')

for sta in estaciones:
    serie = df[sta]

    data = pd.DataFrame(serie)

    data['year'] = df.index.year
    data['month'] = df.index.month

    df_g = data.pivot(index='year', columns='month', values=sta)

    df_g.to_excel(xls, sheet_name=str(sta))

xls.save()
