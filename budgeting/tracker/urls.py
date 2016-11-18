from django.conf.urls import url

#namespacing: to be used with site's urls.py
app_name = 'tracker'

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^expenses/add/$',views.add_expense,name='add_expense'),
    url(r'^expenses/$',views.get_all_expenses,name='get_all_expenses'),
    url(r'^expenses/(?P<cat>[a-z]+)/',views.get_filtered_expenses,name='get_filtered_expenses'),
]
