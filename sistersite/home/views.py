from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'author.html'

class AboutProfessView(TemplateView):
    template_name = 'profess.html'

class AboutTeamView(TemplateView):
    template_name = 'team.html'    

class AboutTeachingView(TemplateView):
    template_name = 'teaching.html'
    