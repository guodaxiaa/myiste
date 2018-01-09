from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext,loader
def index(request):
    last_question_list=Question.objects.order_by('-pub_date')[:5]
    template =loader.get_template('/polls/index.html')
    context = {
        'last_question_list':last_question_list,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
def detail(request,question_id):
    return HttpResponse("You're loking at question %s."% question_id)
def results(request,question_id):
    response="you're looking at the results of question %s"
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you're voting on question %s." %question_id)