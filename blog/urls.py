from django.urls import path
from blog import views

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/details/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/draft/', views.PostDraftView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]
