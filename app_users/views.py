from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from app_users.forms import RegistrationForm
from app_users.models import Profile


class RegistrationView(generic.edit.CreateView):

    """
    Представление для регистрации нового пользователя.
    При правильном заполнении всех полей формы, происходит создание
    объекта класса Profile, связанного отношением 1 к 1 с моделью User.
    Таким образом проиходит расширение модели User и сохранение профиля в БД.
    """

    template_name = 'app_users/registration_form.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm

    def form_valid(self, form):

        """
        Переопределение метода проверки валидности формы.
        Добавление логики раширения модели User.
        """

        form = RegistrationForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            surname = form.cleaned_data.get('surname')
            phone_numb = form.cleaned_data.get('phone_numb')
            email = form.cleaned_data.get('phone_numb')
            if self.request.FILES:
                avatar = self.request.FILES['avatar']
                Profile.objects.create(
                    user=user, phone_numb=phone_numb, email=email, surname=surname, avatar=avatar,
                    first_name=first_name, last_name=last_name
                )
            else:
                Profile.objects.create(
                    user=user, phone_numb=phone_numb, email=email, surname=surname,
                    first_name=first_name, last_name=last_name
                )
            return super(RegistrationView, self).form_valid(form)


class Login(LoginView):

    """Представление для авторизации пользователя."""

    template_name = 'app_users/login_form.html'


class Logout(LogoutView):

    """Представление для выхода из учетной записи пользователем."""

    next_page = '/app_cripto/main_paige/'


