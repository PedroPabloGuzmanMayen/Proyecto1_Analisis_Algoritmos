import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos
df = pd.read_csv('resultados.csv')


x = df['Numero'].values.reshape(-1, 1)
y = df['Tiempo'].values
errors = []  # Se usuará para guardar el error de cada modelo
best_degree = None
best_mse = float('inf')

plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xlabel("Número en la secuencia Fibonacci")
plt.ylabel("Tiempo de ejecución")
plt.title("Tamaño de la entrada vs Tiempo de ejecución")
plt.scatter(df['Numero'], df['Tiempo'], color='black', alpha=0.6, edgecolors='black', label="Resultados obtenidos")
plt.savefig('dispersión.png', dpi=300)

for degree in range(1,11): #Evaluar polinomios de grado 1 a 10
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(x)
    #Entrenar el modelo
    model = LinearRegression()
    model.fit(X_poly, y)
    # Generar predicciones
    y_pred = model.predict(X_poly)
    
    #Calcular mse y r2
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    errors.append((degree, mse, r2))
    
    # Tener registro del mejor MSE y mejor r2
    if mse < best_mse:
        best_mse = mse
        best_degree = degree
    
    # Graficar la curva polinomial de regresión
    plt.plot(df['Numero'], y_pred, label=f"Grado polinomial {degree}")

# Graficar 
plt.scatter(df['Numero'], df['Tiempo'], color='black', alpha=0.6, edgecolors='black', label="Resultados obtenidos")


plt.xlabel("Número en la secuencia Fibonacci")
plt.ylabel("Tiempo de ejecución")
plt.title("Tamaño de la entrada vs Tiempo de ejecución")
plt.legend()
plt.grid(True)

plt.savefig('regresion.png', dpi=300)

print("Degree | MSE       | R² Score")
print("-----------------------------")
for degree, mse, r2 in errors:
    print(f"{degree:^6} | {mse:.4f} | {r2:.4f}")

print(f"\nMejor grado del polinomio: {best_degree} (MSE: {best_mse:.4f})")



results_df = pd.DataFrame(errors, columns=["Degree", "MSE", "R2_Score"])
results_df.to_csv("regression_results.csv", index=False)