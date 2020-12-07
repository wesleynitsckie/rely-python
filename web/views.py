from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from base.models import Transaction
import json
from django.shortcuts import redirect
from .forms import RelyForm

def index(request):
    #del request.session['transaction_id']
    # if this is the initial POST then let trigger the job
    if request.method == 'POST':
        form = RelyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Create a Transaction so that we can keep track of the process
            blob = {
                "first_name":form.cleaned_data["first_name"],
                "last_name" : form.cleaned_data["last_name"],
                "income": form.cleaned_data["income"],
                "dob": form.cleaned_data["dob"].strftime("%Y-%m-%d"),
            }
            transaction = Transaction.objects.create(transaction_blob=json.dumps(blob))
            transaction.save()
            request.session['transaction_id'] = str(transaction.id)
            messages.success(request, 'Your information will now be checked. This process will take a while. Please click the "Check Status" button to see the progress of you application')
            return redirect(transaction.status +'/' + str(transaction.id))
        else:
            messages.error(request, 'An Error occurred with your submission. Please check your form')
            return render(request, 'index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        transaction_id = request.session.get('transaction_id', False)
        print(transaction_id)
        if transaction_id is not False:
            print('transaction found ..redirecting')
            transaction = Transaction.objects.get(id=transaction_id)
            return redirect('/' +transaction.status +'/' + str(transaction_id))
        else:
            form = RelyForm()

    return render(request, 'index.html', {'form': form})

def sc(request, id):
    transaction = Transaction.objects.get(id=id)
    if transaction.status !=Transaction.Status.SANCTIONCHECK :
        return redirect('/' +transaction.status +'/' + str(id))
    return render(request, 'sc.html', {'transaction': transaction})
    
def scc(request, id):
    transaction = Transaction.objects.get(id=id)
    return render(request, 'scc.html', {'transaction': transaction})

def pc(request, id):
    transaction = Transaction.objects.get(id=id)
    if transaction.status != Transaction.Status.PEPCHECK :
        return redirect('/' +transaction.status +'/' + str(id))
    return render(request, 'pc.html', {'transaction': transaction})

def deny(request, id):
    del request.session['transaction_id']
    Transaction.objects.filter(id=id).update(
                status=Transaction.Status.DENIED
            )
    return render(request, 'denied.html')

def pep_check(request, id):
    transaction = Transaction.objects.get(id=id)
    transaction.status = Transaction.Status.PEPCHECK
    transaction.save()
    return redirect('/PC/' + str(id))
    
def pcc(request, id):
    transaction = Transaction.objects.get(id=id)
    if transaction.status != Transaction.Status.PEPCHECKCOMPLETED :
        return redirect('/' +transaction.status +'/' + str(id))
    return render(request, 'pcc.html', {'transaction': transaction})

def pcc_confirm(request, id, confirm):
    transaction = Transaction.objects.get(id=id)
    if confirm == 1:
        transaction.confirm_on_pep_list = True
    else:
        transaction.confirm_on_pep_list = False
    transaction.status = Transaction.Status.ASSESSMENT
    transaction.save()
    # The assessment should kick off in the background. Meanwhile we can wait by the 
    # assessment page
    return redirect('/AS/' + str(id))

def assessment(request, id):
    transaction = Transaction.objects.get(id=id)
    if transaction.status != Transaction.Status.ASSESSMENT :
        return redirect('/' +transaction.status +'/' + str(id))
    return render(request, 'as.html', {'transaction': transaction})

def accepted(request, id):
    del request.session['transaction_id']
    transaction = Transaction.objects.get(id=id)
    return render(request, 'accepted.html', {'transaction': transaction})