from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from commons.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегистрированы!'
    title = 'Store - Регистрация'

    
    
class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'
    def get_success_url(self):
        return reverse_lazy('users:profile', args = (self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    class EmailVerificationView(TitleMixin, TemplateView):
        title = 'Store - Подтверждение электронной почты'
        template_name = 'users/email_verification.html'
    
        def get(self, request, *args, **kwargs):
            code = kwargs['code']
            user = User.objects.get(email = kwargs['email'])
            email_verifications = EmailVerification.objects.filter(user = user, code = code)
            if email_verifications.exists() and not email_verifications.first().is_expired():
                user.is_verified_email = True
                user.save()
                return super(EmailVerificationView, self).get(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('index'))
    # def get(self, request, *args, **kwargs):
    #     code = kwargs['code']
    #     user = User.objects.get(email = kwargs['email'])
    #     email_verifications = EmailVerification.objects.filter(user = user, code = code)
    #     if email_verifications.exists():
    #         user.is_verified_email = True
    #         user.save()
    #         return super(EmailVerification, self).get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseRedirect(reverse('index'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


    
    