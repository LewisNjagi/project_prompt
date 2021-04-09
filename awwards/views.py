from django.shortcuts import render,get_object_or_404
from .forms import PostForm,UpdateUserForm,UpdateUserProfileForm,RateForm
from .models import Review,Profile,Post
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,UserSerializer,PostSerializer
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
    posts = Post.all_objects()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
    else:
        form = PostForm()
    return render(request,'index.html',{"form":form,"posts":posts})

def profile(request, username):
    post = request.user.profile.post.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
    else:
        form = PostForm()
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'posts': post,
        'form':form,
    }
    return render(request,'profile.html',params)

# def review(request,post):
#     post = Post.objects.get(title=post)
#     reviews = post.review.all()
#     global review
#     global reviewtotal
#     if request.method == 'POST':
#         rate_form = RateForm(request.POST)
#         if rate_form.is_valid():
#             review = rate_form.save(commit=False)
#             review.post = post
#             review.user = request.user.profile
#             review.save()
#             rating = Review.objects.filter(post=post)

#             design_one = [design.design for design in rating]
#             design = sum(design_one) / len(design_one)
#             usability_one = [usability.usability for usability in rating]
#             usability = sum(usability_one) / len(usability_one)
#             content_one = [content.content for content in rating]
#             content = sum(content_one) / len(content_one)

#             total = (design + usability + content) / 3
#             review.total = round(total, 2)
#             review.save()
#             # create a total class only

#             # reviewtotal = Review.objects(pk = review.id).first()

#     else:
#         rate_form = RateForm()
        
#         # reviewtotal = Review.objects(pk = review.id).first()

#     params = {
#         'posts': post,
#         'rate_form': rate_form,
#         'reviews':reviews,
#         # 'reviewtotal':reviewtotal,
#     }
#     return render(request, 'review.html', params)

# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_profile = Profile.objects.all()
#         serializers = ProfileSerializer(all_profile, many=True)
#         return Response(serializers.data)

# class UserList(APIView):
#     def get(self, request, format=None):
#         all_user = User.objects.all()
#         serializers = UserSerializer(all_user, many=True)
#         return Response(serializers.data)

# class PostList(APIView):
#     def get(self, request, format=None):
#         all_post = Post.objects.all()
#         serializers = PostSerializer(all_post, many=True)
#         return Response(serializers.data)

# #  if request.method == 'POST':
# #         form = UploadForm(request.POST)
# #         if form.is_valid:
# #             post = form.save(commit=False)
# #             post.save()
# #             rating = Rating.objects.filter(id = 26)
# #             # print(design.design for design in rating)
# #             # print(rating)

# #             design_one = [design.design for design in rating]
# #             design = sum(design_one) 
# #             usability_one = [usability.usability for usability in rating]
# #             usability = sum(usability_one) 
# #             content_one = [content.content for content in rating]
# #             content = sum(content_one)

# #             total = (design + usability + content) / 3
# #             post.total = total
# #             post.save()
# #     else:
# #         form = UploadForm()