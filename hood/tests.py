from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id =1, username='missy')
        self.profile = Profile.objects.create(user = self.user,bio = 'No bio',email='nga@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)