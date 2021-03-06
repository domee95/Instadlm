from django.contrib.auth.models import User
from django.test import TestCase

from followers.models import Relationship
from followers.utils import get_followers, get_following


class RelationshipTests(TestCase):
    def setUp(self):
        """
        Se ejecuta antes de cada test
        :return:
        """
        self.user1 = User.objects.create_user("Sonia", "sonia@mendoza.com", "sonialexandra")
        self.user2 = User.objects.create_user("Andres", "andres@mendoza.com", "andresalejandro")
        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 sigue a usuario2

    def test_get_followers_returns_users_that_follow_a_given_user(self):
        followers = get_followers(self.user2)
        self.assertEqual([self.user1], followers)  # followers == [user1]

    def test_get_following_returns_users_that_a_given_users_follow(self):
        following = get_following(self.user1)
        self.assertEqual([self.user2], following)  # followers == [user1]

