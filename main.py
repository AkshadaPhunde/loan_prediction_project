
from flask import Flask,request,render_template

from projectapp.utils import Loan_data

app = Flask(__name__)

@app.route("/")
def home_api():
    print("We are in Home API")
    return render_template("index1.html")

@app.route("/prediction", methods=["GET"])
def Loan_prediction():
    print("We are in Loan Prediction")
    if request.method == "GET":
        print("We are in get method")
        credit_policy                    =  eval(request.args.get("credit_policy"))
        int_rate                         =  eval(request.args.get("int_rate"))
        installment                      =  eval(request.args.get("installment"))
        log_annual_inc                   =  eval(request.args.get("log_annual_inc"))
        dti                              =  eval(request.args.get("dti"))
        fico                             =  eval(request.args.get("fico"))
        days_with_cr_line                =  eval(request.args.get("days_with_cr_line"))
        revol_bal                        =  eval(request.args.get("revol_bal"))
        revol_util                       =  eval(request.args.get("revol_util"))
        inq_last_6mths                   =  eval(request.args.get("inq_last_6mths"))
        delinq_2yrs                      =  eval(request.args.get("delinq_2yrs"))
        pub_rec                          =  eval(request.args.get("pub_rec"))
        purpose                          = request.args.get("purpose")
    
        object = Loan_data(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
                        inq_last_6mths,delinq_2yrs,pub_rec,purpose)
        prediction = object.get_prediction()

        if prediction == 0:
            return render_template("index1.html",prediction="You Paid Complete Loan")
    
        else:
            return render_template("index1.html",prediction="You Does Not Paid Complete Loan")
        
    
if __name__ == "__main__":
    app.run()
        