from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.models import Profile


def users(request,userName):
    #displayname = User.objects.all() 
    usersname = User.objects.get(username = userName)
    # userInfo = User.objects.all().filter(username=abc)
    prof_pic = Profile.objects.all().first()

    context = {
        'userinfo':usersname,
        'prof': prof_pic.image
    }
    return render(request, "accounts/profiles.html", context)


