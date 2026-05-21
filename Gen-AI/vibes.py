from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    "This movie was fantastic! Amazing, iconic",
    "I loved it!", "Amazing story line and great acting!",
    "The plot was cringe.",
    "Loved the acting! Highly recommended."
]

labels = ["positive", "positive", "positive", "negative", "positive"]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

X_train, X_test, y_train, y_test = train_test_split(X,labels,test_size=0.2,random_state=42)

model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

if accuracy > 0.5:
  print("The vibes are great, book the tickets!")
else:
  print("The vibes are iffy")