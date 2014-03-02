from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from roster.models import Member, Mentor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.http import HttpResponse
# Create your views here.

def home(request):
	context = {
		'member_count': Member.objects.count(),
		'mentor_count': Mentor.objects.count(),
	}
	return render(request, 'roster/home.html', context)

def mentor(request, pk):
	#mentor = Mentor.objects.order_by('?')[0]
	mentor = get_object_or_404(Mentor, id=pk)
	return render(request, "roster/mentor.html", {'mentor': mentor})

def member(request, pk):
	#member = Member.objects.order_by('?')[0]
	member = get_object_or_404(Member, id=pk)	
	return render(request, "roster/member.html", {'member': member})

def memberList(request):
	member_list = Member.objects.all()
	paginator = Paginator(member_list, 25)
	page = request.GET.get('page')
	try:
		members= paginator.page(page)
	except PageNotAnInteger:
		members = paginator.page(1)
	except EmptyPage:
		members = paginator.page(paginator.num_pages)

	return render(request, 'roster/member_list.html', {"members": members})

def mentorList(request):
	mentor_list = Mentor.objects.all()
	paginator = Paginator(mentor_list, 25)
	page = request.GET.get('page')
	try:
		mentors = paginator.page(page)
	except PageNotAnInteger:
		mentors = paginator.page(1)
	except EmptyPage:
		mentors = paginator.page(paginator.num_pages)

	return render(request, 'roster/mentor_list.html', {"mentors": mentors})
