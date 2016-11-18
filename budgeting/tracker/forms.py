from django.forms import ModelForm
from .models import Expenses, Revenues

class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ('amount', 'category', 'item')
