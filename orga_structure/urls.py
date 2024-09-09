from django.urls import path, include
from .views import get_orga_sturcture ,create_orga_member,crud_orga, make_logic


urlpatterns = [
    path("",get_orga_sturcture, name="get_orga_sturcture"),
    path("create/",create_orga_member, name="create_orga_member"),
    path("do/<int:pk>",crud_orga, name="update_orga"),
    path("logic/",make_logic, name="make_logic"),


]
