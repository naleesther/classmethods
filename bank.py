
class Account:
    def __init__(self,accountname,accountnumber):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]


      
    def deposit(self,amount):

       if amount<=0:
            return f"Deposit must be positive amount"
       else:
                self.balance+=amount

                self.deposits.append(amount)
                return f"Hello {self.accountname} you have deposited {amount} and your new balance is {self.balance}"

             

    def withdraw(self,amount):
        self.transaction=100
        if amount<=0:
            return f"withdraw should be greater than zero"
        elif amount >self.balance:
            return f"Your balance is{self.balance},you can't withdraw{amount}"
        else:
                self.balance-=amount+self.transaction
                self.withdrawals.append(amount)
                return f"Hello {self.accountname}, you have withdrawn {amount}.Your new balance is {self.balance} and the withdrawals are{self.withdrawals}"
    def deposits_statement(self):
        for x in self.deposits:
            print(x,end="/n")
    def withdrawals_statement(self):
        for y in self.withdrawals:
            print(y,end="/n")  
    def current_balance(self):
        return f"{self.balance}"        

