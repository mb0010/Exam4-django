from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, User, Question, Answer
from .form import CategoryForm, UserForm, QuestionForm, AnswerForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category-list')
    return render(request, 'category_confirm_delete.html', {'category': category})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user-list')
    return render(request, 'user_confirm_delete.html', {'user': user})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('question-list')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question-list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question_form.html', {'form': form})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('question-list')
    return render(request, 'question_confirm_delete.html', {'question': question})


def answer_list(request):
    answers = Answer.objects.all()
    return render(request, 'answer_list.html', {'answers': answers})

def answer_create(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('answer-list')
    else:
        form = AnswerForm()
    return render(request, 'answer_form.html', {'form': form})

def answer_update(request, pk):
    answer = Answer.objects.get(pk=pk)  
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES, instance=answer) 
        if form.is_valid():
            form.save() 
            return redirect('answer-list') 
    else:
        form = AnswerForm(instance=answer) 
    return render(request, 'answer_form.html', {'form': form})  
def answer_delete(request, pk):
    answer = Answer.objects.get(pk=pk)  
    if request.method == 'POST':
        answer.delete() 
        return redirect('answer-list')  
    return render(request, 'answer_confirm_delete.html', {'answer': answer}) 

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  
