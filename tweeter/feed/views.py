
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import View

from .decorators import authenticated_user, unauthenticated_user
from .forms import loginForm, signupForm

# Create your views here.


@method_decorator([unauthenticated_user(redirect_to="/"), ], name='dispatch')
class registerView(View):
    def get(self, request, *args, **kwargs):
        form = signupForm()
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        pass


@method_decorator([never_cache, unauthenticated_user(redirect_to="/"), ], name='dispatch')
class loginView(View):

    def get(self, request, *args, **kwargs):
        form = loginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = loginForm()
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next = request.GET.get('next')
            if next:
                return redirect(next)

            return redirect("feed")
        else:
            context = {
                'status': 'error',
                'message': 'Credenciais inválidas',
                'form': form
            }

        return render(request, 'login.html', context)


@method_decorator([authenticated_user(redirect_to="/login"), ], name="dispatch")
class logoutUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("feed")


class feedView(View):
    def get(self, request, *args, **kwargs):
        login_form = loginForm()
        signup_form = signupForm()
        context = {
            "login_form": login_form,
            "signup_form": signup_form,
        }
        return render(request, "feed.html", context)
