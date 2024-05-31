from django.shortcuts import render


# Create your views here.
# from django.shortcuts import render
# from . form import book_form
# def book_create(request):
#     form = book_form()
#     return render(request, 'books/book_form.html', {'form': form})
   
from django.shortcuts import render, redirect
from .form import GoogleFormForm

def GoogleForm_create(request):
    if request.method == 'POST':
        form = GoogleFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Googleforms')  # Redirect to a view that lists Googleforms or any other page
    else:
        form = GoogleFormForm()
    return render(request, 'GoogleForm_form.html', {'form': form})

# Create your views here.
