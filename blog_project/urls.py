from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from blog.views import read_file

admin.site.site_header = settings.ADMIN_SITE_HEADER

from blog.sitemap import PostSitemap,StorySitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

sitemaps = {
    'blog': PostSitemap,
    'story':StorySitemap,
}


urlpatterns = i18n_patterns(
    path(_('admin/site/'), admin.site.urls), 
    path('rosetta/', include('rosetta.urls')),  # NEW
    path('', include('blog.urls', namespace='blog')), 
    path('account/register/', user_views.register, name='register'),
    path('account/profile-update/',user_views.updateProfile,name='profile-update'),
    path('account/follow-unfollow/<int:pk>/',user_views.userFollowUnfollow,name="follow-unfollow"),
    path('account/password-change/', user_views.change_password, name='change-password'),

    path('account/login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'), 
    path('account/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),  
    path('account/password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),  
    path('account/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),  
    path('account/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),  
    path('account/password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),  
    path('account/community/', include('footer.urls', namespace='community')),
    path('<str:username>/', user_views.profile, name='profile'),
  
    
)

htmx_urlpatterns = [
    path('',include('pwa.urls')),
    path('.well-known/assetlinks.json',read_file),
    path('robots.txt', TemplateView.as_view(template_name='blog/partials/robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
   
    
    path('validate_username/', user_views.validate_username,name='validate-username'),
    path('validate_email/', user_views.validate_email,name='validate-email'),
]

urlpatterns += htmx_urlpatterns
    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'footer.views.error_404_view'