import joblib

model = joblib.load('spam_classifier.joblib')
vectorizer = joblib.load('cv.joblib')

def predict_spam(message):
    transformed_message = vectorizer.transform([message])

    prediciton = model.predict(transformed_message)

    return "Spam" if prediciton[0] == 1 else "Ham"

test_message1 = "Congratulations! You have won a free ticket to the Bahamas. Text 'WIN' to 12345 to claim your prize."
test_message2 = "Hello, Thanks for the invitation. However given some prior commitments, I will not be able to attend the program."
print(predict_spam(test_message1))
print(predict_spam(test_message2))