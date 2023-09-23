from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import UserProfile, Post, Comment, Like, Follow, Notification, Message, Hashtag, UserSettings, Report
from django.contrib.auth.models import User

@login_required
def home(request):
    # Implement logic to display the user's home feed, including posts from people they follow
    # You can use the User, Post, Follow, and other models to fetch and display data
    return render(request, 'home.html')

class UserProfileView(View):
    def get(self, request, username):
        # Retrieve the user's profile based on their username and display it
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        return render(request, 'profile.html', {'profile': profile})

@login_required
class CreatePostView(View):
    def post(self, request):
        # Implement logic to create a new post
        # You can use the Post model to create a new post
        return redirect('home')

@login_required
class CommentView(View):
    def post(self, request, post_id):
        # Implement logic to add a comment to a post
        # You can use the Comment model to create a new comment
        return redirect('home')

@login_required
class LikeView(View):
    def post(self, request, post_id):
        # Implement logic to add or remove a like from a post
        # You can use the Like model to manage likes
        return redirect('home')

@login_required
class FollowView(View):
    def post(self, request, username):
        # Implement logic to follow or unfollow a user
        # You can use the Follow model to manage followers
        return redirect('profile', username=username)

@login_required
class NotificationsView(View):
    def get(self, request):
        # Implement logic to display user notifications
        # You can use the Notification model to fetch notifications
        return render(request, 'notifications.html')

@login_required
class SendMessageView(View):
    def post(self, request, username):
        # Implement logic to send a message to another user
        # You can use the Message model to create and store messages
        return redirect('messages')

@login_required
class MessagesView(View):
    def get(self, request):
        # Implement logic to display user's messages and conversations
        # You can use the Message model to fetch messages and conversations
        return render(request, 'messages.html')

@login_required
class HashtagView(View):
    def get(self, request, hashtag_name):
        # Implement logic to display posts with a specific hashtag
        # You can use the Hashtag model to fetch posts associated with the hashtag
        return render(request, 'hashtag.html')