import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

# Загрузка данных
data = pd.read_csv("data.csv")

# Преобразуем диагноз в числовой формат (0 - B, 1 - M)
data['diagnosis'] = data['diagnosis'].map({'B': 0, 'M': 1})

# Удалим нечисловые колонки, такие как 'id', если они есть
if 'id' in data.columns:
    data = data.drop(columns=['id'])

# Удаляем пустой столбец, если он есть
if 'Unnamed: 32' in data.columns:
    data = data.drop(columns=['Unnamed: 32'])

# Заполнение пропущенных значений средним значением
imputer = SimpleImputer(strategy='mean')
data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])

# Проверка на пустые строки после предобработки
if data.empty:
    raise ValueError("Датасет пуст после предобработки!")

# Проверка на NaN после обработки
print("Пропущенные значения после предобработки:")
print(data.isna().sum())

# Основные статистики
print(data.describe())

# Визуализация распределения признаков
plt.figure(figsize=(12, 6))
for column in data.columns[1:-1]:
    if data[column].nunique() > 1: # Проверяем, что есть несколько уникальных значений
        sns.histplot(data, x=column, hue='diagnosis', element='step', kde=True)
        plt.title(f'Распределение of {column}')
        plt.show()

# Матрица корреляции
plt.figure(figsize=(12, 8))
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Матрица корреляции')
plt.show()

# Поиск сильно скоррелированных признаков
high_corr_features = [column for column in corr_matrix.columns if any(corr_matrix[column] > 0.85) and column != 'diagnosis']
if high_corr_features:
    print("Сильно коррелированные признаки:", high_corr_features)
    sns.pairplot(data, vars=high_corr_features, hue='diagnosis')
    plt.show()
else:
    print("Сильно коррелированные признаки не найдены.")

# Разделение на train/test
X = data.drop(columns=['diagnosis'])
y = data['diagnosis']

if X.empty or y.empty:
    raise ValueError("Признаки или целевая переменная пусты!")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Проверка на нулевую дисперсию
zero_variance_features = [col for col in X_train.columns if X_train[col].nunique() == 1]
if zero_variance_features:
    print("Предупреждение: Обнаружены признаки с нулевой дисперсией:", zero_variance_features)
    X_train = X_train.drop(columns=zero_variance_features)
    X_test = X_test.drop(columns=zero_variance_features)

# Стандартизация
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Проверка на NaN после стандартизации
if np.isnan(X_train_scaled).sum() > 0 or np.isnan(X_test_scaled).sum() > 0:
    print("Ошибка: После стандартизации обнаружены NaN! Перемещено с 0.")
    X_train_scaled = np.nan_to_num(X_train_scaled)
    X_test_scaled = np.nan_to_num(X_test_scaled)

# Модель kNN
knn = KNeighborsClassifier()
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

# Метрики kNN
print("Метрики kNN:")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Precision:", precision_score(y_test, y_pred_knn))
print("Recall:", recall_score(y_test, y_pred_knn))
print("F1 Score:", f1_score(y_test, y_pred_knn))

# ROC-кривая kNN
fpr, tpr, _ = roc_curve(y_test, knn.predict_proba(X_test_scaled)[:, 1])
plt.plot(fpr, tpr, label=f'KNN (AUC = {auc(fpr, tpr):.2f})')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Подбор числа соседей
k_range = range(1, 21)
k_scores = [cross_val_score(KNeighborsClassifier(n_neighbors=k), X_train_scaled, y_train, cv=5, scoring='accuracy').mean() for k in k_range]
plt.plot(k_range, k_scores, marker='o')
plt.xlabel('Количество соседей K')
plt.ylabel('Кросс-валидационная точность')
plt.title('Подбор гиперпараметров kNN')
plt.show()

# Логистическая регрессия
logreg = LogisticRegressionCV(cv=5, max_iter=1000)
logreg.fit(X_train_scaled, y_train)
y_pred_logreg = logreg.predict(X_test_scaled)

# Метрики логистической регрессии
print("Метрики логистической регрессии:")
print("Accuracy:", accuracy_score(y_test, y_pred_logreg))
print("Precision:", precision_score(y_test, y_pred_logreg))
print("Recall:", recall_score(y_test, y_pred_logreg))
print("F1 Score:", f1_score(y_test, y_pred_logreg))

# ROC-кривая логистической регрессии
fpr, tpr, _ = roc_curve(y_test, logreg.predict_proba(X_test_scaled)[:, 1])
plt.plot(fpr, tpr, label=f'LogReg (AUC = {auc(fpr, tpr):.2f})')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Вывод: какая модель лучше
if accuracy_score(y_test, y_pred_logreg) > accuracy_score(y_test, y_pred_knn):
    print("Логистическая регрессия показала лучший результат.")
else:
    print("Метод kNN показал лучший результат.")
