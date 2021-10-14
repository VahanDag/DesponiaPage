from django.forms.utils import flatatt
from django.urls import reverse
import threading
from django.conf import settings
from django.core.mail import EmailMessage
from .utils import generate_token
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.forms.widgets import NullBooleanSelect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.messages.api import add_message
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from accounts.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):
    if request.method == "POST":

        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username control
            if User.objects.filter(username=username).exists():
                messages.add_message(
                    request, messages.WARNING, "This username is already exist")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(
                        request, messages.WARNING, "This email is already exist")
                    return redirect("register")
                else:
                    # No Problem
                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    user.save()

                    send_activation_email(user, request)

                    messages.add_message(
                        request, messages.SUCCESS, "We sent you an email to verify your account")
                    return redirect("login")
        else:
            messages.add_message(request, messages.ERROR,
                                 "passwords do not match")
            return redirect("register")

    else:
        return render(request, "accounts/register.html")


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(
                request, username=username, password=password)

            if user and not user.is_email_verified:
                messages.add_message(request, messages.ERROR,
                                     'Email is not verified, please check your email inbox')
                return render(request, 'accounts/login.html', status=401)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect("home")
                else:
                    messages.add_message(
                        request, messages.ERROR, "Disabled Account")
            else:
                messages.add_message(
                    request, messages.ERROR, "Invalid login or password. Please try again.")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {'form': form})


def logout_user(request):
    auth.logout(request)
    return redirect('home')


def update_profile(request):
    if request.method == "POST":
        beforeEmail = request.user.email
        print(beforeEmail, "email yazdi")
        u_form = UserUpdateForm(request.POST, instance=request.user)
        U_username = request.POST['username']
        U_email = request.POST['email']
        u_signature = request.POST['signature']
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if U_email != request.user.email:
            if User.objects.filter(email=U_email).exists():
                messages.add_message(
                    request, messages.ERROR, "This email is already exist")
            else:
                if u_form.is_valid() and p_form.is_valid():
                    
                    u_form.save()
                    p_form.save()

                    request.user.is_email_verified = False
                    send_activation_email(request.user, request)
                    request.user.save()
                    messages.add_message(
                        request, messages.SUCCESS, "Your account has been updated! You need to verify your email account. Please check your email.")
                    return logout_user(request)
                    # messages.add_message(
                    #     request, messages.SUCCESS, "Your account has been updated! ")
                    # userName = request.user
                    # return redirect("users", userName=userName)
        else:
            if u_form.is_valid() and p_form.is_valid():

                u_form.save()
                p_form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Your account has been updated! ")
                userName = request.user
                return redirect("users", userName=userName)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, "accounts/update.html", context)


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('accounts/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    # if not settings.TESTING:
    EmailThread(email).start()
    # email.send()


def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'accounts/activate-failed.html', {"user": user})

