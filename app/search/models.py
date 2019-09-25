# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name
