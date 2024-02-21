from django.urls import path, include

urlpatterns = [
    path('careers/', include('careers.urls')),
]
