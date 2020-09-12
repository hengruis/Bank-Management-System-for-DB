from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(primary_key=True, max_length=20)
    city = models.CharField(max_length=20)
    asset = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.bank_name + ' ' + self.city + ' ' + str(self.asset)


class Department(models.Model):
    depart_id = models.CharField(primary_key=True, max_length=4)
    depart_name = models.CharField(max_length=20)
    depart_type = models.CharField(max_length=15, blank=True)
    manager = models.CharField(max_length=18)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, to_field='bank_name')

    def __str__(self):
        return self.depart_id + ' ' + self.depart_name


class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=18)
    emp_name = models.CharField(max_length=20)
    emp_phone = models.CharField(max_length=11, blank=True)
    emp_addr = models.CharField(max_length=50, blank=True)
    emp_type = models.IntegerField()
    emp_start = models.DateField()
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, to_field='depart_id')

    def __str__(self):
        return self.emp_id + ' ' + self.emp_name


class Client(models.Model):
    client_id = models.CharField(primary_key=True, max_length=100)
    client_name = models.CharField(max_length=10)
    client_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50, blank=True, null=True)
    contact_phone = models.CharField(max_length=11)
    contact_name = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=30, blank=True, null=True)
    relation = models.CharField(max_length=10)
    loan_res = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='loan_res', to_field='emp_id', null=True)
    acc_res = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='acc_res', to_field='emp_id', null=True)

    def __str__(self):
        return self.client_id + ' ' + self.client_name


class Account(models.Model):
    account_id = models.CharField(primary_key=True, max_length=6)
    remain = models.FloatField()
    open_date = models.DateField()
    account_type = models.CharField(max_length=5)

    def __str__(self):
        return self.account_id + ' ' + str(self.remain) + ' ' + str(self.open_date) + ' ' + self.account_type


class SaveAcc(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='account_id', primary_key=True)
    interest_rate = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)


class CheckAcc(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='account_id', primary_key=True)
    overdraft = models.FloatField(blank=True, null=True)


class ClientAcc(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='account_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='client_id')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, to_field='bank_name')
    latest_access = models.DateField(blank=True, null=True)
    account_type = models.CharField(max_length=5)

    def __str__(self):
        return self.account_type

    class Meta:
        unique_together = ("account", "client")


class Loan(models.Model):
    loan_id = models.CharField(primary_key=True, max_length=4)
    amount = models.FloatField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, to_field='bank_name')
    state = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.loan_id + ' ' + str(self.amount) + ' ' + self.state


class ClientLoan(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, to_field='loan_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='client_id')

    class Meta:
        unique_together = ("loan", "client")


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, to_field='loan_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='client_id')
    pay_amount = models.FloatField()
    pay_date = models.DateField()

    class Meta:
        unique_together = ("loan", "client", "pay_amount", "pay_date")
    
    def __str__(self):
        return str(self.pay_amount) + ' ' + str(self.pay_date)
