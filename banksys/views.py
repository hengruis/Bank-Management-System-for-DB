from django.db.models import Count
from django.shortcuts import render
import datetime

from .models import Bank, Department, Employee, Client, Account, \
    SaveAcc, CheckAcc, ClientAcc, Loan, ClientLoan, Payment

# Create your views here.

# -- client management -- #

def addClient(request):
    """
    add client to database
    """
    if request.method == 'POST':
        client_id = request.POST.get("client_id")
        client_name = request.POST.get("client_name")
        client_phone = request.POST.get("client_phone")
        address = request.POST.get("address")
        contact_phone = request.POST.get("contact_phone")
        contact_name = request.POST.get("contact_name")
        contact_email = request.POST.get("contact_email")
        relation = request.POST.get("relation")
        loan_res_id = request.POST.get("loan_res")
        acc_res_id = request.POST.get("acc_res")

        try:
            client = Client.objects.get(client_id=client_id)
            return render(request, 'banksys/client/add.html',
                            {'status': 0, 'message': 'Sorry, this client ID has already existed.'})
        except:
            try:
                new_loan_res = Employee.objects.get(emp_id=loan_res_id)
                new_acc_res = Employee.objects.get(emp_id=acc_res_id)
                new_client = Client(client_id=client_id, client_name=client_name,
                                    client_phone=client_phone, address=address,
                                    contact_phone=contact_phone, contact_name=contact_name,
                                    contact_email=contact_email, relation=relation,
                                    loan_res=new_loan_res, acc_res=new_acc_res)
                new_client.save()
                print('success')
                return render(request, 'banksys/client/add.html',
                                {'status': 1, 'message': 'Success.'})
            except:
                return render(request, 'banksys/client/add.html',
                                {'status': 2, 'message': 'Client creation failed.'})
    else:
        return render(request, 'banksys/client/add.html')


def deleteClient(request):
    """
    delete client from database
    """
    if request.method == 'POST':
        client_id = request.POST.get("client_id")
        client_name = request.POST.get("client_name")

        try:
            client_acc = ClientAcc.objects.filter(client=Client.objects.get(client_id=client_id))
            client_loan = ClientLoan.objects.filter(client=Client.objects.get(client_id=client_id))
            if client_acc.exists() or client_loan.exists():
                return render(request, 'banksys/client/delete.html',
                                {'status': 0, 'message': 'You are not allowed to delete a client that is related to one or more accounts or loans!'})
            else:
                client_to_delete = Client.objects.get(client_id=client_id)
                client_to_delete.delete()
                print('success')
                return render(request, 'banksys/client/delete.html',
                                {'status': 1, 'message': 'Success.'})
        except:
            return render(request, 'banksys/client/delete.html',
                            {'status': 2, 'message': 'Sorry, this client does not exist.'})
    else:
        return render(request, 'banksys/client/delete.html')


def modifyClient(request):
    """
    change client's info
    """
    if request.method == 'POST':
        client_id = request.POST.get("client_id")
        client_name = request.POST.get("client_name")
        client_phone = request.POST.get("client_phone")
        address = request.POST.get("address")
        contact_phone = request.POST.get("contact_phone")
        contact_name = request.POST.get("contact_name")
        contact_email = request.POST.get("contact_email")
        relation = request.POST.get("relation")
        loan_res_id = request.POST.get("loan_res")
        acc_res_id = request.POST.get("acc_res")

        try:
            client = Client.objects.get(client_id=client_id)
            try:
                if client_name: client.client_name = client_name
                if client_phone: client.client_phone = client_phone
                if address: client.address = address
                if contact_phone: client.contact_phone = contact_phone
                if contact_name: client.contact_name = contact_name
                if contact_email: client.contact_email = contact_email
                if relation: client.relation = relation
                if loan_res_id:
                    loan_res = Employee.objects.get(emp_id=loan_res_id)
                    client.loan_res = loan_res
                if acc_res_id:
                    acc_res = Employee.objects.get(emp_id=acc_res_id)
                    client.acc_res = acc_res
                client.save()
                print('success')
                return render(request, 'banksys/client/modify.html',
                                {'status': 1, 'message': 'Success.'})
            except:
                return render(request, 'banksys/client/modify.html',
                                {'status': 0, 'message': 'Client modification failed.'})
        except:
            return render(request, 'banksys/client/modify.html',
                            {'status': 2, 'message': 'Sorry, the client you have required does not exist.'})
    else:
        return render(request, 'banksys/client/modify.html')


def searchClient(request):
    """
    search for one client
    """
    if request.method == 'POST':
        client_id = request.POST.get("client_id")
        client_name = request.POST.get("client_name")

        if client_id:
            try:
                use_id = 1
                use_name = 0
                search_by_id = Client.objects.get(client_id=client_id)
                try:
                    print('success')
                    return render(request, 'banksys/client/index.html',
                                    {'status': 1, 'message': 'Success.', "search_by_id": search_by_id,
                                     'use_id': use_id, 'use_name': use_name})
                except:
                    return render(request, 'banksys/client/search.html',
                                    {'status': 0, 'message': 'Client search failed.'})
            except:
                return render(request, 'banksys/client/search.html',
                                {'status': 2, 'message': 'Sorry, the client does not exist.'})
        elif client_name:
            search_by_name = Client.objects.filter(client_name=client_name)
            if search_by_name.exists():
                try:
                    use_id = 0
                    use_name = 1
                    print('success')
                    return render(request, 'banksys/client/index.html',
                                    {'status': 1, 'message': 'Success', "search_by_name": search_by_name,
                                     'use_id': use_id, 'use_name': use_name})
                except:
                    return render(request, 'banksys/client/search.html',
                                    {'status': 0, 'message': 'Client search failed.'})
            else:
                return render(request, 'banksys/client/search.html',
                               {'status': 2, 'message': 'Sorry, the client does not exist.'})
    else:
        return render(request, 'banksys/client/search.html')



# -- account management -- #

def createAcc(request):
    """
    create one account
    """
    if request.method == 'POST':
        account_id = request.POST.get("account_id")
        client_id = request.POST.get("client_id")
        account_type = request.POST.get("account_type")
        remain = request.POST.get("remain")
        open_date = request.POST.get("open_date")
        bank_name = request.POST.get("bank_name")
        interest_rate = request.POST.get("interest_rate")
        currency = request.POST.get("currency")
        overdraft = request.POST.get("overdraft")
        remain = float(remain)
        interest_rate = float(interest_rate)
        overdraft = float(overdraft)

        try:
            account = Account.objects.get(account_id=account_id)
            return render(request, 'banksys/account/create.html',
                            {'status': 2, 'message': 'Sorry, this account ID has already existed.'})
        except:
            try:
                client = Client.objects.get(client_id=client_id)
                bank = Bank.objects.get(bank_name=bank_name)
                clientacc = ClientAcc.objects.filter(client=client, bank=bank)
                if clientacc.count() == 0:
                    new_account = Account(account_id=account_id, remain=remain,
                                            open_date=open_date, account_type=account_type)
                    new_account.save()
                    new_clientacc = ClientAcc(account=new_account, client=client,
                                                bank=bank, account_type=account_type)
                    new_clientacc.save()
                    if account_type == "save":
                        new_saveacc = SaveAcc(account=new_account, interest_rate=interest_rate, currency=currency)
                        new_saveacc.save()
                    elif account_type == "check":
                        new_checkacc = CheckAcc(account=new_account, overdraft=overdraft)
                        new_checkacc.save()
                    print('success')
                    return render(request, 'banksys/account/create.html', {'status': 1, 'message': 'Success.'})
                elif clientacc.count() == 1:
                    if account_type != clientacc[0].account_type:
                        new_account = Account(account_id=account_id, remain=remain,
                                                open_date=open_date, account_type=account_type)
                        new_account.save()
                        new_clientacc = ClientAcc(account=new_account, client=client,
                                                    bank=bank, account_type=account_type)
                        new_clientacc.save()
                        if account_type == "save":
                            new_saveacc = SaveAcc(account=new_account, interest_rate=interest_rate, currency=currency)
                            new_saveacc.save()
                        elif account_type == "check":
                            new_checkacc = CheckAcc(account=new_account, overdraft=overdraft)
                            new_checkacc.save()
                        print('success')
                        return render(request, 'banksys/account/create.html', {'status': 1, 'message': 'Success.'})
                    elif account_type == clientacc[0].account_type:
                        return render(request, 'banksys/account/create.html',
                                        {'status': 3, 'message': 'There is already the same type of account in this bank.'})
                elif clientacc.count() == 2:
                    return render(request, 'banksys/account/create.html',
                                    {'status': 4, 'message': 'There are already 2 accounts in this bank.'})
            except:
                return render(request, 'banksys/account/create.html',
                                {'status': 0, 'message': 'Account creation failed. At least one of the inputs error.'})
    else:
        return render(request, 'banksys/account/create.html')


def deleteAcc(request):
    """
    delete account from database
    """
    if request.method == 'POST':
        account_id = request.POST.get("account_id")

        try:
            account = Account.objects.get(account_id=account_id)
            try:
                account.delete()
                print('success')
                return render(request, 'banksys/account/delete.html',
                                {'status': 1, 'message': 'Success.'})
            except:
                return render(request, 'banksys/account/delete.html',
                                {'status': 0, 'message': 'Account delete failed.'})
        except:
            return render(request, 'banksys/account/delete.html',
                            {'status': 2, 'message': 'Sorry, this account does not exist.'})
    else:
        return render(request, 'banksys/account/delete.html')


def modifyAcc(request):
    """
    change account's info
    """
    if request.method == 'POST':
        account_id = request.POST.get("account_id")
        client_id = request.POST.get("client_id")
        account_type = request.POST.get("account_type")
        remain = request.POST.get("remain")
        bank_name = request.POST.get("bank_name")
        latest_access = request.POST.get("latest_access")
        interest_rate = request.POST.get("interest_rate")
        currency = request.POST.get("currency")
        overdraft = request.POST.get("overdraft")

        try:
            account = Account.objects.get(account_id=account_id)
            try:
                clientacc = ClientAcc.objects.get(account=account)
                client = Client.objects.get(client_id=client_id)
                bank = Bank.objects.get(bank_name=bank_name)

                if remain:
                    remain = float(remain)
                    account.remain = remain
                
                if client_id: clientacc.client = client
                if bank_name: clientacc.bank = bank
                if latest_access: clientacc.latest_access = latest_access
                if account_type:
                    client_bank_acc = ClientAcc.objects.filter(client=client, bank=bank)
                    if client_bank_acc.count() == 2:
                        return render(request, 'banksys/account/modify.html',
                                        {'status': 2, 'message': 'Sorry, there is already this certain type of account in this bank.'})
                    else:
                        account.account_type = account_type
                        clientacc.account_type = account_type
                        account.save()
                        clientacc.save()
                        if account_type == "save":
                            checkacc = CheckAcc.objects.get(account=account)
                            checkacc.delete()
                            interest_rate = float(interest_rate)
                            new_saveacc = SaveAcc(account=account, interest_rate=interest_rate, currency=currency)
                            new_saveacc.save()
                        elif account_type == "check":
                            saveacc = SaveAcc.objects.get(account=account)
                            saveacc.delete()
                            overdraft = float(overdraft)
                            new_checkacc = CheckAcc(account=account, overdraft=overdraft)
                            new_checkacc.save()
                elif account_type == '':
                    account.save()
                    clientacc.save()
                    if account.account_type == 'save':
                        saveacc = SaveAcc.objects.get(account=account)
                        if interest_rate != '0':
                            interest_rate = float(interest_rate)
                            saveacc.interest_rate = interest_rate
                        if currency != 'N/A':
                            saveacc.currency = currency
                        saveacc.save()
                    elif account_type == 'check':
                        if overdraft != '0':
                            overdraft = float(overdraft)
                            checkacc = CheckAcc.objects.get(account=account)
                            checkacc.overdraft = overdraft
                            checkacc.save()
                print('success')
                return render(request, 'banksys/account/modify.html',
                                {'status': 1, 'message': 'Success.'})
            except:
                return render(request, 'banksys/account/modify.html',
                                {'status': 0, 'message': 'Account modification failed. At least one of inputs error.'})
        except:
            return render(request, 'banksys/account/modify.html',
                            {'status': 3, 'message': 'Sorry, this account does not exist.'})
    else:
        return render(request, 'banksys/account/modify.html')


def searchAcc(request):
    """
    search for one account
    """
    if request.method == 'POST':
        account_id = request.POST.get("account_id")

        try:
            search_by_account_id = Account.objects.get(account_id=account_id)
            try:
                search_by_account_id_clientacc = ClientAcc.objects.get(account=search_by_account_id)
                if search_by_account_id.account_type == "save":
                    search_by_account_id_detail = SaveAcc.objects.get(account=search_by_account_id)
                elif search_by_account_id.account_type == "check":
                    search_by_account_id_detail = CheckAcc.objects.get(account=search_by_account_id)
                print('success')
                return render(request, 'banksys/account/index.html',
                                {'status': 1, 'message': 'Success.',
                                 "search_by_account_id": search_by_account_id,
                                 "search_by_account_id_detail": search_by_account_id_detail,
                                 "search_by_account_id_clientacc": search_by_account_id_clientacc})
            except:
                return render(request, 'banksys/account/search.html',
                                {'status': 0, 'message': 'Account search failed.'})
        except:
            return render(request, 'banksys/account/search.html',
                            {'status': 2, 'message': 'Sorry, the account does not exist.'})
    else:
        return render(request, 'banksys/account/search.html')



# -- loan management -- #

def addLoan(request):
    """
    add a loan
    """
    if request.method == 'POST':
        loan_id = request.POST.get("loan_id")
        client_id = request.POST.get("client_id")
        amount = request.POST.get("amount")
        bank_name = request.POST.get("bank_name")
        state = request.POST.get("state")

        try:
            loan = Loan.objects.get(loan_id=loan_id)
            return render(request, 'banksys/loan/add.html',
                            {'status': 2, 'message': 'Sorry, this loan ID is already existed.'})
        except:
            try:
                bank = Bank.objects.get(bank_name=bank_name)
                amount = float(amount)
                new_loan = Loan(loan_id=loan_id, amount=amount, bank=bank, state=state)
                new_loan.save()
                client = Client.objects.get(client_id=client_id)
                new_clientloan = ClientLoan(loan=new_loan, client=client)
                new_clientloan.save()
                print('success')
                return render(request, 'banksys/loan/add.html',
                                {'status': 1, 'message': 'Success.'})
            except:
                return render(request, 'banksys/loan/add.html',
                                {'status': 0, 'message': 'Loan creation failed.'})
    else:
        return render(request, 'banksys/loan/add.html')


def deleteLoan(request):
    """
    delete one laon
    """
    if request.method == 'POST':
        loan_id = request.POST.get("loan_id")

        try:
            loan = Loan.objects.get(loan_id=loan_id)
            if loan.state == '1':
                return render(request, 'banksys/loan/delete.html',
                                {'status': 2, 'message': 'Sorry, this loan is under-paying.'})
            else:
                try:
                    loan.delete()
                    print('success')
                    return render(request, 'banksys/loan/delete.html',
                                    {'status': 1, 'message': 'Success.'})
                except:
                    return render(request, 'banksys/loan/delete.html',
                                    {'status': 0, 'message': 'Loan delete failed.'})
        except:
            return render(request, 'banksys/loan/html',
                            {'status': 3, 'message': 'Sorry, this loan does not exist.'})
    else:
        return render(request, 'banksys/loan/delete.html')


def payLoan(request):
    """
    implement a paying-loan operation
    """
    if request.method == 'POST':
        loan_id = request.POST.get("loan_id")
        client_id = request.POST.get("client_id")
        pay_amount = request.POST.get("pay_amount")
        pay_date = request.POST.get("pay_date")

        try:
            loan = Loan.objects.get(loan_id=loan_id)
            client = Client.objects.get(client_id=client_id)
            try:
                clientloan = ClientLoan.objects.get(loan=loan)
                if clientloan.client == client:
                    paid = Payment.objects.filter(loan=loan)
                    sum = 0
                    if paid.count():
                        for pay in paid:
                            sum += pay.pay_amount
                    if sum < loan.amount:
                        pay_amount = float(pay_amount)
                        sum += pay_amount
                        if sum < loan.amount:
                            loan.state = '1'
                            new_payment = Payment(loan=loan, client=client, pay_amount=pay_amount, pay_date=pay_date)
                            new_payment.save()
                            print('success')
                            return render(request, 'banksys/loan/pay.html',
                                            {'status': 1, 'message': 'Success.'})
                        elif sum == loan.amount:
                            loan.state = '2'
                            new_payment = Payment(loan=loan, client=client, pay_amount=pay_amount, pay_date=pay_date)
                            new_payment.save()
                            print('success')
                            return render(request, 'banksys/loan/pay.html',
                                            {'status': 1, 'message': 'Success.'})
                        elif sum > loan.amount:
                            return render(request, 'banksys/loan/pay.html',
                                            {'status': 4, 'message': 'Your paying amount exceeds.'})
                    elif sum == loan.amount:
                        return render(request, 'banksys/loan/pay.html',
                                            {'status': 5, 'message': 'This loan is already finished.'})
                else:
                    return render(request, 'banksys/loan/pay.html',
                                    {'status': 3, 'message': 'The loan and the client are not matched.'})
            except:
                return render(request, 'banksys/loan/pay.html',
                                {'status': 0, 'message': 'Loan payment failed.'})
        except:
            return render(request, 'banksys/loan/pay.html',
                            {'status': 2, 'message': 'Sorry, this loan or client does not exist.'})
    else:
        return render(request, 'banksys/loan/pay.html')


def searchLoan(request):
    """
    search for one loan detail
    """
    if request.method == 'POST':
        loan_id = request.POST.get("loan_id")
        client_id = request.POST.get("client_id")

        if loan_id:
            use_loan_id = 1
            use_client_id = 0
            try:
                result_loan = Loan.objects.get(loan_id=loan_id)
                try:
                    result_clientloan = ClientLoan.objects.filter(loan=result_loan)
                    result_payment = Payment.objects.filter(loan=result_loan)
                    print('success')
                    return render(request, 'banksys/loan/detail.html',
                                    {'status': 1, 'message': 'Success.',
                                     'use_loan_id': use_loan_id,
                                     'use_client_id': use_client_id, 
                                     "result_loan": result_loan,
                                     "result_clientloan": result_clientloan,
                                     "result_payment": result_payment})
                except:
                    return render(request, 'banksys/loan/search.html',
                                   {'status': 0, 'message': 'Loan search failed.'})
            except:
                return render(request, 'banksys/loan/search.html',
                                {'status': 2, 'message': 'Sorry, this loan does not exist.'})
        elif client_id:
            use_loan_id = 0
            use_client_id = 1
            try:
                client = Client.objects.get(client_id=client_id)
                try:
                    result_clientloan = ClientLoan.objects.filter(client=client)
                    result_payment = Payment.objects.filter(client=client)
                    print('success')
                    return render(request, 'banksys/loan/detail.html',
                                    {'status': 1, 'message': 'Success.',
                                     'use_loan_id': use_loan_id,
                                     'use_client_id': use_client_id,
                                     "result_clientloan": result_clientloan,
                                     "result_payment": result_payment})
                except:
                    return render(request, 'banksys/loan/search.html',
                                    {'status': 0, 'message': 'Loan search failed.'})
            except:
                return render(request, 'banksys/loan/search.html',
                                {'status': 2, 'message': 'Sorry, this client does not exist.'})
    else:
        return render(request, 'banksys/loan/search.html')



# -- statistics -- #

def bankSavings(bank_name, year):
    """
    calculate savings sum of one bank
    """
    bank_acc = ClientAcc.objects.filter(bank=Bank.objects.get(bank_name=bank_name))

    # -- monthly savings total amount -- #
    jan_sum = 0
    feb_sum = 0
    mar_sum = 0
    apr_sum = 0
    may_sum = 0
    jun_sum = 0
    jul_sum = 0
    aug_sum = 0
    sep_sum = 0
    oct_sum = 0
    nov_sum = 0
    dec_sum = 0

    jan_acc = Account.objects.filter(open_date__year=year, open_date__month=1)
    feb_acc = Account.objects.filter(open_date__year=year, open_date__month=2)
    mar_acc = Account.objects.filter(open_date__year=year, open_date__month=3)
    apr_acc = Account.objects.filter(open_date__year=year, open_date__month=4)
    may_acc = Account.objects.filter(open_date__year=year, open_date__month=5)
    jun_acc = Account.objects.filter(open_date__year=year, open_date__month=6)
    jul_acc = Account.objects.filter(open_date__year=year, open_date__month=7)
    aug_acc = Account.objects.filter(open_date__year=year, open_date__month=8)
    sep_acc = Account.objects.filter(open_date__year=year, open_date__month=9)
    oct_acc = Account.objects.filter(open_date__year=year, open_date__month=10)
    nov_acc = Account.objects.filter(open_date__year=year, open_date__month=11)
    dec_acc = Account.objects.filter(open_date__year=year, open_date__month=12)

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in jan_acc:
                jan_sum += acc.account.remain
            elif acc.account in feb_acc:
                feb_sum += acc.account.remain
            elif acc.account in mar_acc:
                mar_sum += acc.account.remain
            elif acc.account in apr_acc:
                apr_sum += acc.account.remain
            elif acc.account in may_acc:
                may_sum += acc.account.remain
            elif acc.account in jun_acc:
                jun_sum += acc.account.remain
            elif acc.account in jul_acc:
                jul_sum += acc.account.remain
            elif acc.account in aug_acc:
                aug_sum += acc.account.remain
            elif acc.account in sep_acc:
                sep_sum += acc.account.remain
            elif acc.account in oct_acc:
                oct_sum += acc.account.remain
            elif acc.account in nov_acc:
                nov_sum += acc.account.remain
            elif acc.account in dec_acc:
                dec_sum += acc.account.remain
    
    monthly_savings_sum = [jan_sum, feb_sum, mar_sum, apr_sum, may_sum, jun_sum,
                           jul_sum, aug_sum, sep_sum, oct_sum, nov_sum, dec_sum]

    # -- quarterly savings total amount -- #
    q1_sum = 0
    q2_sum = 0
    q3_sum = 0
    q4_sum = 0

    q1_start = datetime.date(year, 1, 1)
    q1_end = datetime.date(year, 3, 31)
    q2_start = datetime.date(year, 4, 1)
    q2_end = datetime.date(year, 6, 30)
    q3_start = datetime.date(year, 7, 1)
    q3_end = datetime.date(year, 9, 30)
    q4_start = datetime.date(year, 10, 1)
    q4_end = datetime.date(year, 12, 31)

    q1_acc = Account.objects.filter(open_date__range=(q1_start, q1_end))
    q2_acc = Account.objects.filter(open_date__range=(q2_start, q2_end))
    q3_acc = Account.objects.filter(open_date__range=(q3_start, q3_end))
    q4_acc = Account.objects.filter(open_date__range=(q4_start, q4_end))

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in q1_acc:
                q1_sum += acc.account.remain
            elif acc.account in q2_acc:
                q2_sum += acc.account.remain
            elif acc.account in q3_acc:
                q3_sum += acc.account.remain
            elif acc.account in q4_acc:
                q4_sum += acc.account.remain

    quarterly_savings_sum = [q1_sum, q2_sum, q3_sum, q4_sum]

    # -- annual savings total amount -- #
    year_sum1 = 0
    year_sum2 = 0
    year_sum3 = 0
    year_sum4 = 0
    year_sum5 = 0
    year_sum6 = 0

    year_acc1 = Account.objects.filter(open_date__year=2015)
    year_acc2 = Account.objects.filter(open_date__year=2016)
    year_acc3 = Account.objects.filter(open_date__year=2017)
    year_acc4 = Account.objects.filter(open_date__year=2018)
    year_acc5 = Account.objects.filter(open_date__year=2019)
    year_acc6 = Account.objects.filter(open_date__year=2020)

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in year_acc1:
                year_sum1 += acc.account.remain
            elif acc.account in year_acc2:
                year_sum2 += acc.account.remain
            elif acc.account in year_acc3:
                year_sum3 += acc.account.remain
            elif acc.account in year_acc4:
                year_sum4 += acc.account.remain
            elif acc.account in year_acc5:
                year_sum5 += acc.account.remain
            elif acc.account in year_acc6:
                year_sum6 += acc.account.remain

    yearly_savings_sum = [year_sum1, year_sum2, year_sum3, year_sum4, year_sum5, year_sum6]


    return monthly_savings_sum, quarterly_savings_sum, yearly_savings_sum


def bankLoans(bank_name, year):
    """
    calculate loans sum of one bank
    """
    # -- monthly loans sum -- #
    jan_sum = 0
    feb_sum = 0
    mar_sum = 0
    apr_sum = 0
    may_sum = 0
    jun_sum = 0
    jul_sum = 0
    aug_sum = 0
    sep_sum = 0
    oct_sum = 0
    nov_sum = 0
    dec_sum = 0

    jan_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=1)
    feb_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=2)
    mar_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=3)
    apr_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=4)
    may_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=5)
    jun_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=6)
    jul_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=7)
    aug_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=8)
    sep_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=9)
    oct_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=10)
    nov_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=11)
    dec_pay = Payment.objects.filter(pay_date__year=year, pay_date__month=12)

    if jan_pay.count():
        for pay in jan_pay:
            if pay.loan.bank.bank_name == bank_name:
                jan_sum += pay.pay_amount
    if jan_pay.count():
        for pay in feb_pay:
            if pay.loan.bank.bank_name == bank_name:
                feb_sum += pay.pay_amount
    if jan_pay.count():
        for pay in mar_pay:
            if pay.loan.bank.bank_name == bank_name:
                mar_sum += pay.pay_amount
    if jan_pay.count():
        for pay in apr_pay:
            if pay.loan.bank.bank_name == bank_name:
                apr_sum += pay.pay_amount
    if jan_pay.count():
        for pay in may_pay:
            if pay.loan.bank.bank_name == bank_name:
                may_sum += pay.pay_amount
    if jan_pay.count():
        for pay in jun_pay:
            if pay.loan.bank.bank_name == bank_name:
                jun_sum += pay.pay_amount
    if jan_pay.count():
        for pay in jul_pay:
            if pay.loan.bank.bank_name == bank_name:
                jul_sum += pay.pay_amount
    if jan_pay.count():
        for pay in aug_pay:
            if pay.loan.bank.bank_name == bank_name:
                aug_sum += pay.pay_amount
    if jan_pay.count():
        for pay in sep_pay:
            if pay.loan.bank.bank_name == bank_name:
                sep_sum += pay.pay_amount
    if jan_pay.count():
        for pay in oct_pay:
            if pay.loan.bank.bank_name == bank_name:
                oct_sum += pay.pay_amount
    if jan_pay.count():
        for pay in nov_pay:
            if pay.loan.bank.bank_name == bank_name:
                nov_sum += pay.pay_amount
    if jan_pay.count():
        for pay in dec_pay:
            if pay.loan.bank.bank_name == bank_name:
                dec_sum += pay.pay_amount

    monthly_loans_sum = [jan_sum, feb_sum, mar_sum, apr_sum, may_sum, jun_sum,
                         jul_sum, aug_sum, sep_sum, oct_sum, nov_sum, dec_sum]

    # -- quarterly loans sum -- #
    q1_sum = 0
    q2_sum = 0
    q3_sum = 0
    q4_sum = 0

    q1_start = datetime.date(year, 1, 1)
    q1_end = datetime.date(year, 3, 31)
    q2_start = datetime.date(year, 4, 1)
    q2_end = datetime.date(year, 6, 30)
    q3_start = datetime.date(year, 7, 1)
    q3_end = datetime.date(year, 9, 30)
    q4_start = datetime.date(year, 10, 1)
    q4_end = datetime.date(year, 12, 31)

    q1_pay = Payment.objects.filter(pay_date__range=(q1_start, q1_end))
    q2_pay = Payment.objects.filter(pay_date__range=(q2_start, q2_end))
    q3_pay = Payment.objects.filter(pay_date__range=(q3_start, q3_end))
    q4_pay = Payment.objects.filter(pay_date__range=(q4_start, q4_end))

    if q1_pay.count():
        for pay in q1_pay:
            if pay.loan.bank.bank_name == bank_name:
                q1_sum += pay.pay_amount
    if q2_pay.count():
        for pay in q2_pay:
            if pay.loan.bank.bank_name == bank_name:
                q2_sum += pay.pay_amount
    if q3_pay.count():
        for pay in q3_pay:
            if pay.loan.bank.bank_name == bank_name:
                q3_sum += pay.pay_amount
    if q4_pay.count():
        for pay in q4_pay:
            if pay.loan.bank.bank_name == bank_name:
                q4_sum += pay.pay_amount

    quarterly_loans_sum = [q1_sum, q2_sum, q3_sum, q4_sum]

    # -- annual loans sum -- #
    year_sum1 = 0
    year_sum2 = 0
    year_sum3 = 0
    year_sum4 = 0
    year_sum5 = 0
    year_sum6 = 0
    
    year_pay1 = Payment.objects.filter(pay_date__year=2015)
    year_pay2 = Payment.objects.filter(pay_date__year=2016)
    year_pay3 = Payment.objects.filter(pay_date__year=2017)
    year_pay4 = Payment.objects.filter(pay_date__year=2018)
    year_pay5 = Payment.objects.filter(pay_date__year=2019)
    year_pay6 = Payment.objects.filter(pay_date__year=2020)

    if year_pay1.count():
        for pay in year_pay1:
            if pay.loan.bank.bank_name == bank_name:
                year_sum1 += pay.pay_amount
    if year_pay2.count():
        for pay in year_pay2:
            if pay.loan.bank.bank_name == bank_name:
                year_sum2 += pay.pay_amount
    if year_pay3.count():
        for pay in year_pay3:
            if pay.loan.bank.bank_name == bank_name:
                year_sum3 += pay.pay_amount
    if year_pay4.count():
        for pay in year_pay4:
            if pay.loan.bank.bank_name == bank_name:
                year_sum4 += pay.pay_amount
    if year_pay5.count():
        for pay in year_pay5:
            if pay.loan.bank.bank_name == bank_name:
                year_sum5 += pay.pay_amount
    if year_pay6.count():
        for pay in year_pay6:
            if pay.loan.bank.bank_name == bank_name:
                year_sum6 += pay.pay_amount

    yearly_loans_sum = [year_sum1, year_sum2, year_sum3, year_sum4, year_sum5, year_sum6]


    return monthly_loans_sum, quarterly_loans_sum, yearly_loans_sum


def checkDup(client_id, cnted):
    """
    exclude counted clients while calculating
    """
    sum = 0
    cli = client_id.split(' ')
    for client in cli:
        if client not in cnted:
            sum += 1
            cnted.append(client)
        else: continue
    return sum


def bankClients(bank_name, year):
    """
    calculate clients sum of one bank
    """
    # -- monthly clients sum -- #
    jan_sum = 0
    feb_sum = 0
    mar_sum = 0
    apr_sum = 0
    may_sum = 0
    jun_sum = 0
    jul_sum = 0
    aug_sum = 0
    sep_sum = 0
    oct_sum = 0
    nov_sum = 0
    dec_sum = 0

    jan_acc = Account.objects.filter(open_date__year=year, open_date__month=1)
    feb_acc = Account.objects.filter(open_date__year=year, open_date__month=2)
    mar_acc = Account.objects.filter(open_date__year=year, open_date__month=3)
    apr_acc = Account.objects.filter(open_date__year=year, open_date__month=4)
    may_acc = Account.objects.filter(open_date__year=year, open_date__month=5)
    jun_acc = Account.objects.filter(open_date__year=year, open_date__month=6)
    jul_acc = Account.objects.filter(open_date__year=year, open_date__month=7)
    aug_acc = Account.objects.filter(open_date__year=year, open_date__month=8)
    sep_acc = Account.objects.filter(open_date__year=year, open_date__month=9)
    oct_acc = Account.objects.filter(open_date__year=year, open_date__month=10)
    nov_acc = Account.objects.filter(open_date__year=year, open_date__month=11)
    dec_acc = Account.objects.filter(open_date__year=year, open_date__month=12)

    bank_acc = ClientAcc.objects.filter(bank=Bank.objects.get(bank_name=bank_name))

    jan_cnted = []
    feb_cnted = []
    mar_cnted = []
    apr_cnted = []
    may_cnted = []
    jun_cnted = []
    jul_cnted = []
    aug_cnted = []
    sep_cnted = []
    oct_cnted = []
    nov_cnted = []
    dec_cnted = []

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in dec_acc:
                dec_sum += checkDup(acc.client.client_id, dec_cnted)
            elif acc.account in nov_acc:
                nov_sum += checkDup(acc.client.client_id, nov_cnted)
            elif acc.account in oct_acc:
                oct_sum += checkDup(acc.client.client_id, oct_cnted)
            elif acc.account in sep_acc:
                sep_sum += checkDup(acc.client.client_id, sep_cnted)
            elif acc.account in aug_acc:
                aug_sum += checkDup(acc.client.client_id, aug_cnted)
            elif acc.account in jul_acc:
                jul_sum += checkDup(acc.client.client_id, jul_cnted)
            elif acc.account in jun_acc:
                jun_sum += checkDup(acc.client.client_id, jun_cnted)
            elif acc.account in may_acc:
                may_sum += checkDup(acc.client.client_id, may_cnted)
            elif acc.account in apr_acc:
                apr_sum += checkDup(acc.client.client_id, apr_cnted)
            elif acc.account in mar_acc:
                mar_sum += checkDup(acc.client.client_id, mar_cnted)
            elif acc.account in feb_acc:
                feb_sum += checkDup(acc.client.client_id, feb_cnted)
            elif acc.account in jan_acc:
                jan_sum += checkDup(acc.client.client_id, jan_cnted)

    monthly_clients_sum = [jan_sum, feb_sum, mar_sum, apr_sum, may_sum, jun_sum,
                           jul_sum, aug_sum, sep_sum, oct_sum, nov_sum, dec_sum]

    # -- quarterly clients sum -- #
    q1_sum = 0
    q2_sum = 0
    q3_sum = 0
    q4_sum = 0

    q1_start = datetime.date(year, 1, 1)
    q1_end = datetime.date(year, 3, 31)
    q2_start = datetime.date(year, 4, 1)
    q2_end = datetime.date(year, 6, 30)
    q3_start = datetime.date(year, 7, 1)
    q3_end = datetime.date(year, 9, 30)
    q4_start = datetime.date(year, 10, 1)
    q4_end = datetime.date(year, 12, 31)

    q1_acc = Account.objects.filter(open_date__range=(q1_start, q1_end))
    q2_acc = Account.objects.filter(open_date__range=(q2_start, q2_end))
    q3_acc = Account.objects.filter(open_date__range=(q3_start, q3_end))
    q4_acc = Account.objects.filter(open_date__range=(q4_start, q4_end))

    bank_acc = ClientAcc.objects.filter(bank=Bank.objects.get(bank_name=bank_name))

    q1_cnted = []
    q2_cnted = []
    q3_cnted = []
    q4_cnted = []

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in q1_acc:
                q1_sum += checkDup(acc.client.client_id, q1_cnted)
            elif acc.account in q2_acc:
                q2_sum += checkDup(acc.client.client_id, q2_cnted)
            elif acc.account in q3_acc:
                q3_sum += checkDup(acc.client.client_id, q3_cnted)
            elif acc.account in q4_acc:
                q4_sum += checkDup(acc.client.client_id, q4_cnted)
        
    quarterly_clients_sum = [q1_sum, q2_sum, q3_sum, q4_sum]

    # -- annual clients sum -- #
    year_sum1 = 0
    year_sum2 = 0
    year_sum3 = 0
    year_sum4 = 0
    year_sum5 = 0
    year_sum6 = 0

    year_acc1 = Account.objects.filter(open_date__year=2015)
    year_acc2 = Account.objects.filter(open_date__year=2016)
    year_acc3 = Account.objects.filter(open_date__year=2017)
    year_acc4 = Account.objects.filter(open_date__year=2018)
    year_acc5 = Account.objects.filter(open_date__year=2019)
    year_acc6 = Account.objects.filter(open_date__year=2020)

    bank_acc = ClientAcc.objects.filter(bank=Bank.objects.get(bank_name=bank_name))

    year_cnted1 = []
    year_cnted2 = []
    year_cnted3 = []
    year_cnted4 = []
    year_cnted5 = []
    year_cnted6 = []

    if bank_acc.count():
        for acc in bank_acc:
            if acc.account in year_acc1:
                year_sum1 += checkDup(acc.client.client_id, year_cnted1)
            elif acc.account in year_acc2:
                year_sum2 += checkDup(acc.client.client_id, year_cnted2)
            elif acc.account in year_acc3:
                year_sum3 += checkDup(acc.client.client_id, year_cnted3)
            elif acc.account in year_acc4:
                year_sum4 += checkDup(acc.client.client_id, year_cnted4)
            elif acc.account in year_acc5:
                year_sum5 += checkDup(acc.client.client_id, year_cnted5)
            elif acc.account in year_acc6:
                year_sum6 += checkDup(acc.client.client_id, year_cnted6)

    yearly_clients_sum = [year_sum1, year_sum2, year_sum3, year_sum4, year_sum5, year_sum6]


    return monthly_clients_sum, quarterly_clients_sum, yearly_clients_sum


def search(request):
    """
    display statistics charts
    """
    if request.method == 'POST':
        search_by_year = request.POST.get("search_by_year")
        year = int(search_by_year)

        # -- savings -- #
        A_month_sav, A_quarter_sav, A_year_sav = bankSavings('A', year)
        B_month_sav, B_quarter_sav, B_year_sav = bankSavings('B', year)
        C_month_sav, C_quarter_sav, C_year_sav = bankSavings('C', year)
        D_month_sav, D_quarter_sav, D_year_sav = bankSavings('D', year)
        E_month_sav, E_quarter_sav, E_year_sav = bankSavings('E', year)

        # -- loans -- #
        A_month_loan, A_quarter_loan, A_year_loan = bankLoans('A', year)
        B_month_loan, B_quarter_loan, B_year_loan = bankLoans('B', year)
        C_month_loan, C_quarter_loan, C_year_loan = bankLoans('C', year)
        D_month_loan, D_quarter_loan, D_year_loan = bankLoans('D', year)
        E_month_loan, E_quarter_loan, E_year_loan = bankLoans('E', year)

        # -- Clients -- #
        A_month_client, A_quarter_client, A_year_client = bankClients('A', year)
        B_month_client, B_quarter_client, B_year_client = bankClients('B', year)
        C_month_client, C_quarter_client, C_year_client = bankClients('C', year)
        D_month_client, D_quarter_client, D_year_client = bankClients('D', year)
        E_month_client, E_quarter_client, E_year_client = bankClients('E', year)
        
        print('success')

        return render(request, 'banksys/statistics/charts.html',
                        {"A_month_sav": A_month_sav, "A_quarter_sav": A_quarter_sav, "A_year_sav": A_year_sav,
                         "B_month_sav": B_month_sav, "B_quarter_sav": B_quarter_sav, "B_year_sav": B_year_sav,
                         "C_month_sav": C_month_sav, "C_quarter_sav": C_quarter_sav, "C_year_sav": C_year_sav,
                         "D_month_sav": D_month_sav, "D_quarter_sav": D_quarter_sav, "D_year_sav": D_year_sav,
                         "E_month_sav": E_month_sav, "E_quarter_sav": E_quarter_sav, "E_year_sav": E_year_sav,
                         "A_month_loan": A_month_loan, "A_quarter_loan": A_quarter_loan, "A_year_loan": A_year_loan,
                         "B_month_loan": B_month_loan, "B_quarter_loan": B_quarter_loan, "B_year_loan": B_year_loan,
                         "C_month_loan": C_month_loan, "C_quarter_loan": C_quarter_loan, "C_year_loan": C_year_loan,
                         "D_month_loan": D_month_loan, "D_quarter_loan": D_quarter_loan, "D_year_loan": D_year_loan,
                         "E_month_loan": E_month_loan, "E_quarter_loan": E_quarter_loan, "E_year_loan": E_year_loan,
                         "A_month_client": A_month_client, "A_quarter_client": A_quarter_client, "A_year_client": A_year_client,
                         "B_month_client": B_month_client, "B_quarter_client": B_quarter_client, "B_year_client": B_year_client,
                         "C_month_client": C_month_client, "C_quarter_client": C_quarter_client, "C_year_client": C_year_client,
                         "D_month_client": D_month_client, "D_quarter_client": D_quarter_client, "D_year_client": D_year_client,
                         "E_month_client": E_month_client, "E_quarter_client": E_quarter_client, "E_year_client": E_year_client,})
    else:
        return render(request, 'banksys/statistics/search.html')
