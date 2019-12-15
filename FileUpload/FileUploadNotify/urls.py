from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from FileUploadNotify.main import views


urlpatterns = [
    path('', views.FileListView.as_view(), name='home'),

    path('files/<int:pk>/', views.delete_file, name='delete_file'),

    path('files/', views.FileListView.as_view(), name='file_list'),
    path('files/notifications/', views.NotificationListView, name='notifications'),
    path('files/upload/', views.FileUploadView.as_view(), name='upload_file'),
    path('files/update/<int:pk>/', views.FileUpdateview.as_view(), name='update_file'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
