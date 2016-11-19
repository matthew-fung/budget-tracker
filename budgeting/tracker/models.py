from django.db import models

# Create your models here.
class Expenses(models.Model):
    ID = models.AutoField(primary_key=True)
    log_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    amount = models.DecimalField(max_digits=8,decimal_places = 2)
    category = models.CharField(max_length=100)
    item = models.CharField(max_length = 75, default='item')

    class Meta:
        ordering = ['-log_date']

    def __str__(self):
        output = "{0}: {1}, {2}, {3}".format(self.log_date,self.ID,self.category,self.amount)
        return output

    # def get_expenses(self,category):
    #     spent = self.category
    #
    #     output = "For {0}: you spent ${1}".format(self.category,self.amount)
    #     return output


class Revenues(models.Model):
    ID = models.AutoField(primary_key=True)
    log_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    amount = models.DecimalField(max_digits=8,decimal_places = 2)
    category = models.CharField(max_length=100)

    def __str__(self):
        output = "{0}: {1}, {2}, {3}".format(self.log_date,self.ID,self.category,self.amount)
        return output
