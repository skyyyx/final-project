from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/activity/', views.ActivityList.as_view()),
    path('api/activity/<int:pk>/', views.ActivityList.as_view()),
    path('api/user/', views.UserAccountList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
