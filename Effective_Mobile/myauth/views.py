from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


from .forms import RegisterUserForm, ProfileAvatarForm, ProfileUserForme
from .models import ProfileUser
from .serializers import GroupSerializer, UserSerializer


class GroupViewSet(ModelViewSet):
    """
    Набор представлений для действий над Group.
    Полный CRUD для сущностей групп.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(ModelViewSet):
    """
    Набор представлений для действий над User.
    Полный CRUD для сущностей user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AboutMeView(LoginRequiredMixin, UpdateView):
    model = ProfileUser
    form_class = ProfileAvatarForm
    template_name_suffix = "_update_avatar_form"
    success_url = reverse_lazy("myauth:about-me")

    def get_object(self, queryset=None):
        print(f" текущий пользователь {self.request.user.profileuser.pk}\n {self.request.user}")
        print(f"object {ProfileUser.objects}")
        return self.request.user.profileuser


class LoginUser(LoginView):
    """
    Класс реализующий вход в систему
    """
    form_class = AuthenticationForm
    template_name = "myauth/login.html"
    redirect_authenticated_user = True


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))


class RegisterUser(CreateView):
    """
    Класс, реализующий регистрацию пользователя
    с вводом имени, фамилии, email, пароля, повтор пароля
    и вход в систему
    """
    form_class = RegisterUserForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        print(username)
        password = form.cleaned_data.get("password1")
        ProfileUser.objects.create(
            user=self.object,
            name=form.cleaned_data.get("first_name"),
            surname=form.cleaned_data.get("last_name"),
            email=form.cleaned_data.get("email"), avatar='avatar_default.png')

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class UsersListView(LoginRequiredMixin, ListView):
    """
    Класс реализующий вывод списпа пользователей
    """
    template_name = "myauth/users_list.html"
    queryset = User.objects.select_related().all()
    context_object_name = "users"


class UserDetail(LoginRequiredMixin, DetailView):
    """
    Класс реализующий вывод информации о пользователе
    """
    template_name = "myauth/user_detail.html"
    queryset = User.objects.select_related().prefetch_related().all()
    context_object_name = "user"


class ProfileUpdate(UserPassesTestMixin, UpdateView):
    """
    Класс реализующий изменение информации о пользоаптеле
    """
    def test_func(self):
        return (self.request.user.is_superuser
                or self.request.user.pk == self.get_object().user.pk)

    model = ProfileUser
    template_name_suffix = "_update_form"
    form_class = ProfileUserForme

    def get_success_url(self):
        return reverse(
            "myauth:user_detail",
            kwargs={"pk": self.object.user.pk},
        )
