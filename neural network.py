#pip install keras
#pip install -U scikit-learn
#pip install tensorflow

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generar un conjunto de datos de clasificación binaria
X, Y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=7)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=7)

# Crear el modelo de la red neuronal
modelo = Sequential()
modelo.add(Dense(32, input_dim=20, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, Y_train, epochs=100, batch_size=10)

# Evaluar el rendimiento del modelo en los datos de prueba
puntuaciones = modelo.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (modelo.metrics_names[1], puntuaciones[1]*100))
