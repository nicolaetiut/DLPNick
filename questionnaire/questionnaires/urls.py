from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('questionnaires.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^(?P<quest_id>\d+)/$', 'start'),
    url(r'^(?P<quest_id>\d+)/(?P<page_id>\d+)/$', 'go_to_page'),
    url(r'^(?P<quest_id>\d+)/results/$', 'results'),
    
    #url(r'^$',
    #    ListView.as_view(
    #        queryset=Questionnaire.objects.order_by('creation_date')[:5],
    #        context_object_name='latest_quests',
    #        template_name='index.html')),
    #url(r'^(?P<pk>\d+)/$',
    #    DetailView.as_view(
    #        model=Questionnaire,
    #        template_name='start.html')),
    #url(r'^(?P<quest_id>\d+)/(?P<pk>\d+)/$',
    #    DetailView.as_view(
    #        model=Page,
    #        template_name='go_to_page.html')),
    #url(r'^(?P<pk>\d+)/results/$',
    #    DetailView.as_view(
    #        model=Page,
    #        template_name='results.html'),
    #    name='poll_results'),
)
