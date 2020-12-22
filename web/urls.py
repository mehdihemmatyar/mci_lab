from django.urls import path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense , name = 'submit_expense'),
    path('submit/income/', views.submit_income , name = 'submit_income'),
    path('accounts/register/', views.register, name='register'),
    path('q/show',views.show, name='show'),
    path('resetpassword',views.resetpassword, name='resetpassword'),
    path('charts-show',views.chartsshow, name='charts-show'),
    path('accounts/login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path('showdb', views.showdb, name='showdb'),
    path('train', views.train, name='train'),
    path('test', views.test, name='test'),
    path('', views.index, name='index'),


]
