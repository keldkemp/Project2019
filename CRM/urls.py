from django.urls import path, include
from django.contrib.auth import views as auth_views

from CRM.views import auth


auth_urlpatterns = ([
    path('', auth.CrmLoginRedirectView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='CRM/auth/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        'redirect/',
        auth.CrmLoginRedirectView.as_view(),
        name='login-redirect'
    ),
], 'accounts')

urlpatterns = [
    path('', auth.CrmLoginRedirectView.as_view()),
    path('accounts/', include(auth_urlpatterns)),
]
