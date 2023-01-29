from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdmissionForm
from .models import Student

guidelines_verified = False
form_submitted = False

def home(request):
    return render(request, 'pentagon/home.html')

def guidelines(request):
    return render(request, 'pentagon/guidelines.html')

def guidelines_verify(request):
    global guidelines_verified
    try:
        if request.POST['agree']:
            guidelines_verified = True
            return redirect('pentagon:admission_form')
    except:
        guidelines_verified = False
        return render(request, 'pentagon/guidelines.html', {
            'error_message':'Please Select "I Agree" to continue. '
        })

def admission_form(request):
    global guidelines_verified
    global form_submitted

    if guidelines_verified:
        context = {}

        form = AdmissionForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form_submitted = True
            name = request.POST['first_name']
            father = request.POST['father_name']
            if Student.objects.filter(first_name=name, father_name=father): # If student name and father name already exists then the form is not saved once again.
                return redirect('pentagon:already_exists')
            else:
                form.save()
                return redirect('pentagon:acknowledgement')

        context['form'] = form
        return render(request, 'pentagon/admission_form.html', context)
    else:
        return redirect('pentagon:guidelines')

def acknowledgement(request):
    global form_submitted
    if form_submitted:
        return render(request, 'pentagon/acknowledgement.html')
    else:
        return redirect('pentagon:admission_form')

def already_exists(request):
    global form_submitted
    if form_submitted:
        return render(request, 'pentagon/already_exists.html')
    else:
        return redirect('pentagon:admission_form')