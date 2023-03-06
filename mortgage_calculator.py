#first need to set up a mortgage class
#write down the formulas for mortgage 
#ask user for how much they want to borrow and how long will the mortgage be
#let's start by imaginanning that the interest is fixed
class Mortgage:
    def __init__(self, years_to_pay_back_loan, amount_to_borrow, interest_rate):
        self.monthly_interest_rate = (interest_rate / 12) / 100
        self.month_for_loan = years_to_pay_back_loan * 12
        self.amount_to_borrow = amount_to_borrow
        self.monthly_payment = self.amount_to_borrow * (self.monthly_interest_rate*(1 + self.monthly_interest_rate)**self.month_for_loan) / ((1 + self.monthly_interest_rate)**self.month_for_loan -1)
        self.total_amount_to_pay = self.monthly_payment * self.month_for_loan

def set_up_mortgage():#gets the needed data from the user
    amount_to_borrow = int(input("Please enter the amount you would like to borrow in your mortgage"))
    interest_rate = int(input("Please enter the current interest rate in the market"))
    years_to_pay_back_loan = int(input("Please enter how long will your mortgage be in years"))
    return Mortgage(years_to_pay_back_loan, amount_to_borrow, interest_rate)

def print_data_to_user(mortgage):#prints the data the user wants for him
    print("The monthly payment will be ${}".format(mortgage.monthly_payment))
    print("The total amount of the pay-back will come up to ${}".format(mortgage.total_amount_to_pay))
    
mortgage1 = set_up_mortgage()
print_data_to_user(mortgage1)