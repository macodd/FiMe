from django.shortcuts import render, redirect

from .forms import VisitForm
from .models import Visit


def visit_create_view(request):
    context = {}
    form = VisitForm(request.POST or None)
    if form.is_valid():
        visit_obj = form.save(commit=False)
        visit_obj.patient = request.patient
        visit_obj.save()
        return redirect('visit/create/')
    context['form'] = form
    return render(request, 'visit/create.html', context)


def visit_list_view(request):
    context = {}
    visit_list = Visit.objects.all()
    context['visit_list'] = visit_list
    return render(request, 'visit/list.html', context)
