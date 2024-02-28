# A grocery store wants to know its customers better in order to create personalized marketing
# campaigns. You are asked to develop a classification model using Keras that takes into account
# customers' shopping frequency, their spending habits and the maximum amount they spend in the
# store. The goal of the model is to classify customers into three categories: low, medium and high
# value.

from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from metrics_calculations import calculate_total_tran_amount, calculate_frequency, calculate_average_spending
import joblib
import numpy as np


data = pd.read_excel('data_customer_classification.xlsx', engine='openpyxl')

data['trans_date'] = pd.to_datetime(data['trans_date'])

frequency = calculate_frequency(data)
data = data.merge(frequency.rename('frequency'), on='customer_id', how='left')

# print(data[['customer_id', 'frequency']])

total_amount = calculate_total_tran_amount(data)
data = data.merge(total_amount.rename('total_amount'), on='customer_id', how='left')

# print(data[['customer_id', 'total_amount']])

data = calculate_average_spending(data)

# print(data[['customer_id', 'average_spend']])

labels = pd.qcut(data['total_amount'], q=3, labels=['low', 'medium', 'high'])
data['value_category'] = labels

scaler = StandardScaler()
features = ['frequency', 'total_amount', 'average_spend']
X = scaler.fit_transform(data[features])

encoder = LabelEncoder()
y = encoder.fit_transform(data['value_category'])

joblib.dump(scaler, 'scaler.joblib')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_test_df = pd.DataFrame(X_test)

X_test_df.to_csv('X_test.csv', index=False)

y_test_df = pd.DataFrame(y_test)

y_test_df.to_csv('y_test.csv', index=False)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

model.evaluate(X_test, y_test)

model.save('model_exercise4.h5')
