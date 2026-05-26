import pandas as pd
#panda es el lenguaje que te permite transformar datos


#importa csv
#df=pd.read_csv('Top5_League_Players_2017to2024_dataset.csv')

# importa csv
df = pd.read_csv(
    'Top5_League_Players_2017to2024_dataset.csv',
    sep=';'
)


print("OKEY! Archivo cargado correctamente")

#muestra las primeras filas del dataframe
print(df.head())

#filtrando por año 2022
#resultado = df[df['year'] == 2022]
#total_equipo = df['Playing Time_Starts'].count()
#print(f"total de equipos registrados son: {total_equipo}\n")

#mostrando resultado
#print(resultado)

print("--- Analisis Avanzados de datos ---")

filtro_avanzado = df['player'].str.startswith('Alex', na = False)
df_filtrado = df[filtro_avanzado]

sumo_dinero = df_filtrado['trade_value_usd_millions'].sum()
print("--- Reporte FInanciero Automatizado ---")
print(f"Monto total analizado: USD {sumo_dinero: .2f} millones.\n")

filtro_numero = df('trade_value_usd_millions') > 500