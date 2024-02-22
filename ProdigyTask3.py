# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the Bank Marketing dataset
bank_data = pd.read_csv('bank.csv')

# Display the first few rows of the dataset
print(bank_data.head())

# Convert categorical variables to numerical using label encoding
label_encoder = LabelEncoder()
bank_data['job'] = label_encoder.fit_transform(bank_data['job'])
bank_data['marital'] = label_encoder.fit_transform(bank_data['marital'])
bank_data['education'] = label_encoder.fit_transform(bank_data['education'])
bank_data['default'] = label_encoder.fit_transform(bank_data['default'])
bank_data['housing'] = label_encoder.fit_transform(bank_data['housing'])
bank_data['loan'] = label_encoder.fit_transform(bank_data['loan'])
bank_data['contact'] = label_encoder.fit_transform(bank_data['contact'])
bank_data['month'] = label_encoder.fit_transform(bank_data['month'])
bank_data['poutcome'] = label_encoder.fit_transform(bank_data['poutcome'])
bank_data['y'] = label_encoder.fit_transform(bank_data['y'])

# Split the dataset into features and target variable
X = bank_data.drop('y', axis=1)
y = bank_data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Generate a classification report
print(classification_report(y_test, y_pred))

plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
plt.show()
