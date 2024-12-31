import ollama
import asyncio
def medicine_disease(file_content):
    try:
        # Validate input
        if not file_content.strip():
            raise ValueError("File content is empty or invalid.")

        # Create the prompt for the AI model
        prompt=f"""
                         You are Health Expert. You will be given a list of medicines.
                         Here is a list of medicines:
                         {file_content}
                         Please:
                         1. Choose the appropriate disease for the given medicine. 
                         2. Sort the items alphabetically within each category.
                         3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
                         4. Indicate the number of medicines in each disease.
                         5. Indicate the number of medicines that are not medicine.
                         6. Indicate the number of medicines that you don't know.
                        
                  """
        # Generate response from the AI model
        response = ollama.generate(model="llama3.2", prompt=prompt)

        # Extract the AI's response
        generated_text = response.get("response", "")
        if not generated_text:
            raise ValueError("Failed to generate a response from the AI model.")
        
        # Return the generated text
        return generated_text

    except Exception as e:
        # Log and return error details
        error_message = f"An error occurred while processing: {str(e)}"
        print(error_message)
        return error_message
def medicine_usage(medicine_name):
    try:
        prompt=f"""
                    You are Health Expert. You will be given a medicine name.
                    Here is a medicine name:
                    {medicine_name}
                    Please:
                       1. Tell the Purpose of Medicine
                       2. Tell the Dosage of the Medicine for Adult and child
                       3. Tell the Side Effects of the Medicine
                       4. Tell the Timing of Medicine
                       5. Tell the Warning of the Medicine
                       6. Tell the Precautions of the Medicine
                       7. Tell that it is a prescription medicine or not
                       8. Tell the Price of the Medicine
                       9. Tell the Company of the Medicine
                       10.Tell the Composition of the Medicine
                       11. At last please consult the doctor before taking the medicine
                       
                       
                """
        response= ollama.generate(model="llama3.2",prompt=prompt)
        generated_text = response.get("response", "")
        # for Testing purposes only
        #print("==== Medicine Usage: ===== \n")
        #print(generated_text)
        # Actual use of code
        return generated_text
    except Exception as e:
        print("An error occured:",str(e))

import ollama

def medicine_organ(file_content):
    try:
        # Validate input
        if not file_content.strip():
            raise ValueError("File content is empty or invalid.")

        # Create the prompt for the AI model
        prompt = f"""
        You are a Health Expert. You will be given a list of medicines.
        Here is a list of medicines:
        {file_content}
        Please:
        1. Choose the appropriate organ for the given medicine. 
        2. Sort the items alphabetically within each category.
        3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
        4. Indicate the number of medicines in each organ.
        5. Indicate the number of medicines that are not medicine.
        6. Indicate the number of medicines that you don't know.
        """

        # Generate response from the AI model
        response = ollama.generate(model="llama3.2", prompt=prompt)

        # Extract the AI's response
        generated_text = response.get("response", "")
        if not generated_text:
            raise ValueError("Failed to generate a response from the AI model.")
        
        # Return the generated text
        return generated_text

    except Exception as e:
        # Log and return error details
        error_message = f"An error occurred while processing: {str(e)}"
        print(error_message)
        return error_message
