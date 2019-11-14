from django.conf.urls import url, include

from user import views

urlpatterns = [
    # basic api's
    url(r'^signup/$', views.UserCreate.as_view(), name='account-create'),
    url(r'^signin/$', views.UserLogin.as_view(), name='account-login'), #using authtoken django
    url(r'^profile/$', views.Profile.as_view(), name='account-login'), #using authtoken django
    url(r'^profile/update/$', views.UpdateProfile.as_view(), name='account-login'), #using authtoken django


]
