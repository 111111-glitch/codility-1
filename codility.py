#2020-01-01 [0] range of dates are 2020-01-01 and 2020-12-31
#A = [N] (Transaction amount)
#D = ["N"] (Transaction dates which have the format of YYYY-MM-DD)
#N is an integer within [1...100]
#each element of A is within [-1000,1000]
#D(YYYY-MM-DD)[2020-01-01,2020-12-31]

#MAIN TASK IS TO COMPUTE THE FINAL BALANCE AT THE END OF YEAR 2020
#For a transaction,if amount < 0 = this is a card payment ,else (>=):this is an incoming transfer
#in each month,if the account has a card, 5 shillings are deducted monthly unless a minimum of 3 payments were made and the amount adds up to at least 100 shillings

#at the begginning of the year ,2020-01-01 the list of transactions were empty.

def Solution(A, D):
    # the initial balance of the account is 0 and the list of transactions is empty
    balance = 0
    card_payments = {}

    #setting the date format
    for amount, date in zip(A, D):
        #not sure 
         month = int(date.split('-')[1]) #split date by (-) 
       

        # checking if amount is < 0 then that's a card payment else that is an incoming transfer
         if amount < 0:
            # card payment, the balance should be the amount deducted 
            balance += amount
            card_payments.setdefault(month, []).append(amount)  # this transaction should be added to the balance 
         else: 
            # if the amount is greater than 0 that's an incoming transfer
            balance += amount

        # Deducting 5 shillings for an account that has a card unless 3 minimum payments have been made and amount to 100 shillings
        # to check the number of payments in a month I will check the length of the card payments and if the sum of those amounts are 100
         if month in card_payments and len(card_payments[month]) >= 3 and sum(card_payments[month]) >= 100:
            balance -= 5  # if it doesn't satisfy the above, the balance will be deducted by 5

    return balance


print(Solution([-60,60,-40,-20], ["2020-10-01" ,"2020-02-02" ,"2020-10-10" ,"2020-10-30"]))
     

    
   
     