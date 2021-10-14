from forumPage.settings import STATIC_URL
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
from userposts.models import UserPosts, UserMessages
from accounts.models import Notifications, UserRanks
from posts.forms import MessageForm
from posts.forms import PostForm
from posts.models import Category
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.api import add_message
from django.views.generic import UpdateView, DeleteView
from django.contrib import auth, messages
from django import contrib
from django.conf.urls.static import static
from django.conf import settings
from django.forms import inlineformset_factory
from django.core.paginator import Paginator
from accounts.models import Profile

def liked_post(request, pk):
    if request.is_ajax():
        pk1 = request.POST.get('userposts_id')
        # user_pk =get_object_or_404(User, id=request.POST.get("user_id"))
        post = get_object_or_404(UserPosts, id=pk)
        user_update = get_object_or_404(UserRanks, user=post.username)
        if request.user in post.like_post.all():
            liked = False
            post.like_post.remove(request.user)

            user_update.score -= 5
            user_update.save()
        else:
            liked = True
            post.like_post.add(request.user)
            user_update.score += 5
            user_update.save()

            if not Notifications.objects.filter(notification_type=1, post=post, to_user=post.username, from_user=request.user).exists():
                notify = Notifications.objects.create(notification_type=1, post=post,
                                                      to_user=post.username, from_user=request.user,)
                    
                # notify.save()

        return JsonResponse({'liked': liked, 'count': post.like_post.count()})
    return redirect('detail', pk)


def liked_message(request, pk):
    vaho = UserMessages.objects.get(pk=pk)
    if request.is_ajax():
        pk1 = request.POST.get('usermessages_id')
        # post_pk =get_object_or_404(UserPosts, id=request.POST.get("userposts_id"))
        message = get_object_or_404(UserMessages, id=pk)
        user_update = get_object_or_404(UserRanks, user=message.username)
        if request.user in message.like_message.all():
            liked = False
            message.like_message.remove(request.user)
            message.total_like -= 1
            message.save()
            user_update.score -= 5
            user_update.save()
        else:
            liked = True
            message.like_message.add(request.user)
            message.total_like += 1
            message.save()
            user_update.score += 5
            user_update.save()

            if not Notifications.objects.filter(notification_type=1, comment=message, to_user=message.username, from_user=request.user).exists():
                notify = Notifications.objects.create(notification_type=1, comment=message,
                                                      to_user=message.username, from_user=request.user,)
            # else:
            #     notify = Notifications.objects.create(notification_type=1, comment=message,
            #                                           to_user=message.username, from_user=request.user,)
                # notify.save()

        return JsonResponse({'liked': liked, 'count1': message.like_message.count()})
    return redirect('detail', vaho.post_id)


def detail_post(request, _detail):
    postDetail = UserPosts.objects.get(pk=_detail)
    signature = User.objects.get(username=postDetail.username)
    postCount = UserPosts.objects.all().filter(username=signature).count()
    messageCount = UserMessages.objects.all().filter(username=signature).count()

    messagesPaginator = UserMessages.objects.all().filter(post_id=postDetail.id)
    pagenumber = int((messagesPaginator.count() / 5) + 1)

    # ranks = UserRanks.objects.all().filter()
    postDetail.post_views += 1
    postDetail.save()

    total_post_likes = postDetail.total_likes()

    p = Paginator(messagesPaginator, 5)
    page = request.GET.get('page')
    p_message = p.get_page(page)
    # position = Article.objects.filter(date__gt=articleid.date).count()

    # return total_message
    # liked = False
    # if postDetail.like_post.filter(id= request.user.id).exists():
    #     liked = True
    post = get_object_or_404(UserPosts, id=postDetail.id)
    messages1 = UserMessages.objects.filter(post_id=postDetail.id)

    list_mess = list(messagesPaginator)

    # m_messageCount = UserMessages.objects.all().filter(username =messages.username).count()
    # postMessages = UserPosts.objects.all().filter(category=forum.id).order_by('-created_at').filter(category=forum.id)

    if request.method == "POST":  # New Message
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            form.instance.post = postDetail
            form.save()
            # findmessage = UserMessages.objects.get(id = form.instance.id)
            # position = UserMessages.objects.filter(created_at = findmessage.created_at).count()

            postDetail.last_message = form.instance.created_at
            postDetail.last_message_username = form.instance.username
            postDetail.answer_count += 1
            postDetail.save()

            user_update_score = get_object_or_404(UserRanks, user=request.user)
            user_update_score.score += 2
            user_update_score.save()

            user_update_message = get_object_or_404(
                Profile, user=form.instance.username)
            user_update_message.total_message += 1
            user_update_message.save()

            if form.instance.username != postDetail.username:
                notify = Notifications.objects.create(notification_type=2, post=form.instance.post,
                                                      to_user=form.instance.post.username, from_user=form.instance.username, date=form.instance.created_at,
                                                      comment=form.instance)
                notify.save()

            category_message = Category.objects.get(id=postDetail.category_id)
            category_message.totalMessage += 1
            category_message.save()

            messages.add_message(
                request, messages.SUCCESS,
                f"Your message has been successfully published  <a href='?page={pagenumber}#{form.instance.id}'> Go to message </a>")
            # return redirect("detail"  , postDetail.id)
            return HttpResponseRedirect("/posts/%s?page=%s#%s" % (postDetail.id, pagenumber, form.instance.id))
    else:
        form = MessageForm()
    context = {
        "detail": postDetail,
        "sign": signature,
        "totalPost": postCount,
        'totalMessage': messageCount,
        "messages1": messages1,
        "form": form,
        "total_post_likes": total_post_likes,
        "likeList": post.like_post.all(),
        "total": list_mess,
        "p_messages": p_message,
        "pagenumber": pagenumber
        # "evet":messages.like_message.all()
    }
    return render(request, "DetailPost.html", context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserPosts
    form_class = PostForm
    template_name = "edit_post.html"
    context_object_name = "postDetail"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return redirect("login")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserPosts
    template_name = "delete_post.html"
    success_url = "/"
    context_object_name = "postDetail"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return redirect("login")


def reply(request, pk):
    reply_form = MessageForm()
    message = UserMessages.objects.get(pk=pk)
    post = UserPosts.objects.get(pk=message.post.id)

    messagesPaginator = UserMessages.objects.all().filter(post_id=post.id)
    pagenumber = int((messagesPaginator.count() / 5) + 1)

    if request.method == "POST":  # reply
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            form.instance.post = message.post
            form.instance.replies = message
            form.save()

            post.last_message = form.instance.created_at
            post.last_message_username = form.instance.username
            post.save()

            user_update_score = get_object_or_404(UserRanks, user=request.user)
            user_update_score.score += 2
            user_update_score.save()

            user_update_message = Profile.objects.get(
                user=form.instance.username)
            user_update_message.total_message += 1
            user_update_message.save()

            notify = Notifications.objects.create(notification_type=2, comment=form.instance,
                                                  to_user=message.username, from_user=form.instance.username, date=form.instance.created_at,)
            notify.save()

            category_message = Category.objects.get(id=post.category_id)
            category_message.totalMessage += 1
            category_message.save()

            return HttpResponseRedirect("/posts/%s?page=%s#%s" % (post.id, pagenumber, form.instance.id))

    context = {
        "reply_form": reply_form,
        "message": message
    }
    return render(request, "reply_message.html", context)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserMessages
    form_class = MessageForm
    template_name = "edit_message.html"
    context_object_name = "messages"
    # success_url = "/"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return redirect("login")


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserMessages
    template_name = "delete_message.html"
    # success_url = "/"
    context_object_name = "messages"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.username:

            return True
        else:
            return redirect("login")

    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        message = self.get_object()
        return reverse_lazy('detail', args=[str(message.post.id)])
    # def get_success_url(self):
    #      return reverse('some_url', kwargs={'pk': self.pk})
