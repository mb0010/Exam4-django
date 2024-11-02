from django import forms
from .models import Category, User, Question, Answer

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'image', 'phone_number']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'category', 'user', 'image', 'file', 'is_active']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'description', 'question', 'user', 'image', 'file', 'is_active']
