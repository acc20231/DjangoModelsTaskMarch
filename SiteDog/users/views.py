from django.contrib.auth.views import LoginView

from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 form = LoginUserForm()
#     form = LoginUserForm()
#
#     return render(request, 'users/login.html', {'form': form})

# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))
