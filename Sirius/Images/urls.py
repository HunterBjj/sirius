from os import path
from django.conf import settings
from django.conf.urls.static import static
from Sirius.Images import views

urlpatterns = [
                  path('', views.auth, name='auth'),  # Страница входа.
                  path('viewBirds.html/', views.viewBirds, name='viewBirds'),  # Представление птиц.
                  path('creatBirds.html/', views.creatBirds, name='creatBirds'),  # Создание птиц.
                  path('creatUser.html/', views.rgstrUser, name='rgstrUser'),  # Создание пользователя.
                  path('viewUser.html/', views.viewUser, name='viewUser'),  # Просмотренные птицы.
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)