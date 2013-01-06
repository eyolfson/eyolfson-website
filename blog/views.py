from django.core.urlresolvers import reverse
from django.views.generic import date_based, simple
from eyolfson.apps.blog.models import Post

date_field='pub_date'
make_object_list=True
month_format='%m'
queryset=Post.objects.all()

def post_index(request, **kwargs):
    return date_based.archive_index(
        request,
        date_field='pub_date',
        queryset=Post.objects.all(),
        **kwargs
    )
post_index.__doc__ = date_based.archive_index.__doc__

def post_year(request, year, **kwargs):
    return date_based.archive_year(
        request,
        year=year,
        date_field=date_field,
        make_object_list=make_object_list,
        queryset=queryset,
        **kwargs
    )
post_year.__doc__ = date_based.archive_year.__doc__

def post_month(request, year, month, **kwargs):
    return date_based.archive_month(
        request,
        year=year,
        month=month,
        date_field=date_field,
        month_format=month_format,
        queryset=queryset,
        **kwargs
    )
post_month.__doc__ = date_based.archive_month.__doc__

def post_day(request, year, month, day, **kwargs):
    return date_based.archive_day(
        request,
        year=year,
        month=month,
        day=day,
        date_field=date_field,
        month_format=month_format,
        queryset=queryset,
        **kwargs
    )
post_day.__doc__ = date_based.archive_day.__doc__

def post_detail(request, year, month, day, slug, **kwargs):
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        slug=slug,
        date_field=date_field,
        month_format=month_format,
        queryset=queryset,
        **kwargs
    )
post_detail.__doc__ = date_based.object_detail.__doc__

def post_redirect(request, year, month, day=None, slug=None, **kwargs):
    month = month.zfill(2)
    if day:
        day = day.zfill(2)
    if slug:
        return simple.redirect_to(
            request,
            url=reverse('blog_detail', args=[year, month, day, slug]),
            permanent=True,
            **kwargs
        )
    elif day:
        return simple.redirect_to(
            request,
            url=reverse('blog_day', args=[year, month, day]),
            permanent=True,
            **kwargs
        )
    else:
        return simple.redirect_to(
            request,
            url=reverse('blog_month', args=[year, month]),
            permanent=True,
            **kwargs
        )
post_redirect.__doc__ = simple.redirect_to.__doc__
