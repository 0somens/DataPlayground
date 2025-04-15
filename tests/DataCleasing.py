# «age»: edad (numérica)
# «job»: tipo de trabajo (categórica: «admin.», «unknown», «unemployed», «management», «housemaid», «entrepreneur», «student», «blue-collar»,»self-employed», «retired», «technician», «services»)
# «marital»: estado civil (categórica: «married», «divorced», «single»)
# «education»: nivel educativo (categórica: «unknown», «secondary», «primary», «tertiary»)
# «default»: si dejó de pagar sus obligaciones (categórica: «yes», «no»)
# «balance»: saldo promedio anual en euros (numérica)
# «housing»: ¿tiene o no crédito hipotecario? (categórica: «yes», «no»)
# «loan»: ¿tiene créditos de consumo? (categórica: «yes», «no»)
# «contact»: medio a través del cual fue contactado (categórica: «unknown», «telephone», «cellular»)
# «day»: último día del mes en el que fue contactada (numérica)
# «month»: último mes en el que fue contactada (categórica: «jan», «feb», «mar», …, «nov», «dec»)
# «duration»: duración (en segundos) del último contacto (numérica)
# «campaign»: número total de veces que fue contactada durante la campaña (numérica)
# «pdays»: número de días transcurridos después de haber sido contactado antes de la campaña actual (numérica. -1 indica que no fue contactado previamente)
# «previous»: número de veces que ha sido contactada antes de esta campaña (numérica)
# «poutcome»: resultado de la campaña de marketing anterior (categórica: «unknown», «other», «failure», «success»)
# «y»: categoría ¿el cliente se suscribió a un depósito a término? (categórica: «yes», «no»)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("dataset_banco.csv")
# print(data.head()) 
print(data.shape) # (45215, 17)

data.dropna(inplace=True) #elimina datos faltantes (se usa cuando tenemos una cantidad suficiente de datos (como aqui) tambine podriamos interpolarlos con datos vecinos o usar ML)
data.info() 


#columnas categóricas
cols_cat = ['job','marital','education','default','housing',
           'loan','contact','month','poutcome','y']
#for col in cols_cat:
#   print(f'Columna {col}: {data[col].nunique()} subniveles') #Conteo de la cantidad de diferentes valores
#Si alguna de estas columnas posee solo 1 subnivel, entonces es irrelevante

# print(data.describe()) #Busca solo las columnas numéricas
# Si la desviación estadar (std) es igual a 0 significa que todos los valores de esa tabla son iguales
#Por lo tanto son irrelevantes /en este caso no hay ninguna

#Filas repetidas ?
print(f'Dataset tamaño antes de las filas repetidas: {data.shape}' )
data.drop_duplicates(inplace=True)
print(f'Dataset tamaño Despues de eliminar las filas repetidas: {data.shape}' )

# Checkar outliers
# Gráficas individuales pues las variables numéricas están en rangos diferentes
cols_num= ['age','balance','day','duration','campaign','pdays','previous']

fig,ax= plt.subplots(nrows= 7, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)


for i,col in enumerate(cols_num):
    sns.boxplot(x=col,data=data,ax=ax[i])
    ax[i].set_title(col)

# resultados
# hay sujetos con edades > 100 años
# hay valores negativos en 'duration'
# hay valores extremadamentes altos en 'previous' (cercano a 200)



print(f'edades: {data.shape}' )
data = data[data['age']<=100] 
print(f'Dataset con edades < 100: {data.shape}' )

print(f'Dataset registros de duración: {data.shape}' )
data = data[data['duration']>0] 
print(f'Dataset Dataset registros de duración de llamadas > 0: {data.shape}' )

print(f'Dataset registros previous: {data.shape}' )
data = data[data['previous']<=100] 
print(f'Dataset con previous < 100: {data.shape}' )

# Errores tipográficos en variables categóricas


# Graficar los subniveles de las variables categoricas
# Ya tengo definido cols_cat arriba

# Grafico de barras
fig,ax = plt.subplots(nrows=10,ncols=1,figsize=(10,30))
fig.subplots_adjust(hspace=1)

def enumerate_cat():
    for i,col in enumerate(cols_cat):
        sns.countplot(x=col,data=data, ax=ax[i])
        ax[i].set_title(col)
        ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30) 
        # Warning return
#     UserWarning: set_ticklabels() should only be used with a fixed number of ticks, i.e. after set_ticks() or using a FixedLocator. 
#   ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)

# Hay diferencias tipográficas
# management vs Management vs MANAGEMENT
# todo en minusculas
for column in data.columns:
    if column in cols_cat:
        data[column] = data[column].str.lower()
        
# abreviaturas
# unificar admin y administrative
print(data['job'].unique())
data['job'] = data['job'].str.replace('admin.','administrative',regex=False) #regex es para expresiones regulares
print(data['job'].unique())


# marital: unificar div. y divorced

print(data['marital'].unique())
data['marital'] = data['marital'].str.replace('div.','divorce',regex=False) #regex es para expresiones regulares
print(data['marital'].unique())


#education unificar sec. secondary, unk y unknown
print(data['education'].unique())
data['education'] = data['education'].str.replace('sec.','secondary',regex=False) 
data[data['education']] == 'unk' = 'unknown'  
print(data['education'].unique())

#contact: Unificar telehpone y phone
print(data['contact'].unique())
data[data['contact'] == 'phone'] = 'telephone'  
print(data['contact'].unique())

#poutcome: unificar unk y unknown
print(data['poutcome'].unique())
data[data['poutcome'] == 'unk'] = 'unknown'  
print(data['poutcome'].unique())

enumerate_cat()


data.shape
# Ya seguiriamos con el análisis exlpiratorio



    