import numpy as np
import pandas as pd
df = pd.read_csv("Housing.csv")
X = df[["area", "bedrooms", "bathrooms"]].to_numpy()
Y = df.price.to_numpy()

def h(W, X):
    """
    Calculate the hypothesis for linear regression.

    Parameters:
    W (numpy.ndarray): Weight vector (dimension: (n+1,)).
    X (numpy.ndarray): Feature matrix (dimension: (m, n+1)).

    Returns:
    hypothesis (numpy.ndarray): Hypothesis values (dimension: (m,)).
    """
    hypothesis = X @ W
    return hypothesis

def normalize_features(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    
    # Проверяем, что стандартное отклонение не равно нулю
    std[std == 0] = 1
    
    normalized_X = (X - mean) / std
    return normalized_X, mean, std

def nabla_J(W, X, Y):
    """
    Computes the gradient of the loss function for linear regression.

    Parameters:
    W (numpy.ndarray): Vector of weights (dimensionality (n+1,)).
    X (numpy.ndarray): Feature matrix (dimensionality (m, n+1)).
    Y (numpy.ndarray): Target value vector (dimensionality (m,)).

    Returns:
    Gradient (numpy.ndarray): The gradient of the loss function (dimension (n+1,)).
    """
    
    m = len(Y)  # Кількість навчальних прикладів
    error  = X.T @ (h(W, X) - Y)
    gradient = (1 / m) * error
    return gradient


def gradient_descent(X, Y, learning_rate=0.001, num_iterations=1_00_000):
    
    n = X.shape[1]  # Кількість ознак (у цьому випадку 3: area, bedrooms, bathrooms)
    
    # Ініціалізуємо вагові коефіцієнти випадковими значеннями
    W = np.random.randn(n)
    
    for _ in range(num_iterations):       
        # Обновляем веса
        W -= learning_rate * nabla_J(W, X, Y)
        
    return W


# Нормализуем признаки
X, mean, std = normalize_features(X)

# Добавляем столбец с единицами для свободного члена (bias)
X = np.column_stack([np.ones(len(X)), X])

# Вызываем функцию градиентного спуска
learned_weights = gradient_descent(X, Y)

# Восстанавливаем ненормализованные веса
intercept = learned_weights[0]
coefficients = learned_weights[1:] / std

print("Весовые коэффициенты после градиентного спуска:")
print(f"Свободный член (intercept): {intercept}")
print(f"Коэффициенты признаков (area, bedrooms, bathrooms): {coefficients}")
