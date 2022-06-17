import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse

from lexbot.users.forms import UserAdminChangeForm
from lexbot.users.models import User
from lexbot.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def dummy_get_response(self, request: HttpRequest):
        return None

    def test_get_success_url(self, user: User, rf: RequestFactory):
        pass

    def test_get_object(self, user: User, rf: RequestFactory):
        pass

    def test_form_valid(self, user: User, rf: RequestFactory):
        pass


class TestUserRedirectView:
    pass

class TestUserDetailView:
    pass
