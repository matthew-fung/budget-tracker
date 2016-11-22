from django.forms import ModelForm
from .models import Expenses, Revenues

class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ('amount', 'category', 'item')

class SelectForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ('category',)

class QuickAddForm(ModelForm):
    class Meta:
        model=Expenses
        fields=('amount','category','item')
