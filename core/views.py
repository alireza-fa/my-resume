from django.views.generic.base import TemplateView


class HomeFaView(TemplateView):
    template_name = 'index_fa.html'


class HomeEnView(TemplateView):
    template_name = 'index_en.html'

