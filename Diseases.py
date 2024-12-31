import ollama
import asyncio
def Dieseas_name(input_text):
    try:
        prompt=f"""
                 You are Health Expert. You will be given a name of Disease.
                        Here is a name of Disease:
                        {input_text}
                        Please:
                        1. Tell about Symptons into three category Normal,Mild,Severe. 
                        2. Tell the name of Medical Test to confirm it.
                        3. Tell the Emergency Treatment.
                        4. Tell whether it is curable or not. Communicable or Not Communicable.
                        5. Tell the Preventation.
                        6. Tell the Home Treatment,Medication for Same.
                        7. Tell the Best Hospital in India for Disease
                        
            """
        response=ollama.generate(model="llama3.2",prompt=prompt)
        generated_text = response.get("response", "")
        # for Testing purposes
        #print("==== Categorized List: ===== \n")
        #print(generated_text)
        # Actual use of code
        return generated_text
    except Exception as e:
        print("An error occured:",str(e))
#Dieseas_name("Lung Cancer")
def Disease_DietPlan(input_text):
    try:
        prompt=f"""
                 You are Health Expert. You will be given a name of Disease .
                        Here is a name of Disease:
                        {input_text}
                        Please:
                        1. Tell the Diet Plan for Disease.
                        2. Tell the Diet Plan for Vegetarian and Non-Vegetarian.
                        3. Categorize the Diet Plan into appropriate categories such as Lunch,Dinner,BreakFast,Day.
                        4. Further Categorize the Diet Plan into appropriate categories such as Normal,Mild,Severe.
                        
                """
        response=ollama.generate(model="llama3.2",prompt=prompt)
        generated_text = response.get("response", "")
        # for Testing purposes
        #print("==== Categorized List: ===== \n")
        #print(generated_text)
        # Actual use of code
        return generated_text
    except Exception as e:
        print("An error occured:",str(e))    
#Disease_DietPlan("Diabetes") 