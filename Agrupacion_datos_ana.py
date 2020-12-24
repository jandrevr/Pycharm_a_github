import pandas as pd

#http://snirh.ana.gob.pe/visorS2/
#    Estación:  SAN LAZARO DE ESCOMARCA
#    Código:	156102
#    Latitud:	-12.183333
#    Longitud:	-76.35
#    Tipo 1:	CONVENCIONAL
#    Tipo 2:	CLIMÁTICA
name = 'Datos_ANA_San_Lazaro.xlsx'
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
df = pd.read_excel(name, skiprows=[0])
#print(df)
df.set_index('FECHA', inplace=True)
#print(df)
estaciones = df.columns
#print(estaciones)
serie = df['VALOR']
data = pd.DataFrame(serie)
#print(data)
df_m = data.resample('M').max()
#.resample()  groupby basado en el tiempo, seguido de un método de reducción en cada uno de sus grupos.
#print(df_m)
df_m['year'] = df_m.index.year
#(df_m['year'])
df_m['month'] = df_m.index.month
#print(df_m['month'])
#print(df_m)
df_g = df_m.pivot(index='year', columns='month', values='VALOR')
#print(df_g)

#https://www.analyticslane.com/2019/05/06/como-cambiar-el-nombre-de-las-columnas-en-pandas/
df_g.columns = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']
#print(df_g)

xls = pd.ExcelWriter('Datos_agrupados_San_Lazaro_max.xlsx')
df_g.to_excel(xls, sheet_name='Pacum_San_Lazaro_max')

xls.save()

df_g['ANUAL'] = df_g[['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']].max(axis=1)
print(df_g)

#Ene = df_g['Ene'].sum()
#print(Ene)

#https://www.delftstack.com/es/howto/python-pandas/how-to-get-the-sum-of-pandas-column/
#https://es.stackoverflow.com/questions/191740/desviaci%C3%B3n-estandar-en-python-con-pandas#:~:text=Hay%20dos%20m%C3%A9todos%20que%20permiten,el%20otro%20a%20Series%20(%20pandas.&text=axis%20%3A%20debe%20ser%20un%20entero,por%20cada%20fila%20(index).
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.std.html
Media = df_g.mean()
#print(Media)
Desvest = df_g.std()
#print(Desvest)
Varianza = df_g.var()
#print(Varianza)
Total = df_g.sum()
#print(Total)

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
#https://living-sun.com/es/python-3x/683879-how-to-sum-columns-in-pandas-and-add-the-result-into-a-new-row-python-3x-pandas-sum-append-row.html
#https://stackoverflow.com/questions/39621239/how-to-sum-columns-in-pandas-and-add-the-result-into-a-new-row/39621278#comment66548153_39621239
df_F = df_g.append(Media, ignore_index=True)
df_F = df_F.append(Desvest, ignore_index=True)
df_F = df_F.append(Varianza, ignore_index=True)
df_F = df_F.append(Total, ignore_index=True)
# ignore_index=True, Si es True, el eje resultante se etiquetará como 0, 1,..., n-1
# y no con los nombres de las columnas: 'Ene', 'Feb', ..., 'Dic'
print(df_F)