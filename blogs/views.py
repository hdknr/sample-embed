# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from corekit import views as core_views
from . import models
from logging import getLogger
logger = getLogger()


class ArticleView(core_views.View):

    @core_views.handler(
        url=r'',
        name="blogs_article_index", order=90,)
    def index(self, request):
        instances = models.Article.objects.all()
        return self.render(
            'blogs/article/index.html', instances=instances, )

    @core_views.handler(
        url=r'^(?P<id>\d+)$',
        name="blogs_article_detail", order=20, )
    def detail(self, request, id):
        instance = models.Article.objects.filter(id=id).first()
        if not instance:
            return self.page_not_found()

        return self.render('blogs/article/detail.html', instance=instance)
