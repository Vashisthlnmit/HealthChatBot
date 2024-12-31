from flask import Flask,request,jsonify
from Medicine import medicine_usage
from Medicine import medicine_disease
from Medicine import medicine_organ
from Diseases import Dieseas_name
from Diseases import Disease_DietPlan
import json
app=Flask(__name__)
@app.route('/api/v1/meduse',methods=['POST'])
def med_use():
    try:
        data = request.json
        print(data)
        if not data or 'medicine_name' not in data:
            return jsonify({'error': 'Please provide medicine_name'}), 400
        
        medicine_name = data.get('medicine_name')
        result = medicine_usage(medicine_name)

        return jsonify({'result': result}), 200
    except Exception as e:
        print("An error occurred in med_use:", str(e))
        return jsonify({'error': 'An internal error occurred'}), 500
@app.route('/api/v1/medfile',methods=['POST'])
def med_dis():
    try:
        data = request.get_json()  # Parse JSON payload
        if not data or 'file' not in data:
            return jsonify({'error': 'No file content provided'}), 400
        
        file_content = data['file']  # Extract file content
        if not file_content:
            return jsonify({"error": "File content is empty"}), 400
        
        print("Processing file content")
        result = medicine_disease(file_content)  # Pass file content directly
        return jsonify({'result': result})
    except Exception as e:
        print("An error occurred in med_org:", str(e))
        return jsonify({'error': 'An internal error occurred'}), 500   
@app.route('/api/v1/medorg', methods=["POST"])
def med_org():
    try:
        data = request.get_json()  # Parse JSON payload
        if not data or 'file' not in data:
            return jsonify({'error': 'No file content provided'}), 400
        
        file_content = data['file']  # Extract file content
        if not file_content:
            return jsonify({"error": "File content is empty"}), 400
        
        print("Processing file content")
        result = medicine_organ(file_content)  # Pass file content directly
        return jsonify({'result': result})
    except Exception as e:
        print("An error occurred in med_org:", str(e))
        return jsonify({'error': 'An internal error occurred'}), 500           
@app.route('/api/v1/disease',methods=['POST'])
def dis_name():
    try:
        data=request.json
        if not data or 'disease_name' not in data:
              return jsonify({'error':'Please provide disease_name'})
        disease_name=data.get('disease_name')
        result=Dieseas_name(disease_name)
        print(result)
        return jsonify({'result':result})
    except Exception as e:
        print("An error occurred in dis_name:", str(e))
        return jsonify({'error': 'An internal error occurred'}), 500

@app.route('/api/v1/dietplan',methods=['POST'])
def dis_dietplan():
    try:
        data=request.json
        if not data or 'disease_name' not in data:
            return jsonify({'error':'Please provide disease_name'})
        disease_name=data.get('disease_name')
        result=Disease_DietPlan(disease_name)
        return jsonify({'result':result})
    except Exception as e:
        print("An error occurred in dis_dietplan:", str(e))
        return jsonify({'error': 'An internal error occurred'}), 500
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)