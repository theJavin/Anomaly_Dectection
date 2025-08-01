import pandas as pd, numpy as np, xgboost as xgb, seaborn as sns, matplotlib.pyplot as plt, time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc

data = pd.read_csv('data.csv')


#remove redundant columns from read_csv
data.drop('Unnamed: 0', axis=1, inplace=True)
data.drop('session_id', axis=1, inplace=True)

#remove the extra data
data = data.groupby('type').head(50)
data.reset_index(drop=True, inplace=True)

data['delta'] = data['delta'].astype('category')

# data.drop('X', axis=1, inplace=True)
# data.drop('Y', axis=1, inplace=True)
data['X'] = data['X'].astype('category')
data['Y'] = data['Y'].astype('category')

# print(data)


#ACTUAL MACHINE LEARNING
y = data['type']
X = data.drop('type', axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = xgb.XGBClassifier(enable_categorical=True)

start_time = time.time()
model.fit(X_train, y_train)

start_time = time.time()
y_pred = model.predict(X_test)
inference_time = time.time() - start_time

print(f"inference time: {inference_time:.5f}s")

accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy: {accuracy}")

cm = confusion_matrix(y_test, y_pred)
print(cm)

sns.heatmap(cm, annot=True, fmt='d')
plt.show()

print(classification_report(y_test, y_pred))

y_pred_proba = model.predict_proba(X_test)[:, 1]

fp, tp, threshholds = roc_curve(y_test, y_pred_proba)

roc_auc = auc(fp, tp)

plt.figure(figsize=(8, 6))
plt.plot(fp, tp, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='Random guess')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()