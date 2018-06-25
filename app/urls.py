"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
# from rest_framework import routers
from helpers.no_put_router import NoPutRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from . import views

# main modules
from unit.api.views import UnitViewset
from user.api.views import UserViewset,ProfileViewset
from courses.api.views import CourseViewSet
from curiculum.api.views import CuriculumViewSet
from section.api.views import SectionViewSet

# change admin page title
admin.site.site_header = 'Teachable Admin'

swagger_view = get_swagger_view(title='Teachable API')

# router = routers.DefaultRouter()
router = NoPutRouter()

# main routers
router.register('unit', UnitViewset)

#Related TO user
router.register("user", UserViewset)
router.register("profile",ProfileViewset)

router.register("courses", CourseViewSet)
router.register("curiculum", CuriculumViewSet)
router.register("section", SectionViewSet)


urlpatterns = [
    path('', swagger_view),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/authentication/', obtain_jwt_token),
    path('api/version/', views.version),
]
