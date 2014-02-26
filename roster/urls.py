from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='roster_home'),
	url(r'^mentor/$', views.mentorList, name='roster_mentor_list'),
	url(r'^member/$', views.memberList, name='roster_member_list'),
	url(r'^mentor/(?P<pk>\d+)$', views.mentor, name='roster_mentor'),
	url(r'^member/(?P<pk>\d+)$', views.member, name='roster_member'),
	)
