from django.shortcuts import render, redirect
from .models import Message, Comment
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	context={
	'messages':Message.objects.all(),
	'comments':Comment.objects.all()
	}
	return render(request, 'comments/index.html', context)

def new(request):
	if 'id' in request.session:
		if request.method == 'POST':
			print request.session['id']
			try:
				message = Message.objects.create(content=request.POST['content'], user_id=request.session['id'])
				print message
				return redirect('/comments')
			except:
				return redirect('/comments')

		else:
			return redirect('/comments')
	else:
		return redirect(reverse('users:	welcome'))

def add(request, id):
	if 'id' in request.session:
		if request.method == 'POST':
			print "message",id
			try:
				comment = Comment.objects.create(content=request.POST['content'], user_id=request.session['id'], message_id=id)
				return redirect('/comments')
			except:
				return redirect('/comments')

		else:
			return redirect('/comments')
	else:
		return redirect(reverse('users:	welcome'))


def delete(request, id):
	if 'id' in request.session:
		if request.method == 'POST':
			print request.session['id']
			try:
				message = Message.objects.get(id=id)
				message.delete()
				print message
				return redirect('/comments')
			except:
				return redirect('/comments')

		else:
			return redirect('/comments')
	else:
		return redirect(reverse('users:	welcome'))	
			