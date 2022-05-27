class Account:
    def __init__(self,accountname,accountnumber,amount,balance):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.amount=amount
        self.balance=balance

    def deposit(self):
        self.balance+=self.amount
        return f"Hello {self.accountname} your new balance {self.balance}"
    def widthraw(self):
        self.balance-=self.amount 
        return f"Hello {self.accountname} your new balance {self.balance}" 

    


