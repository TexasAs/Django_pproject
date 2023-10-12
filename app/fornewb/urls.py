from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from .views import *

from django.conf import settings
from django.conf.urls.static import static


router = SimpleRouter()
router.register(r"api", FornewbViewSet)     # http://127.0.0.1:8000/api/?format=json

urlpatterns = ([
    path('', FornewbHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutuser, name='logout'),
    path('user_account/', useraccount, name='user_account'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', FornewbCategory.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) + router.urls

