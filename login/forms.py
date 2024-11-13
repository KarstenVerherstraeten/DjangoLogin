from django import forms
from django.contrib.auth.models import User, Group
from .models import Task

class CustomRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, empty_label="Select a group")  # Dropdown for groups
    password = forms.CharField(widget=forms.PasswordInput, required=True)  # Set password field with PasswordInput widget

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password

        if commit:
            user.save()
            # Add user to the selected group
            selected_group = self.cleaned_data['group']
            user.groups.add(selected_group)
        return user
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
    
    def save(self, commit=True):
        task = super().save(commit=False)
        
        if commit:
            task.save()
        return task