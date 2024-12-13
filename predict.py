from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load('Model/spam_classifier.joblib')
vectorizer = joblib.load('Model/cv.joblib')

@app.route('/predict', methods=['POST'])
def predict_spam():
    data = request.json
    message = data.get('message', '')

    transformed_message = vectorizer.transform([message])

    prediction = model.predict(transformed_message)
    return jsonify({
        'message': message,
        'is_spam': bool(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)