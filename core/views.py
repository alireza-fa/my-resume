from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from core.models import AboutMe
from core.forms import StartProjectFaForm, ContactForm, StartProjectEnForm
from blog.models import Post
from blog.forms import NewsletterSubscribeForm, NewsletterSubscribeEnForm


class HomeFaView(TemplateView):
    template_name = 'index_fa.html'
    start_project_form = StartProjectFaForm
    contact_form = ContactForm
    newsletter_form = NewsletterSubscribeForm
    success_url = reverse_lazy('core:home_fa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['me'] = AboutMe.get_info()
        context['project_form'] = self.start_project_form(initial={"form_name": 'project_form'})
        context['contact_form'] = self.contact_form()
        context['newsletter_form'] = self.newsletter_form()
        context['posts_part'] = Post.get_posts_two_part()
        context['posts'] = Post.objects.all()
        return context

    def get_form_class(self):
        form_name = self.request.POST.get('form_class')
        if form_name:
            if form_name == 'project_form':
                return self.start_project_form
            elif form_name == 'contact_form':
                return self.contact_form
            elif form_name == 'newsletter_form':
                return self.newsletter_form
        return None

    def post(self, request):
        form_class = self.get_form_class()
        if form_class:
            form = form_class(data=request.POST)
            if form.is_valid():
                form.save()
        return redirect(self.success_url)


class HomeEnView(HomeFaView):
    template_name = 'index_en.html'
    start_project_form = StartProjectEnForm
    success_url = reverse_lazy('core:home_en')
    newsletter_form = NewsletterSubscribeEnForm
