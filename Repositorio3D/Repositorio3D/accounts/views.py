from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class PerfilUsuario(TemplateView):
    template_name = "accounts/perfil.html"


# contrario de loginrequired
class RegistrarUsuario(RegistrationView):
    form_class = RegistrationFormUniqueEmail
