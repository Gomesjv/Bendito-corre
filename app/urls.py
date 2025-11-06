from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tenis.views import NewTenisView, TenisListView, TenisDetailView, TenisUpdateView, DeleteTenisView
from accounts.views import login_view, logout_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tenis/', TenisListView.as_view(), name='tenis_list'),
    path('new_tenis/', NewTenisView.as_view(), name='new_tenis'),
    path('tenis/<int:pk>/', TenisDetailView.as_view(), name='tenis_detail'),
    path('tenis/<int:pk>/update/', TenisUpdateView.as_view(), name='tenis_update'),
    path('tenis/<int:pk>/delete/', DeleteTenisView.as_view(), name='tenis_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)