from django.conf.urls import url, include

from Repositorio3D.accounts.views import PerfilUsuario, RegistrarUsuario

urlpatterns = [
    url(r'^profile/$', PerfilUsuario.as_view(), name='account_profile'),
    url(r'^register/$', RegistrarUsuario.as_view(), name='registration_register'),
    url(r'', include('registration.backends.default.urls')),
]
