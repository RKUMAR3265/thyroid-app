from flask import Flask, render_template, request, redirect, session, flash
import numpy as np
import pandas as pd
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import joblib
import os
import random
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ================= SAFE MODEL LOAD =================
try:
    image_model = load_model("model/image_model.h5")
    print("✅ Image model loaded")
except Exception as e:
    print("❌ Image model error:", e)
    image_model = None

try:
    clinical_model = joblib.load("model/clinical_model.pkl")
    print("✅ Clinical model loaded")
except Exception as e:
    print("❌ Clinical model error:", e)
    clinical_model = None

# ================= USER =================
USER = {
    "username": "Team03",
    "password": generate_password_hash("Rithik19")
}

# ================= HELPERS =================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 🔥 Dynamic Notes (har report alag)
def generate_notes():
    notes_pool = [
        "TSH levels fluctuate during the day.",
        "Clinical correlation is required.",
        "Ultrasound shows possible variation.",
        "Repeat test may be needed.",
        "Hormonal imbalance may be temporary.",
        "Lifestyle impacts thyroid levels.",
        "Early detection improves treatment.",
        "Consult specialist if symptoms persist.",
        "Do not rely on single report.",
        "Follow-up is recommended."
    ]
    return random.sample(notes_pool, 5)

# ================= MODEL FUNCTIONS =================

def get_image_prob(img_path):
    try:
        if image_model is None:
            return 0.5

        img = image.load_img(img_path, target_size=(160,160))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return float(image_model.predict(img_array)[0][0])
    except Exception as e:
        print("Image Error:", e)
        return 0.5


def get_clinical_prob(patient_dict):
    try:
        if clinical_model is None:
            return 0.5

        df = pd.DataFrame([patient_dict])
        return float(clinical_model.predict_proba(df)[0][1])
    except Exception as e:
        print("Clinical Error:", e)
        return 0.5


# ================= ROUTES =================

@app.route('/')
def login_page():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == USER['username'] and check_password_hash(USER['password'], password):
        session['user'] = username
        return redirect('/home')

    flash("Invalid Username or Password ❌")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')
    return render_template("register.html")


# ================= PREDICTION =================

@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect('/')

    try:
        name = request.form['name']

        # FILE UPLOAD
        file = request.files['image']
        if file.filename == '' or not allowed_file(file.filename):
            flash("Invalid image ❌")
            return redirect('/home')

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # INPUT DATA
        age = float(request.form['age'])

        patient_dict = {
            'age': age,
            'sex': int(request.form['sex']),
            'TSH': float(request.form['tsh']),
            'T3 measured': float(request.form['t3']),
            'TT4': float(request.form['tt4']),
            'T4U': float(request.form['t4u']),
            'FTI': float(request.form['fti'])
        }

        # MODEL
        img_prob = get_image_prob(filepath)
        clinical_prob = get_clinical_prob(patient_dict)

        # FUSION
        final_score = 0.6 * clinical_prob + 0.4 * img_prob

        # RESULT
        if final_score < 0.3:
            result = "LOW RISK"
            color = "green"
            message = "No immediate concern"
        elif final_score < 0.6:
            result = "MEDIUM RISK"
            color = "orange"
            message = "Further tests recommended"
        else:
            result = "HIGH RISK"
            color = "red"
            message = "Consult doctor immediately"

        # 🔥 EXTRA FEATURES
        notes = generate_notes()
        report_id = f"THY-{random.randint(1000,9999)}"
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M")

        return render_template("result.html",
            name=name,
            age=age,
            sex="Male" if patient_dict['sex']==1 else "Female",
            result=result,
            color=color,
            confidence=round(final_score*100,2),
            img_prob=round(img_prob,3),
            clin_prob=round(clinical_prob,3),
            message=message,
            image_path=filepath,
            date_time=date_time,
            notes=notes,
            report_id=report_id
        )

    except Exception as e:
        print("❌ Error:", e)
        flash("Something went wrong ❌")
        return redirect('/home')


# ================= RUN =================

if __name__ == '__main__':
    print("🚀 Server Starting...")
    app.run(debug=True, port=5000)