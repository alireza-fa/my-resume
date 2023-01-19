from django import forms

from core.models import StartProject, Project, Contact, ProjectEn


class StartProjectFaForm(forms.ModelForm):
    subject = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={"class": 'my-select'}), required=True)

    class Meta:
        model = StartProject
        fields = ('name', 'phone_number', 'email', 'message')

    def save(self, commit=True):
        cd = self.cleaned_data
        start_project = StartProject(
            name=cd['name'], phone_number=cd['phone_number'], email=cd['email'],
            subject=cd['subject'], message=cd['message']
        )
        if commit:
            start_project.save()
        return start_project


class StartProjectEnForm(StartProjectFaForm):
    subject = forms.ModelChoiceField(
        queryset=ProjectEn.objects.all(),
        widget=forms.Select(attrs={"class": 'my-select'}), required=True)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname', 'phone_number', 'email', 'subject', 'message')
