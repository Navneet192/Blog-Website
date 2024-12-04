from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'blog'

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    path('api/login/', views.login_view, name='api_login'),
    path('api/logout/', views.logout_view, name='api_logout'),
    
    # Regular URLs
    path('', views.PostListView.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
