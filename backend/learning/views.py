from django.shortcuts import render
from .models import Lesson

def lessons_list(request):
    lessons = Lesson.objects.all().order_by('title')
    return render(request, 'learning/lessons_list.html', {'lessons': lessons})
