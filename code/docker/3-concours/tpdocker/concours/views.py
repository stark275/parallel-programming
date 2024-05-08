from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .tasks import add 
import django.contrib.sessions

# Create your views here.
def index(request):

    my_task_id = request.session.get('my_task_id')
    if not my_task_id:
        my_task_id = '0'

    return render(request, "concours/index.html",{
        'my_task_id': my_task_id
    })

def evaluate(request):
    if request.method == 'POST':
        print("Form Sent")
        my_task = add.delay(4,6)
        request.session['my_task_id'] = my_task.id

    return HttpResponseRedirect(reverse("concours:index"))

@api_view(['GET'])
def get_task_result(request, task_id):
    my_task_id = task_id
    print(my_task_id)
    my_task = None

    if my_task_id == None :
        return Response({'result': None})
    else:
        my_task = add.AsyncResult(my_task_id)

    if my_task.ready():
        return Response({'result': my_task.result})
   
    return Response({'result': my_task.result})
