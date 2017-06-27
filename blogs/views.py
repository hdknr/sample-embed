# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from corekit import views as core_views
from . import models
from logging import getLogger
import mimetypes
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
        url=r'^(?P<id>\d+)(?:/(?P<tpl>[^\.]+))?(?:\.(?P<xt>.+))?$',
        name="blogs_article_detail", order=20, )
    def detail(self, request, id, tpl, xt):
        tpl = tpl or 'detail'
        xt = xt or 'html'
        name = ".".join([tpl, xt])
        content_type = mimetypes.guess_type(name)[0]
        instance = models.Article.objects.filter(id=id).first()
        if not instance:
            return self.page_not_found()

        return self.cors(
            self.render(
                'blogs/article/{}'.format(name),
                content_type=content_type, instance=instance, ),
            origin='*')
