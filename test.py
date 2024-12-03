import joblib

model = joblib.load('spam_classifier.joblib')
vectorizer = joblib.load('cv.joblib')

def predict_spam(message):
    transformed_message = vectorizer.transform([message])

    prediciton = model.predict(transformed_message)

    return "Spam" if prediciton[0] == 1 else "Ham"

test_message = "Congratulations! You have won a free ticket to the Bahamas. Text 'WIN' to 12345 to claim your prize."

print(predict_spam(test_message))