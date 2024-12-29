from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
@staff_member_required
def administrator(request):
    title = 'Panel de administrador'
    return render(request, 'administrator/administrator.html', {
        'title':title
    })