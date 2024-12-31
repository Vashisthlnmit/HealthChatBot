from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)

# Route for Home Page
@app.route("/", methods=["GET"])
def home():
    #api_response = None
    #error_message = None
    # Render the same template with the API response or error
    return render_template("home.html")
@app.route("/medic_usage",methods=["GET", "POST"])
def med_usage():
    api_response = None
    error_message = None

    if request.method == "POST":
        user_input = request.form.get("user_input")  # Get input from form
        #print(f"User Input: {user_input}")  # Debugging user input

        if user_input:
            api_url = "http://127.0.0.1:5000/api/v1/meduse"
            payload = {"medicine_name": user_input}
            try:
                #print(f"Sending payload to API: {payload}")  # Debugging payload
                response = requests.post(api_url, json=payload)
                #print(f"API Response Status Code: {response.status_code}")  # Debugging status code
                #print(f"API Response Content: {response.text}")  # Debugging response content
                response.raise_for_status()

                api_response = response.json()  # Parse JSON response
                #print(f"Parsed API Response: {api_response}")  # Debugging parsed response

            except requests.exceptions.RequestException as e:
                error_message = f"API request failed: {e}"
                print(f"Error: {error_message}")  # Debugging error message
        else:
            error_message = "Please provide valid input."
            print("Error: No input provided.")  # Debugging missing input

    return render_template(
        "Medicine_usage.html",
        api_response=api_response,
        error=error_message
    )
@app.route("/disease",methods=["GET", "POST"])
def disease_usage():
    api_response = None
    error_message = None

    if request.method == "POST":
        user_input = request.form.get("user_input")  # Get input from form
        #print(f"User Input: {user_input}")  # Debugging user input

        if user_input:
            api_url = "http://127.0.0.1:5000/api/v1/disease"
            payload = {"disease_name": user_input}
            try:
                #print(f"Sending payload to API: {payload}")  # Debugging payload
                response = requests.post(api_url, json=payload)
                #print(f"API Response Status Code: {response.status_code}")  # Debugging status code
                #print(f"API Response Content: {response.text}")  # Debugging response content
                response.raise_for_status()

                api_response = response.json()  # Parse JSON response
                #print(f"Parsed API Response: {api_response}")  # Debugging parsed response

            except requests.exceptions.RequestException as e:
                error_message = f"API request failed: {e}"
                print(f"Error: {error_message}")  # Debugging error message
        else:
            error_message = "Please provide valid input."
            print("Error: No input provided.")  # Debugging missing input

    return render_template(
        "Disease.html",
        api_response=api_response,
        error=error_message
    )
@app.route("/ddt",methods=["GET", "POST"])
def disease_diet():
    api_response = None
    error_message = None

    if request.method == "POST":
        user_input = request.form.get("user_input")  # Get input from form
        #print(f"User Input: {user_input}")  # Debugging user input
        if user_input:
            api_url = "http://127.0.0.1:5000/api/v1/dietplan"
            payload = {"disease_name": user_input}
            try:
                print(f"Sending payload to API: {payload}")  # Debugging payload
                response = requests.post(api_url, json=payload)
                #print(f"API Response Status Code: {response.status_code}")  # Debugging status code
                #print(f"API Response Content: {response.text}")  # Debugging response content
                response.raise_for_status()
                api_response = response.json()
                 # Parse JSON response
                #print(f"Parsed API Response: {api_response}")  # Debugging parsed response

            except requests.exceptions.RequestException as e:
                error_message = f"API request failed: {e}"
                print(f"Error: {error_message}")  # Debugging error message
        else:
            error_message = "Please provide valid input."
            print("Error: No input provided.")  # Debugging missing input

    return render_template(
        "Disease_Diet.html",
        api_response=api_response,
        error=error_message
    )
    # api_response=None
    # error_message=None
    # if request.method=="POST":
    #     user_input=request.form.get("user_input")
    #     if user_input:
    #         api_url="http://127.0.0.1:5000/api/v1/dietplan"
    #         payload={"input":user_input}
    #         try:
    #             response=requests.post(api_url,json=payload)
    #             response.raise_for_status()
    #             api_response=response.json()
    #         except requests.exceptions.RequestException as e:
    #             error_message=f"API request failed: {e}"
    #     else:
    #         error_message="Please provide valid input."
    # return render_template("Disease_Diet.html",api_response=api_response,error=error_message)
@app.route("/med_org", methods=["GET", "POST"])
def medicine_org():
    api_response = None
    error_message = None  
    if request.method == "POST":
        uploaded_file = request.files.get("file_input")
        #print(uploaded_file)
        if uploaded_file and uploaded_file.filename != '':
            try:
                # Read the file content
                file_content = uploaded_file.read()
                #print(file_content)
                if not file_content:
                    raise ValueError("File content is empty.")
                
                # Call the API
                api_url = "http://127.0.0.1:5000/api/v1/medorg"
                payload = {"file": file_content.decode("utf-8")}
                response = requests.post(api_url, json=payload)
                response.raise_for_status()  # Raise exception for HTTP errors
                api_response = response.json()  # Parse JSON response
            except requests.exceptions.RequestException as e:
                error_message = f"API request failed: {e}"
            except Exception as e:
                error_message = f"An error occurred: {e}"
        else:
            error_message = "Please upload a file."
    
    return render_template("Medicine_Organ.html", api_response=api_response, error=error_message)          
@app.route("/med_dis",methods=["GET", "POST"])
def med_dis():
    api_response = None
    error_message = None  
    if request.method == "POST":
        uploaded_file = request.files.get("file_input")
        #print(uploaded_file)
        if uploaded_file and uploaded_file.filename != '':
            try:
                # Read the file content
                file_content = uploaded_file.read()
                #print(file_content)
                if not file_content:
                    raise ValueError("File content is empty.")
                
                # Call the API
                api_url = "http://127.0.0.1:5000/api/v1/medfile"
                payload = {"file": file_content.decode("utf-8")}
                response = requests.post(api_url, json=payload)
                response.raise_for_status()  # Raise exception for HTTP errors
                api_response = response.json()  # Parse JSON response
            except requests.exceptions.RequestException as e:
                error_message = f"API request failed: {e}"
            except Exception as e:
                error_message = f"An error occurred: {e}"
        else:
            error_message = "Please upload a file."
    
    return render_template("Medicine_Disease.html", api_response=api_response, error=error_message)     
    # api_response=None
    # error_message=None
    # if request.method=="POST":
    #     uploaded_file = request.files.get("file_input")
    #     if uploaded_file and uploaded_file.filename!= '':
    #         try:
    #              file_content = uploaded_file.read()
    #              api_url="http://127.0.0.1:5000/api/v1/medfile"
    #              payload={"file":file_content.decode("utf-8")}
    #              response = requests.post(api_url, json=payload)
    #              response.raise_for_status()
    #              api_response = response.json()  
    #         except requests.exceptions.RequestException as e:
    #             error_message = f"API request failed: {e}"
    #     else:
    #         error_message = "Please upload a file."
    # return render_template("Medicine_Disease.html", api_response=api_response, error=error_message)
# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8090,debug=True)
