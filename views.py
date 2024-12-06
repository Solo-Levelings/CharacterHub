# TODO There's certainly more than one way to do this task, so take your pick.

from django.http import JsonResponse
from .models import Post, Comment

def get_posts_with_comments(request):
    posts_data = []
    
    posts = Post.objects.all().order_by('-timestamp')
    
    for post in posts:

        comments = Comment.objects.filter(post=post).order_by('-timestamp')[:3]
        
        post_data = {
            "post_text": post.text,
            "post_timestamp": post.timestamp,
            "author_username": post.author.username,
            "comment_count": Comment.objects.filter(post=post).count(),
            "comments": [
                {
                    "comment_text": comment.text,
                    "comment_timestamp": comment.timestamp,
                    "comment_author_username": comment.author.username
                }
                for comment in comments
            ]
        }
        posts_data.append(post_data)
    
    return JsonResponse(posts_data, safe=False)


""""
To fetch 3 random comments instead of the latest:

comments = Comment.objects.filter(post=post).order_by('?')[:3]

This change fetches 3 random comments associated with each post using Django's order_by('?'), which orders results randomly.
"""

