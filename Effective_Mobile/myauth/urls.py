from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LoginUser,
                    AboutMeView,
                    logout_view,
                    RegisterUser,
                    UsersListView,
                    UserDetail,
                    ProfileUpdate,
                    GroupViewSet,
                    UserViewSet,

)


app_name = "myauth"

routers = DefaultRouter()
routers.register("groups", GroupViewSet)
routers.register("users", UserViewSet)

urlpatterns = [
    path("api/", include(routers.urls)),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path('register/', RegisterUser.as_view(), name='register'),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user_detail"),
    path("user/<int:pk>/update", ProfileUpdate.as_view(), name="profile_update"),

]