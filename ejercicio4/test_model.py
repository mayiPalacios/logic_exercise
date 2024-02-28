from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import pandas as pd

X_test = pd.read_csv('X_test.csv')

y_test = pd.read_csv('y_test.csv')

model = load_model('model_exercise4.h5')

y_pred = model.predict(X_test)

print(y_pred)

predicted_classes = np.argmax(y_pred, axis=1)

print(predicted_classes)

y_test = y_test.values.flatten()

accuracy = accuracy_score(y_test, predicted_classes)
print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, predicted_classes))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predicted_classes))