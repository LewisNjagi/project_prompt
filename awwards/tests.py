from django.test import TestCase
from .models import Profile,Post
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    from django.contrib.auth.models import User
    def setUp(self):
        self.user = User(username='martin')
        self.user.save()
        self.profile = Profile(id=1,user=self.user,photo='download.jpeg',bio='My name is Martin', name='person')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user=User(username='martin'))
        self.profile.user.save()
        self.profile.save()
        self.post = Post(user=self.profile,image='default.jpeg', title='person', description='this is it',
        url='https://www.instagram.com/',category='space')
        self.post.save_post()

    def test_insatance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.post, Post))

    def test_save_image(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_update_image_caption(self):
        self.post.save_post()
        new_caption =Post.update_post('this is it','Yeah')
        post = Post.objects.get(description='Yeah')
        self.assertEqual(post.description,'Yeah')