from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$',views.profile,name='profile'),
                       url(r'^reviews/$',views.reviews,name='reviews'),
                       url(r'^create_review/$',views.create_review,name='create_review'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/queries/$',views.queries,name='queries'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/create_query/$',views.create_query,name='create_query'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/create_query/advquery/(?P<query_string>[\w\(\)\%\ \,]+)/$',views.check_API_adv,name='adv_query'),
                       # url(r'^reviews/(?P<review_name_slug>[\w\-]+)/query_results/$',views.query_results,name='query_results'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/abstract_pool/$',views.abstract_pool,name='abstract_pool'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/document_pool/$',views.document_pool,name='document_pool'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/final_pool/$',views.final_pool,name='final_pool'),
                       url(r'^login/$',views.user_login,name='login_register'),
                       url(r'^logout/$',views.user_logout,name='logout'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/$', views.review, name='review'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/queries/(?P<id>\d+)/delete_query/$',views.delete_query,name='delete_query'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/abstract_pool/(?P<id>\d+)/add_to_dp/$',views.add_to_dp,name='add_to_dp'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/document_pool/(?P<id>\d+)/remove_from_dp/$',views.remove_from_dp,name='remove_from_dp'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/document_pool/(?P<id>\d+)/add_to_fp/$',views.add_to_fp,name='add_to_fp'),
                       url(r'^reviews/(?P<review_name_slug>[\w\-]+)/final_pool/(?P<id>\d+)/remove_from_fp/$',views.remove_from_fp,name='remove_from_fp'),
                      )

