from django.shortcuts import render
from principal.models import Post, UserProfile
from principal.forms import UserForm, UserProfileForm, PostForm, PictureForm, DogForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):

    points = Post.objects.all()
    return render(request, 'index.html', {'points': points})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_data(request):
    current = request.user
    if UserProfile.objects.filter(user=current).exists():
        return index(request)
        data = ''
    else:
        registered = False
        if request.method == 'POST':
            data = UserProfileForm(data=request.POST)
            if data.is_valid():
                details = data.save(commit=False)
                details.user = request.user
                details.save()
                return index(request)
            else:
                print data.errors
        else:
            data = UserProfileForm()
    return render(request, 'details.html', {'data': data, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/principal/')
            else:
                return HttpResponse("You account is disabled")
        else:
            print "invalid login details: {0}, {1}".format(username, password)
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'login.html', {})


@login_required
def publish(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        dog_form = DogForm(data=request.POST)
        picture_form = PictureForm(data=request.POST)
        if post_form.is_valid() and dog_form.is_valid():
            post = post_form.save(commit=False)
            post.user_post = request.user
            post.save()
            dog = dog_form.save(commit=False)
            dog.post_dog = post
            dog.save()
            picture = picture_form.save(commit=False)
            if 'picture' in request.FILES:
                picture.picture = request.FILES['picture']
            picture.post_picture = post
            picture.save()
            return index(request)
        else:
            print post_form.errors, dog_form.errors, post_form
    else:
        post_form = PostForm()
        dog_form = DogForm()
        picture_form = PictureForm()
    return render(request,
                  'publish.html',
                  {'post_form': post_form, 'dog_form': dog_form, 'picture_form': picture_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/principal/')
