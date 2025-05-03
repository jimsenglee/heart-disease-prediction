from flask import Flask, render_template, request, jsonify, session
import numpy as np
import joblib
import os
# Import translation library
from googletrans import Translator
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'heart_disease_prediction_key'  # Needed for session management

# Initialize translator
translator = Translator()

# Load models with integrated scaling
models = {
    'svm': joblib.load('models/svm_model.pkl'),
    'rf': joblib.load('models/rf_model.pkl'),
    'lr': joblib.load('models/lr_model.pkl')
}

def validate_form_data(form_data):
    """Validate all form inputs and return errors if any"""
    errors = []
    
    # Define validation constraints
    constraints = {
        'age': {'min': 20, 'max': 100, 'type': float},
        'trestbps': {'min': 80, 'max': 200, 'type': float},
        'chol': {'min': 100, 'max': 400, 'type': float},
        'thalach': {'min': 70, 'max': 220, 'type': float},
        'oldpeak': {'min': 0, 'max': 6, 'type': float},
        'sex': {'options': ['0', '1'], 'type': int},
        'fbs': {'options': ['0', '1'], 'type': int},
        'exang': {'options': ['0', '1'], 'type': int},
        'cp': {'options': ['0', '1', '2', '3', '4'], 'type': int},
        'restecg': {'options': ['0', '1', '2'], 'type': int},
        'slope': {'options': ['0', '1', '2'], 'type': int},
        'ca': {'options': ['0', '1', '2', '3', '4'], 'type': int},
        'thal': {'options': ['0', '1', '2'], 'type': int},
        'model': {'options': ['svm', 'rf', 'lr'], 'type': str}
    }
    
    # Check if all required fields are present
    for field in constraints:
        if field not in form_data:
            errors.append(f"Missing required field: {field}")
    
    if errors:
        return errors
        
    # Validate each field
    for field, constraint in constraints.items():
        try:
            # For numeric fields with min/max
            if 'min' in constraint and 'max' in constraint:
                value = constraint['type'](form_data[field])
                if value < constraint['min'] or value > constraint['max']:
                    errors.append(f"{field} must be between {constraint['min']} and {constraint['max']}")
            
            # For fields with specific options
            elif 'options' in constraint:
                value = str(form_data[field])
                if value not in constraint['options']:
                    errors.append(f"Invalid option for {field}: {value}")
                    
        except (ValueError, TypeError):
            errors.append(f"Invalid data type for {field}")
    
    return errors

# Supported languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'zh-cn': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'ru': 'Russian',
    'ja': 'Japanese',
    'hi': 'Hindi'
}

# Text content for translation - Main page
TEXT_CONTENT = {
    'title': 'Heart Disease Prediction System',
    'subtitle': 'Enter patient information to predict heart disease risk',
    'model_selection': 'Model Selection',
    'choose_model': 'Choose a prediction model:',
    'svm': 'Support Vector Machine',
    'rf': 'Random Forest', 
    'lr': 'Logistic Regression',
    'numerical': 'Numerical Measurements',
    'binary': 'Binary Features',
    'categorical': 'Categorical Features',
    'predict_button': 'Predict Heart Disease Risk',
    'age_label': 'Age: ',
    'trestbps_label': 'Resting Blood Pressure (mm Hg):',
    'chol_label': 'Serum Cholesterol (mg/dl):', 
    'thalach_label': 'Max Heart Rate Achieved:', 
    'oldpeak_label': 'ST Depression (Oldpeak):',
    'm': 'Male',
    'f': 'Female',
    'sex_label': 'Enter Sex:',
    'fbs_label': 'Fasting Blood Sugar > 120 mg/dl?:',
    'n': 'No',
    'y': 'Yes',
    'exang_label': 'Exercise-Induced Angina:',
    'cp_label': 'Chest Pain Type:',
    'np': 'No Pain',
    'ta': 'Typical Angina',
    'aa': 'Atypical Angina',
    'nap': 'Non-anginal Pain',
    'asy': 'Asymptomatic',
    'restecg_label': 'Resting ECG:',
    'normal': 'Normal',
    'stt': 'ST-T Wave Abnormality',
    'lvh': 'Left Ventricular Hypertrophy',
    'slope_label': 'Slope of ST Segment:',
    'u': 'Up',
    'fl': 'Flat',
    'd': 'Down',
    'ca_label': 'Number of Major Vessels (0-4):',
    'thal_label': 'Thalassemia Type:',
    'fd': 'Fixed Defect',
    'rd': 'Reversible Defect',
}

# Text content for translation - Result page
RESULT_CONTENT = {
    'result_title': 'Heart Disease Prediction Results',
    'disease_detected': 'Heart Disease Detected',
    'no_disease_detected': 'No Heart Disease Detected',
    'model_used': 'Model used:',
    'risk_probability': 'Risk probability:',
    'unknown_probability': 'Unknown (Model doesn\'t provide probabilities)',
    'recommendation_title': 'Recommendation:',
    'positive_recommendation': 'Please consult with a cardiologist as soon as possible for further evaluation and treatment options.',
    'negative_recommendation': 'Continue maintaining a healthy lifestyle with regular exercise and balanced diet. Schedule routine check-ups as recommended by your healthcare provider.',
    'another_prediction': 'Make Another Prediction'
}

def translate_text(text, target_lang):
    if target_lang == 'en':  # No need to translate English
        return text
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except:
        return text  # Return original if translation fails

def translate_content(content_dict, target_lang):
    translated = {}
    for key, value in content_dict.items():
        translated[key] = translate_text(value, target_lang)
    return translated

@app.route('/')
def home():
    # Get language from session or default to English
    lang = session.get('lang', 'en')
    
    # Translate content
    content = translate_content(TEXT_CONTENT, lang)
    
    return render_template('index.html', 
                          languages=LANGUAGES,
                          current_lang=lang,
                          content=content)

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('lang', 'en')
    session['lang'] = lang
    
    # Check if this is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'success': True})
    else:
        # If not AJAX, redirect back to the referring page
        return redirect(request.referrer or url_for('home'))

@app.route('/predict', methods=['POST'])
def predict():
    # Get language from session
    lang = session.get('lang', 'en')
    content = translate_content(RESULT_CONTENT, lang)
    
    # Validate form data
    errors = validate_form_data(request.form)
    
    if errors:
        # Translate error messages
        translated_errors = [translate_text(error, lang) for error in errors]
        
        # Return to form with error messages
        form_content = translate_content(TEXT_CONTENT, lang)
        return render_template('index.html', 
                              languages=LANGUAGES,
                              current_lang=lang,
                              content=form_content,
                              errors=translated_errors)
    
    # If validation passes, continue with prediction
    try:
        features = [
            float(request.form['age']),
            int(request.form['sex']),
            int(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            int(request.form['fbs']),
            int(request.form['restecg']),
            float(request.form['thalach']),
            int(request.form['exang']),
            float(request.form['oldpeak']),
            int(request.form['slope']),
            int(request.form['ca']),
            int(request.form['thal'])
        ]
        
        # Get selected model
        model_name = request.form['model']
        if model_name not in models:
            raise ValueError("Invalid model selection")
            
        model = models[model_name]
        
        # Make prediction
        prediction = model.predict([features])[0]
        
        # Get probability if available
        if hasattr(model, 'predict_proba'):
            probability = round(model.predict_proba([features])[0][1] * 100, 2)
        else:
            probability = None
        
        return render_template('result.html', 
                              prediction=prediction, 
                              probability=probability,
                              model_name=model_name,
                              content=content,
                              languages=LANGUAGES,
                              current_lang=lang)
                              
    except Exception as e:
        # Log the error and return to form with error message
        app.logger.error(f"Prediction error: {str(e)}")
        form_content = translate_content(TEXT_CONTENT, lang)
        return render_template('index.html', 
                              languages=LANGUAGES,
                              current_lang=lang,
                              content=form_content,
                              errors=[translate_text("An error occurred during prediction. Please try again.", lang)])


@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        
        # Validate API data
        errors = validate_form_data(data)
        if errors:
            return jsonify({'error': errors}), 400
            
        features = [
            float(data['age']), int(data['sex']), int(data['cp']), float(data['trestbps']),
            float(data['chol']), int(data['fbs']), int(data['restecg']), float(data['thalach']),
            int(data['exang']), float(data['oldpeak']), int(data['slope']), int(data['ca']), int(data['thal'])
        ]
        
        # Use model directly without separate scaling
        model_name = data['model']
        if model_name not in models:
            return jsonify({'error': 'Invalid model selection'}), 400
            
        model = models[model_name]
        prediction = int(model.predict([features])[0])
        
        # Get probability if available
        result = {'prediction': prediction}
        if hasattr(model, 'predict_proba'):
            result['probability'] = round(model.predict_proba([features])[0][1] * 100, 2)
        
        return jsonify(result)
        
    except Exception as e:
        app.logger.error(f"API prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)