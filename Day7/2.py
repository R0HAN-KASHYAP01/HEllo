class Bank:
    def interest(self):
        return 0
    
class Sbi:
    def interest(self):
        return 5.5

class pnb:
    def interest(self):
        return 6.0

bank = Bank()
sbi = Sbi()
Pnb = pnb()

print("Default Bank interest:", bank.interest()) 
print("SBI interest rate:", sbi.interest())       
print("PNB interest rate:", Pnb.interest())       