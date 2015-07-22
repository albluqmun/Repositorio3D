from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class PerfilUsuario(LoginRequiredMixin, TemplateView):
    template_name = "accounts/perfil.html"


# contrario de loginrequired
class RegistrarUsuario(RegistrationView):
    form_class = RegistrationFormUniqueEmail
