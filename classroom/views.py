from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Classroom
from .forms import ClassroomForm, AddStudent, AddBook, RemoveStudent, RemoveBook
from users.models import CustomUser, UserQuiz
from books.models import Book


def class_detail_view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    return render(request, 'classroom/class_detail.html', {"classroom": classroom})


def class_list_view(request):
    class_list = get_list_or_404(Classroom)
    return render(request, 'classroom/class_list.html', {"class_list": class_list})


def add_class_view(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save()
            return redirect('class-detail', pk=classroom.pk)
    else:
        form = ClassroomForm()
        return render(request, 'classroom/create_class.html', {"form": form})


def class_update_view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == "POST":
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('class-detail', pk=classroom.pk)
    else:
        form = ClassroomForm()
        return render(request, 'classroom/class_update.html', {"form": form, "classroom": classroom})


def book_delete_view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == "POST":
        classroom.delete()
        return redirect('class-list')
    else:
        return render(request, 'books/book_delete.html', {"classroom": classroom})


def class_add_students(request, pk):
    if request.method == "POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            classroom = get_object_or_404(Classroom, pk=pk)
            student.classroom.add(classroom)
            student.has_class = True
            student.save()
            for book in classroom.book_set.all():
                for unit in book.unit_set.all():
                    for quiz in unit.quiz_set.all():
                        userquiz = UserQuiz(user=student, quiz=quiz)
                        userquiz.save()
            return redirect('class-detail', pk=pk)
    else:
        form = AddStudent()
        return render(request, 'classroom/add_to_class.html', {"form": form})


def class_remove_students(request, pk):
    if request.method == "POST":
        form = RemoveStudent(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            classroom = get_object_or_404(Classroom, pk=pk)
            student.classroom.remove(classroom)
            student.has_class = False
            for book in classroom.book_set.all():
                for unit in book.unit_set.all():
                    for quiz in unit.quiz_set.all():
                        userquiz= UserQuiz.objects.get(user=student, quiz=quiz)
                        userquiz.delete()
            student.save()
            return redirect('class-detail', pk=pk)
    else:
        form = RemoveStudent()
        return render(request, 'classroom/add_to_class.html', {"form": form})


def class_add_books(request, pk):
    if request.method == "POST":
        form = AddBook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['book']
            classroom = get_object_or_404(Classroom, pk=pk)
            book = get_object_or_404(Book, title=title)
            if book not in classroom.book_set.all():
                book.classroom.add(classroom)
                for student in classroom.customuser_set.all():
                    for unit in book.unit_set.all():
                        for quiz in unit.quiz_set.all():
                            userquiz = UserQuiz(quiz=quiz, user=student)
                            userquiz.save()
            return redirect('class-detail', pk=pk)
    else:
        form = AddBook()
        return render(request, 'classroom/add_to_class.html', {"form": form})


def class_remove_books(request, pk):
    if request.method == "POST":
        form = RemoveBook(request.POST)
        if form.is_valid():
            book = form.cleaned_data.get('book')
            classroom = get_object_or_404(Classroom, pk=pk)
            if book in classroom.book_set.all():
                book.classroom.remove(classroom)
                book.save()
                for student in classroom.customuser_set.all():
                    for unit in book.unit_set.all():
                        for quiz in unit.quiz_set.all():
                            userquiz = student.userquiz_set.get(quiz = quiz)
                            userquiz.delete()
            return redirect('class-detail', pk=pk)
    else:
        form = RemoveBook()
        return render(request, 'classroom/add_to_class.html', {"form": form})
