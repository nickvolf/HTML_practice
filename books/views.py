from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Book, Unit
from .forms import BookCreateForm, UnitCreateForm


def book_list_view(request):
    book_list = Book.objects.all()
    return render(request, 'books/book_list.html', {"book_list": book_list})


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {"book": book})


def book_create_view(request):
    if request.method == "POST":
        form = BookCreateForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookCreateForm()
        return render(request, 'books/book_create.html', {"form": form})


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookCreateForm()
        return render(request, 'books/book_update.html', {"form": form, "book": book})


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')
    else:
        return render(request, 'books/book_delete.html', {"book": book})


def unit_detail_view(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    return render(request, 'books/unit_detail.html', {"unit": unit})


def unit_create_view(request):
    if request.method == "POST":
        form = UnitCreateForm(request.POST)
        if form.is_valid():
            unit = form.save()
            return redirect('book-detail', pk=unit.book.pk)
    else:
        form = UnitCreateForm()
        return render(request, 'books/unit_create.html', {"form": form})


def unit_update_view(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == "POST":
        form = BookCreateForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit-detail', pk=unit.pk)
    else:
        form = BookCreateForm()
        return render(request, 'books/unit_update.html', {"form": form, "unit": unit})


def unit_delete_view(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    book = unit.book
    if request.method == "POST":
        unit.delete()
        return redirect('book-detail', pk=book.pk)
    else:
        return render(request, 'books/unit_delete.html', {"unit": unit})