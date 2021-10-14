from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from posts.models import Category
from userposts.models import UserPosts, UserMessages
from accounts.models import Notifications, UserRanks
from django.views import View
from django.core.paginator import Paginator
from .models import Report
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import HttpResponseRedirect, JsonResponse
from .serializers import UserSerailizer
from posts.forms import ContactUsForm

def index(request):
    category = Category.objects.all()
    latest_post = UserPosts.objects.all().order_by("-last_message")
    answers = UserMessages.objects.all()
    rank_news = UserRanks.objects.all()
    answer_count = 0
    for answer in answers:
        for post in latest_post:
            if answer.post_id == post.id:
                answer_count += 1
    context = {
        'category': category,
        "latest_post": latest_post,
        "answers": answers,
        "count": answer_count,
        "rank_news": rank_news
    }
    return render(request, "intro.html", context)


def forums(request, forumname):
    forum = Category.objects.get(categoryName=forumname)
    post2 = UserPosts.objects.all().filter(category=forum.id).order_by(
        "-last_message").filter(category=forum.id)
    post_message = UserMessages.objects.all().order_by('-created_at')
    post3 = UserMessages.objects.all().order_by('-created_at')
    # usersname = User.objects.get(username = abc)
    post12 = UserMessages.objects.filter(username=request.user.id)

    # Set up Paginator
    p = Paginator(post2, 15)
    page = request.GET.get('page')
    pposts = p.get_page(page)
    context = {
        'categoryName': forumname,
        'categoryDescription': forum.Categorydescription,
        "categoryBrand": forum.categoryBrand,
        'posts': post2,
        "post_message": post_message,
        "post3": post3,
        "pposts": pposts,
    }
    return render(request, "_forums.html", context)


class PostNotification(View):
    def get(self, request, notifications_pk, userposts_pk, *args, **kwargs):
        notification = Notifications.objects.get(pk=notifications_pk)
        post = UserPosts.objects.get(pk=userposts_pk)

        if notification.post and notification.notification_type == 2:
            messagesPaginator = UserMessages.objects.all().filter(post_id=notification.post.id)
            pagenumber = int((messagesPaginator.count() / 5) + 1)
            notification.user_has_seen = True
            notification.save()
            return HttpResponseRedirect("/posts/%s?page=%s#%s" % (notification.post.id, pagenumber, notification.comment.id))

        elif notification.comment and notification.notification_type == 2:
            messagesPaginator = UserMessages.objects.all().filter(post_id=notification.comment.post.id)
            pagenumber = int((messagesPaginator.count() / 5) + 1)
            notification.user_has_seen = True
            notification.save()
            return HttpResponseRedirect("/posts/%s?page=%s#%s" % (notification.comment.post.id, pagenumber, notification.comment.id))
        
        elif notification.comment and notification.notification_type == 1:
            messagesPaginator = UserMessages.objects.all().filter(post_id=notification.comment.post.id)
            pagenumber = int((messagesPaginator.count() / 5) + 1)
            notification.user_has_seen = True
            notification.save()
            return HttpResponseRedirect("/posts/%s?page=%s#%s" % (notification.comment.post.id, pagenumber, notification.comment.id))

        notification.user_has_seen = True
        notification.save()
        return redirect("detail", userposts_pk)

def hierarchy(request):
    return render(request, "hierarchy.html")

def categories(request):
    category = Category.objects.all()

    return render(request, "categories.html", {"categories":category})

def reportsMessage(request,id):
    reportM = UserMessages.objects.get(id=id)
    if request.method == "POST":
        getReason = request.POST.get("report")
        if getReason == "1":
            reason = "Nudity"
        elif getReason == "2":
            reason = "False Information"
        elif getReason == "3":
            reason = "Spam"
        elif getReason == "4":
            reason = "Hate Speech"
        elif getReason == "5":
            reason = "Suicide of Self-Injury"
        elif getReason == "6":
            reason = "Harassment"
        elif getReason == "7":
            reason = "Terrorism"
        elif getReason == "8":
            reason = "Violance"
        report = Report.objects.create(to_user=reportM.username, from_user=request.user, comment = reportM,
                                        report = reason, post= reportM.post  )
        report.save()
        messages.add_message(request, messages.SUCCESS, "Thanks for letting us know.")
        return redirect("detail", reportM.post.id)
    else:
        return redirect("detail", reportM.post.id)

def reportPost(request, id):
    reportP = UserPosts.objects.get(id=id)
    if request.method == "POST":
        getReason = request.POST.get("report")
        if getReason == "1":
            reason = "Nudity"
        elif getReason == "2":
            reason = "False Information"
        elif getReason == "3":
            reason = "Spam"
        elif getReason == "4":
            reason = "Hate Speech"
        elif getReason == "5":
            reason = "Suicide of Self-Injury"
        elif getReason == "6":
            reason = "Harassment"
        elif getReason == "7":
            reason = "Terrorism"
        elif getReason == "8":
            reason = "Violance"
        report = Report.objects.create(to_user=reportP.username, from_user=request.user,
                                        report = reason, post= reportP  )
        report.save()
        messages.add_message(request, messages.SUCCESS, "Thanks for letting us know.")
        return redirect("detail", reportP.id)
    else:
        return redirect("detail", reportP.id)


def userSettings(request):
	user, created = User.objects.get_or_create(id=request.user.id)
	setting = user.setting

	seralizer = UserSerailizer(setting, many=False)

	return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
	data = json.loads(request.body)
	theme = data['theme']
	
	user, created = User.objects.get_or_create(id=request.user.id)
	user.setting.value = theme
	user.setting.save()
	return JsonResponse('Updated..', safe=False)

def aboutUs(request):
    return render(request, "aboutUs.html")

def termofservices(request):
    return render(request, "tos.html")

def privacy(request):
    return render(request, "privacy.html")

def contact(request):
    contactform = ContactUsForm()

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your feedback. We will get back to you as soon as possible")
            return redirect("contact")
    else:
        contactform = ContactUsForm()
    return render(request, "contact.html", context={"form":contactform})