from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from core.models import AboutMe, QuestionAnswer
from core.forms import StartProjectFaForm, ContactForm, StartProjectEnForm


class HomeFaView(TemplateView):
    template_name = 'index_fa.html'
    start_project_form = StartProjectFaForm
    contact_form = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['me'] = AboutMe.get_info()
        context['project_form'] = self.start_project_form(initial={"form_name": 'project_form'})
        context['contact_form'] = self.contact_form()
        return context

    def get_form_class(self):
        form_name = self.request.POST.get('form_class')
        if form_name:
            if form_name == 'project_form':
                return self.start_project_form
            elif form_name == 'contact_form':
                return self.contact_form
        return None

    def post(self, request):
        form_class = self.get_form_class()
        if form_class:
            form = form_class(data=request.POST)
            if form.is_valid():
                form.save()
        return redirect('core:home_fa')


class HomeEnView(TemplateView):
    template_name = 'index_en.html'
