from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q

from django.http import HttpResponse,JsonResponse,Http404
try:
    from django.utils import simplejson as json
except ImportError:
    import json


from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post, Comment, PostReport,Quotes,Certify,Do,Story_Urls,Story,Exercise,Do_Exercise
# ,Advice,Stories,Certify,Exercise
from users.models import UserReport
from .forms import CommentForm, ReportPostForm,PostForm

import os
from django.conf import settings


from django.views.decorators.gzip import gzip_page




@login_required
@gzip_page

def home_view(request):
    user = request.user
    quotes = Quotes.objects.prefetch_related().all()
    urls = Story_Urls.objects.prefetch_related().all()
    exercise = Exercise.objects.prefetch_related().all()
    do = Do.objects.prefetch_related().all()
    



    if user.is_authenticated:
        follows_users = user.profile.follows.all()
        follows_posts = Post.objects.prefetch_related().filter(author_id__in=follows_users)
        user_posts = Post.objects.prefetch_related().filter(author=user)
        post_list = (follows_posts|user_posts).distinct().order_by('-date_posted')
        users = User.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(post_list, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
                    'posts': posts,
                    'quotes':quotes,
                    'do':do,
                    'urls':urls,
                    'exercise':exercise,
                    'users':users

            }
        return render(request, 'blog/home_1.html', context)
    else:
        return redirect('login')

def users(request):
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request,'blog/no_posts_home.html',context=context)



def read_file(request):
    f = open('.well-known/assetlinks.json','r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content,content_type='application/json')


@gzip_page
def stories_home(request):
    # stories = Story.objects.all()
    stories = Story.objects.prefetch_related().all().order_by('-pk')
    page = request.GET.get('page', 1)
    paginator = Paginator(stories, 5)
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context = {
        'stories':stories
    }

    return render(request,'blog/stories_home.html',context=context)

@gzip_page
def story_detail_view(request,slug=None):
    story = get_object_or_404(Story,slug=slug)

    context = {
        'story':story
    }

    return render(request,'blog/stories_detail.html',context=context)


@gzip_page
def exercise_home(request):
    # stories = Story.objects.all()
    exercise = Do_Exercise.objects.prefetch_related().all().order_by('-pk')
    page = request.GET.get('page', 1)
    paginator = Paginator(exercise, 5)
    try:
        exercise = paginator.page(page)
    except PageNotAnInteger:
        exercise = paginator.page(1)
    except EmptyPage:
        exercise = paginator.page(paginator.num_pages)

    context = {
        'exercises':exercise
    }

    return render(request,'blog/exercise_home.html',context=context)

@gzip_page
def exercise_detail_view(request,slug=None):
    exercise = get_object_or_404(Do_Exercise,slug=slug)

    context = {
        'exercise':exercise
    }

    return render(request,'blog/exercise_detail.html',context=context)







def certificates(request):
    context=Certify.objects.all()
    return render(request,'blog/certificates.html',{'context':context})



@gzip_page
def post_detail_view(request,slug=None):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect('blog:post-detail', slug=post.slug)
    else:
        form = CommentForm()
        report_form = ReportPostForm()
        comments = Comment.objects.filter(post=post).order_by('-id')
        context = {'post':post,'form':form,'comments':comments,'report_form':report_form}

    return render(request,'blog/post_detail1.html',context)

    
@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            ctx = {'url':post.get_absolute_url()}
            return HttpResponse(json.dumps(ctx), content_type='application/json')

    else:
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request,'blog/post_form.html',context)


@login_required
def post_update_view(request,pk):
    post1 = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post1)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            ctx = {'url':post.get_absolute_url()}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
    else:
        post = get_object_or_404(Post,pk=pk)
        form = PostForm(instance = post)
        context = {
            'form': form,
            'post':post,
        }
        return render(request,'blog/post_from_update1.html',context)

@login_required
def post_delete_view(request, pk=None):
    context = {}
    post = get_object_or_404(Post,pk=pk)
    
    if request.method =="POST":
        if post.author == request.user:
            post.delete()
            return redirect('profile', username=request.user.username)
    context = {"post":post}
    return render(request,'blog/post_confirm_delete.html',context)



@login_required
def search_view(request):
    
    message = ""
    post_list = Post.objects.all().order_by('-pk');
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        try:
            search_input = request.POST.get('search')
            result_posts = Post.objects.filter(Q(title__icontains=search_input)|Q(content__icontains=search_input))
            users = User.objects.filter(Q(username__iexact=search_input))

            # first condition : post-0 , users-0
            if result_posts.count() == 0 and users.count() == 0:
                message = "No results found for: " + search_input
                context = {'message':message,'posts':posts,'search_input':search_input}
                return render(request,'blog/search.html',context)

            # second condition : post-yes , users-0
            elif users.count() == 0 and result_posts.count() != 0:
                context = {'result_posts':result_posts,'search_input':search_input,'posts':posts}
                return render(request,'blog/search.html',context)

            # 3rd condition : post-no , users-yes
            elif result_posts.count() == 0 and users.count() > 0:
                context = {'users':users,'posts':posts,'search_input':search_input}
                return render(request,'blog/search.html',context)
            
            # 4th condition : post:yes , user: yes
            else:
                context = {'users':users,'result_posts':result_posts,'posts':posts,'search_input':search_input}
                return render(request,'blog/search.html',context)

        except:
            message = "Unexpected Error Occured!"
            context = {'message':message}
            return render(request,'blog/search.html',context)
    else:
        flag = True
        context = {'posts':posts,'flag':flag}
        return render(request,'blog/search.html',context)

def gratitude_or_note(request):
    return render(request,'blog/notes_or_gratitude.html')


def like_post(request,slug=None):
    if request.method == "POST":
        instance = Post.objects.get(slug=slug)
        # pk = request.POST.get('pk', None)
        # instance = get_object_or_404(Post, pk=pk)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'blog/partials/likes_area.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'blog/partials/likes_area.html', context={'post':instance})

def like_story(request,slug=None):
    if request.method == "POST":
        instance = Story.objects.get(slug=slug)
        # pk = request.POST.get('pk', None)
        # instance = get_object_or_404(Post, pk=pk)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'blog/partials/story_area.html', context={'story':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'blog/partials/story_area.html', context={'story':instance})


@login_required
@require_POST
def like_view(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk', None)
        post = get_object_or_404(Post, pk=pk)

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            like = False
            post_id = '#like'+str(post.id)
        else:
            post.likes.add(user)
            like = True
            post_id = '#like'+str(post.id)
           
    ctx = {'likes_count': post.total_likes,'like':like,'post_id':post_id}
    return HttpResponse(json.dumps(ctx), content_type='application/json')

@login_required
@require_POST
def like_view_story(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk', None)
        post = get_object_or_404(Story, pk=pk)

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            like = False
            post_id = '#like'+str(post.id)
        else:
            post.likes.add(user)
            like = True
            post_id = '#like'+str(post.id)
           
    ctx = {'likes_count': post.total_users,'like':like,'post_id':post_id}
    return HttpResponse(json.dumps(ctx), content_type='application/json')



@login_required
@require_POST
def post_report_view(request):
    if request.method == 'POST':
        pk = request.POST.get('pk',None)
        reason = request.POST.get('reason')
        post=get_object_or_404(Post,pk=pk)
        user=request.user
        report = PostReport(post=post,reason=reason,user=user)
        report.save()

        return HttpResponse('')

@login_required
@require_POST
def user_report_view(request):
    if request.method == 'POST':
        pk = request.POST.get('pk',None)
        reason = request.POST.get('reason')
        reported_user=get_object_or_404(User,pk=pk)
        report = UserReport(reported_user=reported_user,reason=reason,reporting_user=request.user)
        report.save()

        return HttpResponse('')

