import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

try:
    model = joblib.load("final_pizza_price_model.pkl")
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Model file not found.")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded.'}), 500

    try:
        data = request.get_json()

        required_fields = ['pizza_category', 'pizza_size', 'unit_price']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400

        input_df = pd.DataFrame([data])

        input_df = input_df[required_fields]

        prediction = model.predict(input_df)

        return jsonify({
            'success': True,
            'predicted_price': round(prediction[0], 2),
            'input_data': data
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)