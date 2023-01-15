from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import Course


@login_required
def order_home(request, username):
    return render(request, 'order/order_home.html', {'username': username})


@login_required
def order_form(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Order Has Been Placed")
            return redirect('order:order_form')
        else:
            messages.error(request, "Couldn't Place the Order")
            return redirect('order:order_form')
    return render(request, 'order/order_form.html', {'form': form})


def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    return render(request, 'order/course_dropdown_list_options.html', {'courses': courses})
