from django.forms import ModelForm
from .models import Project
from django import forms
from django.contrib.auth.models import User
from registration.models import UserDashboard


class ProjectForm(ModelForm):
    all_executors = UserDashboard.get_all_executors()
    executors = forms.ModelMultipleChoiceField(queryset=all_executors, widget=forms.CheckboxSelectMultiple(),
                                               label="Wybierz wykonawców", required=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'executors']
