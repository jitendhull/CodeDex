# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample movie reviews and their corresponding labels
reviews = [
    "This movie was fantastic! Amazing, iconic",
    "I loved it!", "Amazing story line and great acting!",
    "The plot was cringe.",
    "Loved the acting! Highly recommended."
]

labels = ["positive", "positive", "positive", "negative", "positive"]

# Convert the text data into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a Multinomial Naive Bayes model
model = MultinomialNB()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print("Accuracy:", accuracy)

# Determine if the vibes are good based on the accuracy
if accuracy > 0.5:
  print("The vibes are great, book the tickets!")
else:
  print("The vibes are iffy")