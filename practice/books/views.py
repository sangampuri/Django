from django.shortcuts import redirect, render,get_object_or_404
from .models import Book
from .forms import BookForm
# Create your views here.
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST) # creates a form with populated data
        if form.is_valid:
            form.save()

    else:
        form = BookForm()

    return render(request,'books/book_create.html',{'form':form})

def book_read(request):
    books = Book.objects.all()
    return render(request,'books/book_read.html',{'books':books})

def book_update(request,book_id):
    book = get_object_or_404(Book,id = book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid:
            form.save()
            return redirect('book_read')

    else:
        form = BookForm(instance=book)

    return render(request,'books/book_create.html',{'form':form})

def book_delete(request,book_id):
    book = get_object_or_404(Book, id = book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_read')

    else:
        return render(request,'books/delete_confirmation.html',{'book':book})

