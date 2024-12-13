from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('Model\spam_classifier.joblib')
vectorizer = joblib.load('Model\cv.joblib')

@app.route('/predict', methods=['POST'])
def predict_spam():
    data = request.json
    message = data.get('message', '')

    transformed_message = vectorizer.transform([message])

    prediction = model.predict(transformed_message)
    return jsonify({
        'message': message,
        'is_spam': bool(prediction[0]),
        'spam_probability': float(model.predict_proba(transformed_message)[0][1])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)