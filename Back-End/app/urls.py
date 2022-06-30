from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('flaglists', views.flags_list, name='flaglist'),
    path('interventions/', views.interventions_list, name='interventions'),
    path('raiseflag/<int:id>/', views.flag_detail, name='flag'),
    path('intervationrequest/<int:id>/', views.intervention_detail, name='intervationrequest')
]
urlpatterns = format_suffix_patterns(urlpatterns)
