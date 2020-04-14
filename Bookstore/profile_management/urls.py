from django.urls import path
from . import views

app_name = 'profile_management'

urlpatterns = [
	path('userprofile/', views.home, name = 'userProfile-home'),
	#path('about/', views.about, name = 'userProfile-about'),
	path('signup/', views.signup, name = 'userProfile-signup'),
	path('addcreditcard/', views.addcreditcard, name = 'userProfile-addcreditcard'),
	path('addshippingaddress/', views.addshippingaddress, name = 'userProfile-addshippingaddress'),
	path('signin/', views.signin, name = 'userProfile-signin'),
	path('changepassword/', views.changepassword, name = 'userProfile-changepassword')
]