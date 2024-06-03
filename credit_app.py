import gradio as gr
import numpy as np
import pickle

# Load the pre-trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# Define the function that will process the inputs
def process_data(Months, Credit_amount, Installment_rate, residence, Age, Existing_credits, 
                 Liable_for_maintenance, Telephone, foreign_worker, Account_Status_A11,
                 Account_Status_A12, Account_Status_A13, Account_Status_A14, Credit_history_A30,
                 Credit_history_A31, Credit_history_A32, Credit_history_A33, Credit_history_A34,
                 Purpose_A40, Purpose_A41, Purpose_A410, Purpose_A42, Purpose_A43,
                 Purpose_A44, Purpose_A45, Purpose_A46, Purpose_A48, Purpose_A49,
                 Savings_bonds_A61, Savings_bonds_A62, Savings_bonds_A63, Savings_bonds_A64,
                 Savings_bonds_A65, employment_A71, employment_A72, employment_A73, 
                 employment_A74, employment_A75, Personal_status_and_sex_A91,
                 Personal_status_and_sex_A92, Personal_status_and_sex_A93,
                 Personal_status_and_sex_A94, debtors_guarantors_A101, debtors_guarantors_A102,
                 debtors_guarantors_A103, Property_A121, Property_A122, Property_A123,
                 Property_A124, Installment_plans_A141, Installment_plans_A142,
                 Installment_plans_A143, Housing_A151, Housing_A152, Housing_A153,
                 Job_A171, Job_A172, Job_A173, Job_A174):
    
    Telephone = 1 if Telephone == "Yes" else 0
    foreign_worker = 1 if foreign_worker == "Yes" else 0
    Account_Status_A11 = 1 if Account_Status_A11 == "... < 0 DM" else 0
    Account_Status_A12 = 1 if Account_Status_A12 == "... < 200 DM" else 0
    Account_Status_A13 = 1 if Account_Status_A13 == "... >= 200 DM / Salary Assignments for at least 1 year" else 0
    Account_Status_A14 = 1 if Account_Status_A14 == "No Checking Account" else 0
    Credit_history_A30 = 1 if Credit_history_A30 == "no credits taken/ all credits paid back duly" else 0
    Credit_history_A31 = 1 if Credit_history_A31 == "all credits at this bank paid back duly" else 0
    Credit_history_A32 = 1 if Credit_history_A32 == "existing credits paid back duly till now" else 0
    Credit_history_A33 = 1 if Credit_history_A33 == "delay in paying off in the past" else 0
    Credit_history_A34 = 1 if Credit_history_A34 == "critical account/  other credits existing (not at this bank)" else 0
    Purpose_A40 = 1 if Purpose_A40 == "car (new)" else 0
    Purpose_A41 = 1 if Purpose_A41 == "car (used)" else 0
    Purpose_A42 = 1 if Purpose_A42 == "furniture/equipment" else 0
    Purpose_A43 = 1 if Purpose_A43 == "radio/television" else 0
    Purpose_A44 = 1 if Purpose_A44 == "domestic appliances" else 0
    Purpose_A45 = 1 if Purpose_A45 == "repairs" else 0
    Purpose_A46 = 1 if Purpose_A46 == "education" else 0
    # Purpose_A47 = 1 if Purpose_A47 == "(vacation - does not exist?)" else 0
    Purpose_A48 = 1 if Purpose_A48 == "retraining" else 0
    Purpose_A49 = 1 if Purpose_A49 == "business" else 0
    # Purpose_A410 = 1 if Purpose_A410 == "Others" else 0
    Savings_bonds_A61 = 1 if Savings_bonds_A61 == "... < 100 DM" else 0
    Savings_bonds_A62 = 1 if Savings_bonds_A62 == "100 <= ... < 500 DM" else 0
    Savings_bonds_A63 = 1 if Savings_bonds_A63 == "500 <= ... < 1000 DM" else 0
    Savings_bonds_A64 = 1 if Savings_bonds_A64 == ".. >= 1000 DM" else 0
    Savings_bonds_A65 = 1 if Savings_bonds_A65 == "unknown/ no savings account" else 0
    employment_A71 = 1 if employment_A71 == "unemployed" else 0
    employment_A72 = 1 if employment_A72 == "... < 1 year" else 0
    employment_A73 = 1 if employment_A73 == "... < 4 years" else 0
    employment_A74 = 1 if employment_A74 == "... < 7 years" else 0
    employment_A75 = 1 if employment_A75 == ".. >= 7 years" else 0
    Personal_status_and_sex_A91 = 1 if Personal_status_and_sex_A91 == "male : divorced/separated" else 0
    Personal_status_and_sex_A92 = 1 if Personal_status_and_sex_A92 == "female : divorced/separated" else 0
    Personal_status_and_sex_A93 = 1 if Personal_status_and_sex_A93 == "male : single" else 0
    Personal_status_and_sex_A94 = 1 if Personal_status_and_sex_A94 == "male : married/widowed" else 0
    # Personal_status_and_sex_A95 = 1 if Personal_status_and_sex_A95 == "female : single" else 0
    debtors_guarantors_A101 = 1 if debtors_guarantors_A101 == "none" else 0
    debtors_guarantors_A102 = 1 if debtors_guarantors_A102 == "co-applicant" else 0
    debtors_guarantors_A103 = 1 if debtors_guarantors_A103 == "guarantor" else 0
    Property_A121 = 1 if Property_A121 == "real estate" else 0
    Property_A122 = 1 if Property_A122 == "building society savings agreement/ life insurance" else 0
    Property_A123 = 1 if Property_A123 == "car or other" else 0
    Property_A124 = 1 if Property_A124 == "unknown / no property" else 0
    Installment_plans_A141 = 1 if Installment_plans_A141 == "bank" else 0
    Installment_plans_A142 = 1 if Installment_plans_A142 == "stores" else 0
    Installment_plans_A143 = 1 if Installment_plans_A143 == "none" else 0
    Housing_A151 = 1 if Housing_A151 == "rent" else 0
    Housing_A152 = 1 if Housing_A152 == "own" else 0
    Housing_A153 = 1 if Housing_A153 == "for free" else 0
    Job_A171 = 1 if Job_A171 == "unemployed/ unskilled  - non-resident" else 0
    Job_A172 = 1 if Job_A172 == "unskilled - resident" else 0
    Job_A173 = 1 if Job_A173 == "skilled employee / official" else 0
    Job_A174 = 1 if Job_A174 == "management/ self-employed/highly qualified employee/ officer" else 0
    input_data = np.array([[Months, Credit_amount, Installment_rate, residence, Age, Existing_credits, 
                 Liable_for_maintenance, Telephone, foreign_worker, Account_Status_A11,
                 Account_Status_A12, Account_Status_A13, Account_Status_A14, Credit_history_A30,
                 Credit_history_A31, Credit_history_A32, Credit_history_A33, Credit_history_A34,
                 Purpose_A40, Purpose_A41, Purpose_A410, Purpose_A42, Purpose_A43,
                 Purpose_A44, Purpose_A45, Purpose_A46, Purpose_A48, Purpose_A49,
                 Savings_bonds_A61, Savings_bonds_A62, Savings_bonds_A63, Savings_bonds_A64,
                 Savings_bonds_A65, employment_A71, employment_A72, employment_A73, 
                 employment_A74, employment_A75, Personal_status_and_sex_A91,
                 Personal_status_and_sex_A92, Personal_status_and_sex_A93,
                 Personal_status_and_sex_A94, debtors_guarantors_A101, debtors_guarantors_A102,
                 debtors_guarantors_A103, Property_A121, Property_A122, Property_A123,
                 Property_A124, Installment_plans_A141, Installment_plans_A142,
                 Installment_plans_A143, Housing_A151, Housing_A152, Housing_A153,
                 Job_A171, Job_A172, Job_A173, Job_A174]])
    prediction = model.predict(input_data)
    return "Good" if prediction[0] == 1 else "Bad"



# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Glass()) as demo:
    gr.Markdown("# Credit Risk Assessment")
    
    with gr.Row():
        Months = gr.Number(label="Months")
        Credit_amount = gr.Number(label="Credit Amount")
        Installment_rate = gr.Number(label="Installment Rate")
        residence = gr.Number(label="Residence Since")
        Age = gr.Number(label="Age (years)")
        Existing_credits = gr.Number(label="Existing Credits at this bank")
        Liable_for_maintenance = gr.Number(label="Liable for Maintenance")
        Telephone = gr.Radio(choices=["Yes", "No"], label="Telephone")
        foreign_worker = gr.Radio(choices=["Yes", "No"], label="Foreign Worker")
    
    with gr.Row():
        Account_Status = gr.Radio(
            choices=["... < 0 DM", "... < 200 DM", "... >= 200 DM / Salary Assignments for at least 1 year",
                     "No Checking Account"], 
            label="Status of existing checking account"
        )
        Credit_history = gr.Radio(
            choices=["no credits taken/ all credits paid back duly", "all credits at this bank paid back duly",
                    "existing credits paid back duly till now", "delay in paying off in the past",
                    "critical account/  other credits existing (not at this bank)"], 
            label="Credit History"
        )
        Purpose = gr.Radio(
            choices=["car (new)", "car (used)", "furniture/equipment", "radio/television", "domestic appliances", 
                     "repairs", "education", "retraining", "business"], 
            label="Purpose"
        )
        Savings_bonds = gr.Radio(
            choices=["... < 100 DM", "100 <= ... < 500 DM", "500 <= ... < 1000 DM", ".. >= 1000 DM",
                     "unknown/ no savings account"], 
            label="Savings account/bonds"
        )
        employment = gr.Radio(
            choices=["unemployed", "... < 1 year", "... < 4 years", "... < 7 years", ".. >= 7 years"], 
            label="Present employment since"
        )
        Personal_status_and_sex = gr.Radio(
            choices=["male : divorced/separated", "female : divorced/separated", "male : single", "male : married/widowed"], 
            label="Personal Status and Sex"
        )
        debtors_guarantors = gr.Radio(
            choices=["none", "co-applicant", "guarantor"], 
            label="Other debtors / guarantors"
        )
        Property = gr.Radio(
            choices=["real estate", "building society savings agreement/ life insurance", "car or other", "unknown / no property"], 
            label="Property"
        )
        Installment_plans = gr.Radio(
            choices=["bank", "stores", "none"], 
            label=" Other Installment Plans"
        )
        Housing = gr.Radio(
            choices=["rent", "own", "for free"], 
            label="Housing"
        )
        Job = gr.Radio(
            choices=["unemployed/ unskilled  - non-resident",
                     "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"], 
            label="Job"
        )

    process_button = gr.Button("Process")
    output = gr.Textbox(label="Prediction")

    process_button.click(
        fn=process_data,
        inputs=[
            Months, Credit_amount, Installment_rate, residence, Age, Existing_credits, 
            Liable_for_maintenance, Telephone, foreign_worker, Account_Status, 
            Credit_history, Purpose, Savings_bonds, employment, Personal_status_and_sex, 
            debtors_guarantors, Property, Installment_plans, Housing, Job
        ],
        outputs=output

    )
    
demo.launch(share=True)