from datetime import datetime

class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.statement = []
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
        
    
    def  deposit(self,amount):
        if amount <=0:
             print(f"Deposit must be positive amount")
        else:
            self.balance+=amount   
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"Deposit"
            }
            self.deposits.append(amount)
            self.statement.append(transaction) 
            print(f"Hello {self.account_name}, your new balance is {self.balance} and your deposits are {self.deposits}and your statement is {self.statement}" )


    def withdrawal(self,amount):
        
        if amount+self.transaction_fee > self.balance:
            print(f"Hello {self.account_name}, your balance is {self.balance} you can't withdraw {amount}")    
        elif amount <=0:
            print(f"Withdrawal amount must be greater than 0")
        else:    
            self.balance-=amount+self.transaction_fee
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"Withdraw"
            }
            self.withdrawals.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.account_name}, your new balance is {self.balance} and the withdrawals are {self.statement}")    



    
         
    def deposit_statement(self):
        for x in self.deposits:
            print (x)
    def withdraw_statement(self):
        for y in self.withdrawals: 
            print(y)
         
    def current_balance(self):
        return f" Your current balance is  {self.balance}" 
    
    def full_statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}----{Narration}-----{amount}")  
    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
            
        if len(self.deposits) <10:
            return f"you are not eligible to borrow.make {10-len(self.deposits)} to borrow "
        if amount<100:
            return f"you can borrow atleast 100"  
        if amount>sum/3:
            return f"you can borrow upto {sum/3}" 
        if self.balance!=0:
            return f"you have ksh.{self.balance} you cant borrow yet you still have balance on your account"
        if self.loan_balance!=0:
            return f"you have a debt of {self.loan_balance} you have to pay first for you to borrow."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"you have borrowed {amount} your loan is now at {self.loan_balance}"
    
    def loan_repayment(self,amount):
        
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"
               
         else:
             self.loan_balance-=amount
             return f"thank you"
            
         
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"insuficient funds"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"you have sent {amount} to {new_account} with the name {new_account.name}.your new balance is {self.balance}"
        
             

       
          
