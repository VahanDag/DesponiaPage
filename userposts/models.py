from posts.models import Category
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db import models
from froala_editor.fields import FroalaField
from tinymce import models as tinymce_models


class UserPosts(models.Model):
    postTitle = models.CharField(max_length=100, verbose_name="Title")
    postContent = tinymce_models.HTMLField(null=True, verbose_name="Content")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", null=True,blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of upload")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True ,null=True, verbose_name="Username")
    last_message= models.DateTimeField(blank=True,null=True)
    last_message_username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True, verbose_name="Last Message Username", related_name="last_message_username")
    answer_count = models.IntegerField(null=True,blank=True,verbose_name="Answer Count", default=0)
    like_post = models.ManyToManyField(User, related_name="like_post",blank=True)
    post_views = models.IntegerField(null=True, verbose_name="post_views", default=0)
    
    def __str__(self):
        return self.postTitle

    def total_likes(self):
        likes = self.like_post.count()
        return self.like_post.count()

    def get_absolute_url(self): # new
        return reverse('detail', args=[str(self.id)])

        
class UserMessages(models.Model):
    postMessages = tinymce_models.HTMLField(null=True, verbose_name="Messages")
    post = models.ForeignKey(
        UserPosts, on_delete=models.CASCADE, verbose_name="Linked Post", null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of upload")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Username", null=True)
    replies = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    like_message = models.ManyToManyField(User, related_name="like_message",blank=True)
    total_like = models.IntegerField(null=True,blank=True,verbose_name="Total Like", default=0)
    
    
    def children(self): #replies
        return UserMessages.objects.filter(replies = self)

    @property
    def is_replies(self):
        if self.replies is not None:
            return False
        return True

    def total_likes(self):
        return self.like_message.count()
    
    def get_absolute_url(self): # new
        return reverse('detail', args=[str(self.post.id)])

    def __str__(self):
        return self.postMessages
