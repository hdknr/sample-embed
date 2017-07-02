# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from . import methods


class Article(models.Model, methods.Article):
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
