from django import forms
from userposts.models import UserPosts
from userposts.models import UserMessages
from froala_editor.widgets import FroalaEditor
from pages.models import ContactUs


class PostForm(forms.ModelForm):
    class Meta:
        model = UserPosts
        fields = ("postTitle", "postContent")

        widgets = {
            "postTitle": forms.TextInput(attrs={"class": "form-control formEx  ", "placeholder": "Title", "style": "font-size: x-large"}),
            "postContent": FroalaEditor(attrs={"class": "form-control formEx"}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = UserMessages
        fields = ("postMessages",)


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ("email","content")

        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control formEx  ", "placeholder": "Email", "style": "font-size: 20px"}),
            "content": forms.Textarea(attrs={"class": "form-control formEx","placeholder": "Your Message","style": "font-size: 20px"}),
        }