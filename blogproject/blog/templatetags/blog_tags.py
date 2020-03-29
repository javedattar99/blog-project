


from blog.models import Post
from django import template
register = template.Library()

@register.simple_tag(name='tag_count')
def total_post():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_post():
    latest_post = Post.objects.order_by('-publish')[:4]
    return {'latest_post':latest_post}

from django.db.models import Count

#@register.assignment_tag
@register.simple_tag
def get_most_Commented_post(count=4):

    return Post.objects.annotate(total_comment=Count('comments')).order_by('-total_comment')[:count]
