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

class HoodTest(TestCase):
    def setUp(self):
        self.kgl = Location.objects.create(name='kgl')

        self.south = Hood.objects.create(
            hood_name='south',occupants_count =1, location=self.kgl)

    def test_instance(self):
        self.south.save()
        self.assertTrue(isinstance(self.south, Hood))

    def test_get_hoods(self):
        self.south.save()
        hoods = Hood.get_hoods()
        self.assertTrue(len(hoods) > 0)

class BusinessTest(TestCase):
    def setUp(self):
        self.bizz= Business.objects.create(b_name='store',b_description='supermarket',b_email='kgl@email.com')

    def test_instance(self):
        self.bizz.save()
        self.assertTrue(isinstance(self.bizz,Business))

    def test_get_business(self):
        self.bizz.save()
        business = Business.get_business()
        self.assertTrue(len(business) >0 )

class PostsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='missy')
        self.kgl = Location.objects.create(name='kgl')

        self.south = Hood.objects.create(
            hood_name='south',occupants_count =1, location=self.kgl)

        self.security= Posts.objects.create(title='new',content='new content',posted_by= self.user, hood= self.south)

    def test_instance(self):
        self.security.save()
        self.assertTrue(isinstance(self.security,Posts))

    def test_delete_posts(self):
        self.security.save()
        self.security.delete()
        self.assertTrue(len(Posts.objects.all()) == 0)
