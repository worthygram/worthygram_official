from django.urls import path
from . import views




app_name = "blog"




urlpatterns = [
    path('', views.home_view, name='home'),
    path('users',views.users,name='users'),
    path("certificates",views.certificates,name="certificates"),
    path("gratitude_or_note",views.gratitude_or_note,name="gratitude_or_note"),
    path('stories/',views.stories_home,name='stories'),
    path('stories/<slug:slug>/',views.story_detail_view,name='story-detail'),
    path('exercises/',views.exercise_home,name='exercises'),
    path('exercises/<slug:slug>/',views.exercise_detail_view,name='exercise-detail'),
    path('p/<slug:slug>/',views.post_detail_view,name='post-detail'),  
    path('post/new/',views.post_create_view,name='post-create'),
    path('post/<int:pk>/update/', views.post_update_view, name='post-update'),  
    path('post/<int:pk>/delete/',views.post_delete_view, name='post-delete'), 
    path('search/', views.search_view, name='search'), 
    path('like/post/<slug:slug>',views.like_post,name='like_post'),
    path('like/story/<slug:slug>',views.like_story,name='story_post'),
    path('report/post/',views.post_report_view,name='report'),
    path('report/user/',views.user_report_view,name='report-user'),
    # path('<str:username>/notifications/',views.notifications_view,name='notifications'),
    # path('<str:username>/notifications/update/',views.notifications_update_view,name='notifications-update'),
    # path('<str:username>/notifications/count/',views.notifications_unread_count_view,name='notifications-count'),
]

