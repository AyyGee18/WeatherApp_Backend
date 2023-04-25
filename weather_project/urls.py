"""weather_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_app import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='1.0.0',
        description="API documentation of App"
    ),
    # public=True
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name="swagger_schema"),

    path('admin/', admin.site.urls),

    path('continentsAll/', views.ContinentListAll.as_view()),

    path('continents/<str:continent_name>/',
         views.ContinentList.as_view({'get': 'list'})),

    path('continents/<str:continent_name>/<str:conutry_name>/',
         views.ContinentList.as_view({'get': 'retrieve'})),

    path('continents/<str:continent_name>/<str:conutry_name>/<str:city_name>/',
         views.ContinentList.as_view({'get': 'retrieve'})),

    path('countries/', views.CountryList.as_view()),
    path('cities/', views.CityList.as_view()),
    path('weather/', views.WeatherList.as_view()),
    path('', views.home, name="home")
    # path('continents/', views.get_continent, name="get_continent")
]
