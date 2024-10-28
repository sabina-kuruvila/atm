from django.db import models

# Create your models here.
class ATM(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2,default=1000)
    min_balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    withdrawal_min = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    withdrawal_max = models.DecimalField(max_digits=10, decimal_places=2, default=20000)
    deposit_min = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    deposit_max = models.DecimalField(max_digits=10, decimal_places=2, default=100000)


class transaction(models.Model):
    transaction_type_choices = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw')
    ]
    atm = models.ForeignKey(ATM, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=transaction_type_choices )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.amount} on {self.transaction_date}"