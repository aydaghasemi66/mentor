from django.shortcuts import render,redirect
from .models import Category, Course , Comment, Reply
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from course.forms import CommentForm,ReplyForm
from root.forms import NewsLetterForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def courses(request,cat=None, trainer=None):
    category = Category.objects.all()
    if cat:
        courses = Course.objects.filter(category__title=cat,status=True)
    elif trainer:
        courses = Course.objects.filter(teacher__info__username=trainer,status=True)
    elif request.GET.get('search'):
        courses = Course.objects.filter(content__contains=request.GET.get('search')) 
    else:
        courses = Course.objects.filter(status=True)
    paginator = Paginator(courses, 3)  
    first_page = 1
    last_page = paginator.num_pages  

    try:
        page_number = request.GET.get('page')
        courses = paginator.get_page(page_number)     
    except EmptyPage:
        courses = paginator.get_page(1)
    except PageNotAnInteger:
        courses = paginator.get_page(1)

    context= {
        'courses': courses,
        'category': category,
        'first_page': first_page,
        'last_page': last_page,
        'page_number': page_number,
    }
    return render(request, 'course/courses.html',context=context)

def course_detail(request, id):
    if request.method=="GET":
        try:
            courses=Course.objects.get(id=id)
            comments = Comment.objects.filter(which_course=id, status=True)
            comment_count=Comment.objects.filter(status=True,which_course=id).count()
            reply = Reply.objects.filter(status=True)
            courses.counted_views+=1
            id_list=[]
            coursess=Course.objects.filter(status=True)
            for cr in coursess:
                id_list.append(cr.id)

            if len(id_list) > 1:
                if id_list[0] == id:
                    next_course = Course.objects.get(id=id_list[1])
                    previous_course = None
                elif id_list[-1] == id:
                    previous_course = Course.objects.get(id=id_list[-2])
                    next_course = None
                else:
                    current_index = id_list.index(id)
                    if current_index + 1 < len(id_list):
                        next_course = Course.objects.get(id=id_list[current_index + 1])
                    if current_index - 1 >= 0:
                        previous_course = Course.objects.get(id=id_list[current_index - 1])
            elif len(id_list) == 1:
                next_course = None
                previous_course = None

            context= {
                'courses': courses,
                'comment_count': comment_count,
                'next_course': next_course,
                'previous_course': previous_course,
                'comments': comments,
                'reply':reply,
                }
            return render(request, 'course/course-details.html',context=context)
        except:
           return render(request, 'course/404.html')
    elif request.method=="POST" and len(request.POST)>2:
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'yor comment submited and publish as soon')
            return redirect(request.path_info)
        else:
            messages.add_message(request,messages.ERROR,'yor comment data is not valid')
            return redirect(request.path_info)
        
    elif request.method == 'POST' and len(request.POST) == 2:
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect(request.path_info)   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect(request.path_info)
@login_required
def reply(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        form = ReplyForm()

        context = {
            'comment' : comment,
            'form' : form,
        }
        return render(request,'course/reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            cid = comment.which_course.id
            return redirect (f'/courses/course-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect (request.path_info)

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_course.id
    comment.delete()
    return redirect (f'/courses/course-detail/{cid}')

@login_required
def delete_reply(request, id):
    reply = Reply.objects.get(id=id)
    rid = reply.which_comment.id
    reply.delete()
    return redirect (f'/courses/course-detail/{rid}')

@login_required
def edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        

        context = {
            'comment' : comment,
        }
        return render(request,'course/edit.html',context=context)
    
    elif request.method == 'POST' :
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            cid = comment.which_course.id
            return redirect (f'/courses/course-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect (request.path_info)

@login_required
def edit_reply(request, id):
    reply = Reply.objects.get(id=id)
    if request.method == 'GET':
        

        context = {
           'reply' : reply,
        }
        return render(request,'course/edit_reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST,instance=reply)
        if form.is_valid():
            form.save()
            rid = reply.which_comment.id
            return redirect (f'/courses/course-detail/{rid}')
        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect (request.path_info)
        

@api_view()
def apitest(request):
    return Response({
        'name':'test'
    })