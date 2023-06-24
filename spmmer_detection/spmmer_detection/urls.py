"""spmmer_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from spmmer_detection import settings
from Tweet_Server import views as tweetserver
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', remoteuser.login, name="login"),


    url(r'^Register/$', remoteuser.Register, name="Register"),

    url(r'^Post_Tweet/$', remoteuser.Post_Tweet, name="Post_Tweet"),
    url(r'^Review/(?P<pk>\d+)/$', remoteuser.Review, name="Review"),
    url(r'^ViewAllTweets/$', remoteuser.ViewAllTweets, name="ViewAllTweets"),
    url(r'^Viewreviews/$', remoteuser.Viewreviews, name="Viewreviews"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^dislikes/(?P<pk>\d+)/$', remoteuser.dislikes, name="dislikes"),
    url(r'ViewTrending/$', remoteuser.ViewTrending, name="ViewTrending"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),

    url(r'^tweetserverlogin/$',tweetserver.tweetserverlogin, name="tweetserverlogin"),
    url(r'View_Remote_Users/$',tweetserver.View_Remote_Users,name="View_Remote_Users"),
    url(r'ViewTrendings/$',tweetserver.ViewTrendings,name="ViewTrendings"),
    url(r'^charts/(?P<chart_type>\w+)', tweetserver.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', tweetserver.dislikeschart,name="dislikeschart"),
    url(r'^Viewalltweets/$', tweetserver.Viewalltweets, name='Viewalltweets'),
    url(r'^View_Spam_Analysis/$', tweetserver.View_Spam_Analysis, name='View_Spam_Analysis'),
    url(r'^View_Spam_Reviews/$', tweetserver.View_Spam_Reviews, name="View_Spam_Reviews"),
    url(r'^View_User_Reviews/$', tweetserver.View_User_Reviews, name='View_User_Reviews'),
    url(r'^View_Spam_Users/$', tweetserver.View_Spam_Users, name='View_Spam_Users'),
    url(r'^View_Fake_Users/$', tweetserver.View_Fake_Users, name='View_Fake_Users'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
