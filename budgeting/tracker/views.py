from django.shortcuts import render
from .models import *
from .forms import ExpensesForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
    "title":"Home"
    }
    return render(request,"index.html",context)

def get_all_expenses(request):
    latest_expense = Expenses.objects.all()
    context={
    "title":"Expenses",
    'latest_expense':latest_expense
    }
    return render(request,"expenses.html",context)

def get_filtered_expenses(request,cat):
    filtered_expenses=Expenses.objects.filter(category__exact=cat)
    context={
    "title":"Category Expenses",
    "filtered_expenses":filtered_expenses,
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
