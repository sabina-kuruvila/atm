from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from . models import ATM

# Create your views here.

def atm_menu(request):
    if request.method == 'POST':
        action = request.POST.get('action') # This will be a string, even if it's a number
       
        request.session['action'] = action
        # Checking the customer's choice
        if action == 'Balance':
            return redirect(get_balance) 
        elif action == 'Withdraw':        
            return redirect(withdrawal)
        elif action == 'Deposit':
            return redirect(deposit)
        elif action == 'Exit':
            return redirect(exit_atm) 
        else:
            return HttpResponse("Invalid action")
    else:
        message ="Welcome to ATM"
        return render(request, "atm/atm_menu.html", {'message': message})
    
################################################################################################################################

def get_balance(request):
    atm = ATM.objects.first()
    if atm is not None:  # Check if the ATM object exists
        balance = atm.balance  # Access the balance attribute
        message = f"The current balance is : ₹{balance}"
    else:
        balance = None  # Set balance to None if no ATM object is found
        message = "Balance is not available"

    context = {
                'atm': atm,
                'message': message,
                }
    return render(request, "atm/get_balance.html", context)

##################################################################################################################################

def withdrawal(request):
    atm = ATM.objects.first()

    if request.method == 'POST': 
        amount = request.POST.get('amount')
        amount = Decimal(amount)
           
        if amount:
            if amount >= atm.withdrawal_min and amount <= atm.withdrawal_max: 
                if (amount % 50 ==0 or amount % 100 == 0):

                    if atm.balance - amount >= atm.min_balance:
                        atm.balance = atm.balance - amount
                        atm.save()
                        
                        message =f"The amount withdrawn is : {amount}"
                    else:
                        message =f"Your account is insufficient to withdraw the amount. The minimum balance should be {atm.min_balance}"
                else:
                    message =f"The amount entered shoud be in the denominations of 50 or 100"
            else: 
                message = f"Please enter the amount between ₹{atm.withdrawal_min} and ₹{atm.withdrawal_max}."
        
            context = {
            'atm': atm,
            'message': message,
            }
            return render(request, "atm/withdrawal.html", context)       
    else:
        message ="Withdrawal"
        context = {
            'atm': atm,
            'message': message,
            }
        return render(request, "atm/withdrawal.html", context)

##########################################################################################################################
        
def deposit(request):
    atm = ATM.objects.first()
    if request.method == 'POST': 
        amount = Decimal(request.POST.get('deposit_amount'))
        if amount:
            if atm.deposit_min <= amount <= atm.deposit_max:

                atm.balance =atm.balance + amount
                atm.save()
                message = f"The amount deposited is : ₹{amount}"
            else:
                message = f"Please enter the amount between ₹{atm.deposit_min} and ₹{atm.deposit_max}."
            
            context = {
                'atm': atm,
                'message': message,
                }
            return render(request, "atm/deposit.html", context)
       

    else:
        message ="Deposit"
        context = {
            'atm': atm,
            'message': message,
            }
        return render(request, "atm/deposit.html", context)
    
#############################################################################################################################

def exit_atm(request):
    atm = ATM.objects.first()
    message = "Thank you for using ATM.See you again"
    context = {
            'atm': atm,
            'message': message,
            }
    return render(request, "atm/exit_atm.html", context)