from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from testapp.models import Question

class addQuestionform(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"