
import pandas as pd
import numpy as np
import pickle
import json
import config

class Loan_data():
    print("We are in Loan data")

    def __init__(self,credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
    inq_last_6mths,delinq_2yrs,pub_rec,purpose):
        self.credit_policy = credit_policy
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths = inq_last_6mths
        self.delinq_2yrs =delinq_2yrs
        self.pub_rec = pub_rec
        self.purpose = purpose

    def load_models(self):
        with open(config.model_path,"rb") as m:
            self.model = pickle.load(m)

        with open(config.json_path,"r") as j:
            self.json_data = json.load(j)

    def get_prediction(self):

        self.load_models()
        #purpose
        purpose_input = "purpose_" + self.purpose
        purpose_index = list(self.json_data["columns"]).index(purpose_input)

        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.credit_policy
        test_array[1] = self.int_rate
        test_array[2] = self.installment
        test_array[3] = self.log_annual_inc
        test_array[4] = self.dti
        test_array[5] = self.fico
        test_array[6] = self.days_with_cr_line
        test_array[7] = self.revol_bal
        test_array[8] = self.revol_util
        test_array[9] = self.inq_last_6mths
        test_array[10] = self.delinq_2yrs
        test_array[11] = self.pub_rec
        test_array[purpose_index] = 1

        prediction = self.model.predict([test_array])[0]
        if prediction == 0:
            return "Client Paid Complete Loan"
            
        else:
            return "Client Does Not Paid Complete Loan"

if __name__ == "__main":
    credit_policy                    = 1.000000
    int_rate                         = 0.107100
    installment                      = 228.220000
    log_annual_inc                   = 1.082143
    dti                              = 14.290000
    fico                             = 707.000000
    days_with_cr_line                = 2760.000000
    revol_bal                        = 33623.000000
    revol_util                       = 76.700000
    inq_last_6mths                   = 0.000000
    delinq_2yrs                      = 0.000000
    pub_rec                          = 0.000000
    purpose                          = "credit_card"

    object = Loan_data(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
    inq_last_6mths,delinq_2yrs,pub_rec,purpose)
    
    status = object.get_prediction()
    print("Prediction is -->",status)