from django.shortcuts import render, redirect
from .models import Commercial, Vote, Adpost
from django.core.urlresolvers import reverse

def index(request):
	context={
	'commercials':Commercial.objects.all(),
	# 'votes':Commercial.objects.votes.all(),
	'adposts':Adpost.objects.all()
	}
	# User.objects.message_set.all()
	print "COUNT"
	print Commercial.votes
	print "Votes"
	print Vote.objects.all()
	return render(request, 'commercials/index.html', context)


def new(request):
	if 'id' in request.session:
		if request.method == 'POST':
			commercial = Commercial.objects.create(title=request.POST['title'],company=request.POST['company'],
				youtube=request.POST['youtube'], category=request.POST['category'],rhetoric=request.POST['rhetoric'],efficacy=request.POST['efficacy'])
			if commercial:
				vote = Vote.objects.create(user_id=request.session['id'],commercial=commercial)
				if request.POST['adpost'] != "":
					adpost = Adpost.objects.create(content=request.POST['adpost'],user_id=request.session['id'],commercial=commercial)
			return redirect('/commercials')

def vote(request, id):
	if 'id' in request.session:
		if request.method == 'POST':
			vote = Vote.objects.create(user_id=request.session['id'],commercial_id=id)
			return redirect('/commercials')
		else:
			return redirect('/commercials')
	else:
		return redirect('/')

def adpost(request, id):
	if 'id' in request.session:
		if request.method == 'POST':
			adpost = Adpost.objects.create(content=request.POST['content'],user_id=request.session['id'],commercial_id=id)
			return redirect('/commercials')
		else:
			return redirect('/commercials')
	else:
		return redirect('/')