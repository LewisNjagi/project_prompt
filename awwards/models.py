from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = CloudinaryField('gallery/', default='default.jpeg')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)

    class Meta:
        ordering = ["-pk"]

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

# class Rating(models.Model):
#     rating = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'))
#     design = models.IntegerField(choices=rating)
#     usability = models.IntegerField(choices=rating)
#     content = models.IntegerField(choices=rating)
#     total = models.FloatField(default=0,blank=True)
#     user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='rating',null=True)
#     post = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='rating',null=True)

#     def __str__(self):
#         return self.total

# class Post(models.Model):
#     user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='post')
#     image = CloudinaryField('gallery/')
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=400)
#     url = models.URLField(max_length=400)
#     category = models.CharField(max_length=40)

#     def __str__(self):
#         return f'{self.title}'

#     def save_post(self):
#         self.save()

#     @classmethod
#     def update_post(cls,old,new):
#         cap = Post.objects.filter(description=old).update(description=new)
#         return cap

#     @classmethod
#     def all_objects(cls):
#         posts = cls.objects.all()
#         return posts

# RATE_CHOICES = [
#     (1, '1'),
#     (2, '2'),
#     (3, '3'),
#     (4, '4'),
#     (5, '5'),
#     (6, '6'),
#     (7, '7'),
#     (8, '8'),
#     (9, '9'),
#     (10, '10'),
# ]

# class Review(models.Model):
#     review = models.TextField(max_length=500,blank=True)
#     user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='review')
#     post = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='review')
#     design = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
#     usability = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
#     content = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
#     total = models.FloatField(default=0,blank=True)


#     class Meta:
#         ordering = ["-pk"]

#     def __str__(self):
#         return f'{self.user.name} Post'

# class Total(models.Model):
#     score = models.PositiveSmallIntegerField(default=0)

#     def __str__(self):
#         return self.score