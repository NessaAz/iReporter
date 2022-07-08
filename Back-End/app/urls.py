from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('api/admin',views.AdminSignUpView.as_view()),
    path('api/client',views.ClientSignUpView.as_view()),
    path('api/token',views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/flaglists', views.flags_list, name='flaglist'),
    path('api/interventions', views.interventions_list, name='interventions'),
    path('api/raiseflag/<int:id>/', views.flag_detail, name='flag'),
    path('api/intervationrequest/<int:id>/', views.intervention_detail, name='intervationrequest'),
    path('api/adminprofiles', views.admins_list, name='admins'),
    path('api/clientsprofiles', views.clients_list, name='clients'),
    path('api/admins/<int:id>/', views.admin_detail, name='admin'),
    path('api/clients/<int:id>/', views.client_detail, name='client'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
