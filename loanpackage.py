# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:20:26 2023

@author: echon
"""

# Pmt is how much you pay back/mo
## n is number of months
### r is interest rate per month
#### n is number of months

def computesPmt(PV, r, n): # computes monthly payment
    
    """

    Parameters
    ----------
    Pv : TYPE float
        DESCRIPTION: amt borrowed
    r : TYPE float
        DESCRIPTION: interest rate APR
    n : TYPE integer
        DESCRIPTION: number of months to pay back loan

    Returns
    -------
    Pmt : TYPE float
        DESCRIPTION: monthly payment

    """
    r = r/100 # convert apr to decimal
    r = r/12
    
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt

def computesPV(Pmt, r, n): # computes how much money you can borrow
    """
    
    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION: how much i can pay monthly
    r : TYPE
        DESCRIPTION: APR
    n : TYPE
        DESCRIPTION: length of loan

    Returns
    -------
    Pv : TYPE float
        DESCRIPTION: amt i can borrow
    """
    r = r/100 # convert apr to decimal
    r = r/12

    Pv = (1-(1+r)**(-n)) * Pmt / r
    return Pv

def computesN(Pmt,Pv,r):
    """

    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION: how much i can pay monthly
    r : TYPE
        DESCRIPTION: APR
    Pv : TYPE float
        DESCRIPTION: amt i can borrow
        
    Returns
    -------
    n : TYPE
        DESCRIPTION: length of loan

    """
    import numpy as np
    #convert r (APR) to a decimal, per month
    r = r/12 # converts to % per month
    r = r/100 # converts % to decimal 
    
    #given Pmt, Pv, r, we compute n
    
    n = -np.log( 1-Pv*r/Pmt) / np.log(1+r)
    n= round(n,1)
    
    return n

def computesR(Pmt, PV, n):
    
    rLow = 0
    rHigh = 0.5
    diff = 2
    while abs(diff) > 0.001:
        rTry = (rLow + rHigh)/2
        diff = Pmt - PV*rTry/(1-(1+rTry)**(-n))
        if diff > 0:
            # pmt too high, increase r
            rLow = rTry
        else:
            rHigh = rTry
    return rTry

if __name__ == "__main__":                                     
                                
    import numpy as np

    while(True):
        choice = int(input("\nenter 1 for Pmt, 2 for PV, 3 for n, 4 for apr  ->  "))
        if (choice ==1 or choice == 2 or choice == 3 or choice ==4):
            break
        else:
            print(f"\nenter a 1, 2, 3, or a 4. you entered {choice}")

    if choice == 1:
        PV = input("\nEnter present value: ")
        PV = float(PV)
        # equivalently PV = float(input("enter Pv: "))
        # \n creates a new line underneath
        print(f"PV = {PV} \n")
        
        r = float(input("Enter interest (apr): "))
        #  putting a : and 0.2 makes it round to two decimal places. ends in f
        print(f"interest rate = {r: 0.3f}% \n")
        
        n = int(input('How many months:  '))
        print(f"n = {n} months\n")
        
        Pmt = computesPmt(PV, r, n)
        Pmt = np.round(Pmt, 2)
        print(f"payment is {Pmt: } per month")
        
    if choice == 2:
        
        Pmt = input('\nEnter payment: ')
        Pmt = float(Pmt)
        print(f"Pmt = {Pmt} \n")
        
        r = float(input("Enter interest (apr): "))
        print(f"interest rate = {r: 0.3f}% \n")
        
        n = int(input('How many months:  '))
        print(f"n = {n} months\n")
       
        PV = computesPV(Pmt, r, n)
        PV = np.round(PV, )
        print(f"Amount I can borrow (present value) is: {PV: }")
        
    if choice == 3:
    
        Pmt = input('\nEnter payment: ')
        Pmt = float(Pmt)
        print(f"Pmt = {Pmt} \n")
        
        PV = input("Enter present value: ")
        PV = float(PV)
        print(f"PV = {PV} \n")
        
        r = float(input("interest (apr): "))
        print(f"interest rate = {r: 0.3f}% \n")
        MonthsMakingPayment = computesN(Pmt,PV,r)
        MonthsMakingPayment = np.round(MonthsMakingPayment, 2)
        print(f"Loan will be paid off in {MonthsMakingPayment} months")
        
    if choice == 4:
        
        Pmt = input("\nEnter payment: ")
        Pmt = float(Pmt)
        print(f"Pmt = {Pmt} ")
     
        PV = input("\nEnter amount borrowed: ")
        PV = float(PV)
        print(f"PV = {PV} ")
     
        n = float(input("\nEnter number of months: "))
        print(f"n = {n}")
    
        # check for solution
          
        r = computesR(Pmt, PV, n)
        # convert to apr
        r *= 1200
        print(f"\ninterest = {r: 0.2f}% APR")