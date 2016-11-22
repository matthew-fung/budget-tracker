from django.shortcuts import render
from .models import *
from .forms import ExpensesForm, SelectForm, QuickAddForm
from django.shortcuts import redirect
from django.db.models import Sum


# Create your views here.
def index(request):
    context = {
    "title":"Home"
    }
    return render(request,"index.html",context)

def get_all_expenses(request):
    if request.method == "POST":
        addForm = ExpensesForm(request.POST)
        if addForm.is_valid():
            addForm.save()

        cat=request.POST.get('category')
        return redirect('tracker:get_filtered_expenses',cat=cat)
    else:
        addForm = ExpensesForm()
        latest_expense = Expenses.objects.all()
        running_total = Expenses.objects.aggregate(Sum('amount'))
        categories = Expenses.objects.order_by().values('category').distinct()
        context={
        'title':'All Expenses',
        'latest_expense':latest_expense,
        'addForm':addForm,
        'running_total':running_total,
        'categories':categories,
        }
    return render(request,"expenses.html",context)

def get_filtered_expenses(request,cat):
    if request.method == "POST":
        form = QuickAddForm(request.POST)
        if form.is_valid():
            form.category = request.POST['category']
            form.save()
            #return redirect('tracker:get_all_expenses')
        cat=request.POST.get('category')
        return redirect('tracker:get_filtered_expenses',cat=cat)
    else:
        filtered_expenses=Expenses.objects.filter(category__exact=cat)
        running_total = Expenses.objects.filter(category__exact=cat).aggregate(Sum('amount'))
        quickAddForm = QuickAddForm()
        categories = Expenses.objects.order_by().values('category').distinct()
        context={
        'title':'Category Expenses',
        'filtered_expenses':filtered_expenses,
        'running_total':running_total,
        'quickAddForm':quickAddForm,
        'categories':categories,
        }
    return render(request,"filtered_expenses.html",context)

def add_expense(request):
    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_all_expenses')

    else:
        form = ExpensesForm()
        context={
        "title": "Add Expense",
        "form":form
        }
    return render(request,"add_expenses.html",context)
