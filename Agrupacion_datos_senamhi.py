import pandas as pd

#https://www.senamhi.gob.pe/?&p=descarga-datos-hidrometeorologicos
name = 'Datos_senamhi_ayacucho_pauza.xlsx'
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
#df = pd.read_excel(name, 'Hoja1', index_col=0)
df = pd.read_excel(name)  # La primera columna no es el indice
print(df)
# El formato es:
#        AÑO  MES  DIA  Pacum  Tmax  Tmin
#0      1963   12    9    0.0   NaN   NaN
#1      1963   12   10    0.0  24.0   8.2

#Combinar las columnas año, mes y día para crear el indice de fechas
#https://es.stackoverflow.com/questions/233013/combinar-en-una-sola-columna-los-datos-de-varias-columnas-de-un-dataframe
df['FECHA'] = pd.to_datetime(dict(year=df['AÑO'],
                                  month=df['MES'],
                                  day=df['DIA']))
print(df)
#        AÑO  MES  DIA  Pacum  Tmax  Tmin      FECHA
#0      1963   12    9    0.0   NaN   NaN 1963-12-09
#1      1963   12   10    0.0  24.0   8.2 1963-12-10

#Cómo convertir el índice de un Dataframe de Pandas en una columna
#https://www.delftstack.com/es/howto/python-pandas/how-to-convert-index-of-a-pandas-dataframe-into-a-column/
df.set_index('FECHA', inplace=True)  # Cambiar columna indice de filas
print(df)
#             AÑO  MES  DIA  Pacum  Tmax  Tmin
#FECHA
#1963-12-09  1963   12    9    0.0   NaN   NaN
#1963-12-10  1963   12   10    0.0  24.0   8.2

estaciones = df.columns
print(estaciones)
#Index(['AÑO', 'MES', 'DIA', 'Pacum', 'Tmax', 'Tmin'], dtype='object')

serie = df['Pacum']
print(serie)
#FECHA
#1963-12-09    0.0
#1963-12-10    0.0
data = pd.DataFrame(serie)
print(data)
#            Pacum
#FECHA
#1963-12-09    0.0
#1963-12-10    0.0

#Remuestrear o convertir una serie de tiempo a una frecuencia particular
#https://www.analyticslane.com/2018/07/06/agrupacion-de-datos-por-fecha-en-pandas/
#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
df_m = data.resample('M').sum()
#.resample()  groupby basado en el tiempo, seguido de un método de reducción en cada uno de sus grupos.
print(df_m)
#            Pacum
#FECHA
#1963-12-31    0.6
#1964-01-31    2.7


df_m['year'] = df_m.index.year
print(df_m['year'])
#FECHA
#1963-12-31    1963
#1964-01-31    1964
df_m['month'] = df_m.index.month
print(df_m['month'])
#FECHA
#1963-12-31    12
#1964-01-31     1
df_m['day'] = df_m.index.day
print(df_m['day'])
#FECHA
#1963-12-31    31
#1964-01-31    31

print(df_m)
#            Pacum  year  month  day
#FECHA
#1963-12-31    0.6  1963     12   31
#1964-01-31    2.7  1964      1   31


df_g = df_m.pivot(index='year', columns='month', values='Pacum')
print(df_g)
#month      1       2       3      4      5   ...     8      9      10    11      12
#year                                         ...
#1963      NaN     NaN     NaN    NaN    NaN  ...    NaN    NaN    NaN   NaN    0.60
#1964     2.70   44.60   44.50  16.10   6.00  ...   0.00   0.00   0.00  11.3   43.20

xls = pd.ExcelWriter('Datos_agrupados_pauza_acum.xlsx')
df_g.to_excel(xls, sheet_name='Pacum_pauza_acum')

xls.save()
