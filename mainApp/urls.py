from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('download', DownloadPageView.as_view(), name='download'),
    # path('errors/', Errors.as_view(), name = 'errors')

]