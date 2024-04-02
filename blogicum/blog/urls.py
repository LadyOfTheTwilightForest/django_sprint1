from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]

# from django.conf.urls.static import static
# from blogicum import settings

# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
