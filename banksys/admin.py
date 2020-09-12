from django.contrib import admin
from .models import Bank, Department, Employee, Client, Account, \
    SaveAcc, CheckAcc, ClientAcc, Loan, ClientLoan, Payment

# Register your models here.

admin.site.register(Bank)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(SaveAcc)
admin.site.register(CheckAcc)
admin.site.register(ClientAcc)
admin.site.register(Loan)
admin.site.register(ClientLoan)
admin.site.register(Payment)
