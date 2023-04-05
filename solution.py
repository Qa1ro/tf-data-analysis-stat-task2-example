import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)  # размер выборки
    data_min = np.min(x)  # минимальное значение в выборке
    data_max = np.max(x)  # максимальное значение в выборке
    
    # коэффициент для построения доверительного интервала
    coefficient = (n + 1) / (n * (1 - p))
    
    # левая граница доверительного интервала
    left_boundary = data_min

    # правая граница доверительного интервала
    right_boundary = data_max * coefficient

    return (left_boundary, right_boundary)
