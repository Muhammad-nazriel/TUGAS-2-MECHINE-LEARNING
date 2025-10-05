from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join('models', 'model.pkl')
model = None

# Try to load model at startup
if os.path.exists(MODEL_PATH):
	try:
		model = joblib.load(MODEL_PATH)
	except Exception:
		model = None

# Nilai R2 dan RMSE dari hasil training (sesuaikan dengan hasil di notebook)
R2_SCORE = 0.133  # Dari hasil training di notebook ta2.ipynb
RMSE_SCORE = 10.352  # Dari hasil training di notebook ta2.ipynb

@app.route("/", methods=["GET", "POST"])
def index():
	prediction = None
	study_hours_input = None
	error = None
	
	if request.method == "POST":
		try:
			# Ambil input jam belajar dari form
			study_hours_input = float(request.form.get("study_hours"))
			
			if study_hours_input < 0:
				raise ValueError('Jam belajar tidak boleh negatif.')
			
			if model is None:
				error = 'Model belum tersedia. Jalankan notebook pelatihan untuk membuat models/model.pkl.'
			else:
				# Prediksi menggunakan model
				# Model di-train dengan DataFrame, jadi kita perlu menggunakan DataFrame dengan nama kolom
				input_data = pd.DataFrame([[study_hours_input]], columns=['weekly_self_study_hours'])
				prediction = model.predict(input_data)[0]
				prediction = round(prediction, 2)
			
		except (ValueError, TypeError) as e:
			error = f"Error: {str(e)}"
	
	return render_template(
		"index.html",
		prediction=prediction,
		study_hours=study_hours_input,
		error=error,
		r2=R2_SCORE,
		rmse=RMSE_SCORE,
		model_loaded=model is not None
	)

if __name__ == "__main__":
	app.run(debug=True)

