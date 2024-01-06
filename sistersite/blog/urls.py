from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_detail')
]
