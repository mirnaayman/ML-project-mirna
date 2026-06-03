from flask import Flask, request, render_template
import joblib
import pandas as pd

print("✅ Flask is starting...")

app = Flask(__name__)

# Load model and feature list
model = joblib.load("model.pkl")
expected_features = joblib.load("features.pkl")  # ['Rating', 'Founded', 'seniority', 'state', 'avg_salary']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input
        rating = float(request.form['Rating'])
        founded = int(request.form['Founded'])
        seniority = request.form['Seniority']
        state = request.form['State']
        avg_salary = float(request.form['avg_salary'])

        # Build input DataFrame with raw categorical features
        input_df = pd.DataFrame([{
            'Rating': rating,
            'Founded': founded,
            'seniority': seniority,
            'state': state,
            'avg_salary': avg_salary
        }])

        # Ensure all expected columns exist
        input_df = input_df[expected_features]

        # Predict
        prediction = model.predict(input_df)[0]
        result = "High Salary" if prediction == 1 else "Not High Salary"

        return render_template('index.html', prediction_text=f'Prediction: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
