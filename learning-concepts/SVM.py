# Maquinas de soporte vectorial  (SVM)

# Son un tipo de algoritmo de aprendizaje SUPERVISADOZ utilizado para
# la clasificación y regresión de datos
# Genera un hiperplano? optimo que separa las diferentes clades

# Su objetivo es encontrar el limite de decisión que maximiza la distancia
# entre los puntos más cercanso de las clases opuestas 
# llamados vectores de soporte
# ??


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#Cargar conjunto de datos IRIS
iris = datasets.load_iris()
X = iris.data
y = iris.target


# Dividir el conjunto de datos en entrenamiento y prueba 

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42) #Qué es random state? o para qué sirve?

#Escalar los datos
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Inicializar y entrenar el modelo SVM 
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(X_train,y_train)

#Predecir las etiquetas de clase para los datos de prueba
y_pred = svm_classifier.predict(X_test)

#Calcular la precision del modelo
accuracy = accuracy_score(y_test,y_pred)
print('Precisión del modelo SVM: ', accuracy)



