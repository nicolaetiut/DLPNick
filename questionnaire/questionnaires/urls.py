from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('questionnaires.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^(?P<quest_id>\d+)/$', 'start'),
    url(r'^(?P<quest_id>\d+)/(?P<page_id>\d+)/validate/$', 'validate'),
    url(r'^(?P<quest_id>\d+)/(?P<page_id>\d+)/$', 'go_to_page'),
    url(r'^(?P<quest_id>\d+)/results/$', 'results'),
)
