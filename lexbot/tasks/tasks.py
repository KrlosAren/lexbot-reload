from datetime import timedelta

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from config import celery_app

User = get_user_model()


def gen_verification_token(user):
    exp_date = timezone.now() + timedelta(days=1)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


@celery_app.task(name='send_invitation_register_email', max_retries=3)
def send_invitation_register_email(email_details):


    issued_user = User.objects.filter(pk=email_details['issued_pk']).first().username
    invited_email = email_details['invited_email']
    code = email_details['code']
    token = email_details['token']

    subject = 'Hello! @{} invited to Mercadito App'.format(issued_user)
    from_email = 'Mercadito App <noreplay@mercadito_reload.com>'

    content = render_to_string('emails/users/register_invitation.html', {
        'token': token,
        'code': code,
    })

    msg = EmailMultiAlternatives(subject, content, from_email, [invited_email])
    msg.attach_alternative(content, 'text/html')
    msg.send()


@celery_app.task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):

    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)

    subject = 'Welcome @{}! Verify you account to start using Mercadito App'.format(user.username)
    from_email = 'Mercadito App <noreply@mercadito_reload.com>'
    content = render_to_string('emails/users/account_verification.html', {
        'token': verification_token,
        'user': user,
        'url': 'localhost:8000/api/1'
    })
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()
