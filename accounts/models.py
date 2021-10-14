from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_init, post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from userposts.models import UserMessages, UserPosts
from django.templatetags.static import static
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics",
                              null=True, blank=True)
    total_message = models.IntegerField(null=True,blank=True,verbose_name="Total Message", default=0)
    total_post = models.IntegerField(null=True,blank=True,verbose_name="Total Post", default=0)
    is_email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        # profile = super(Profile, self).save()

        super(Profile, self).save(*args, **kwargs)


        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            image = image.convert('RGB')
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class UserRanks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank_name = models.CharField(
        null=True, blank=True, default="Guardian of Nakamoto", verbose_name="Rank Name", max_length=150)
    # rank_image = models.ImageField(
    #     verbose_name="Rank Gif", default="guard.gif", null=True, blank=True)
    score = models.IntegerField(
        null=True, blank=True, verbose_name="Score", default=0)

    # def save(self, *args, **kwargs):
    #     super(UserRanks, self).save(*args, **kwargs)

    def total_score(self):
        return self.score.count()
    
    @property
    def rank_image_url(self):
        if self.score < 50:
            self.rank_name = "Guardian of Nakamoto"
            self.save()
            return static("image/ranks/guardianofnakamoto.gif")
        elif self.score < 100:
            self.rank_name = "Assasin"    
            self.save()      
            return static("image/ranks/assasin.gif")
        elif self.score < 200:
            self.rank_name = "Gladiator"
            self.save()      
            return static("image/ranks/gladiator.gif")
        elif self.score < 400:
            self.rank_name = "Ghost"          
            self.save()
            return static("image/ranks/ghost.gif")
        elif self.score < 400:
            self.rank_name = "Dark Knight"          
            self.save()
            return static("image/ranks/knight.gif")
        elif self.score < 800:
            self.rank_name = "Lord of Shaddows"          
            self.save()
            return static("image/ranks/lordofshaddow.gif")
        elif self.score < 1200:
            self.rank_name = "Guardian of Galaxy"
            self.save()
            return static("image/ranks/guardofgalaxy.gif")
        elif self.score > 2000:
            self.rank_name = "King of Kings"
            self.save()
            return static("image/ranks/kingofkings.gif")

class Notifications(models.Model):
    # 1 = Like, 2 = Comment,Reply
	notification_type = models.IntegerField()
	to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
	from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
	post = models.ForeignKey(UserPosts, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	comment = models.ForeignKey(UserMessages, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)
	user_has_seen = models.BooleanField(default=False)
