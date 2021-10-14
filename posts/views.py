from userposts.models import UserMessages, UserPosts
from django.shortcuts import redirect, render
from .models import Category
from accounts.models import UserRanks
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Profile

# Create your views here.

def newPost(request,ctgUrl):
    catgoryUrl = Category.objects.get(categoryName =ctgUrl)
    
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            form.instance.category = catgoryUrl
            form.save()

            messages.add_message(request, messages.SUCCESS, "Your post has been successfully published")
                        

            total_messages_post = Profile.objects.get(user = request.user)
            total_messages_post.total_post +=1
            total_messages_post.save()
            
            returnPost =  UserPosts.objects.get(id = form.instance.id)
            returnPost.last_message = form.instance.created_at
            returnPost.last_message_username = form.instance.username
            returnPost.save()
            catgoryUrl.totalPost += 1 
            catgoryUrl.save()

            user_update = UserRanks.objects.get(user_id = request.user.id)
            user_update.score += 3
            user_update.save()
            return redirect("detail",returnPost.id)
    
    else:
        form = PostForm()

    context = {
        'form': form,
        'category':catgoryUrl
    }
    return render(request,"newPost.html", context)
