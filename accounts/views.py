from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView, TemplateView, FormView
from betterforms.multiform import MultiModelForm

from .forms import MedicRegister, FimeUserCreationForm


class MedicCreationForm(MultiModelForm):
    form_classes = {"medic_form": MedicRegister, "user_form": FimeUserCreationForm}


class MedicRegisterView(FormView):
    template_name = "account/signup.html"
    form_class = MedicCreationForm

    def form_valid(self, form):
        fime_user = form["user_form"].save()
        medic_user = form["medic_form"].save(commit=False)
        medic_user.user = fime_user
        medic_user.save()
        return redirect("accounts:success")


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "account/login.html"

    def get_success_url(self):
        return redirect("dashboard:home")


class UserLogoutView(LogoutView):
    template_name = "account/logout.html"


class RegistrationSuccessView(TemplateView):
    template_name = "account/success.html"
