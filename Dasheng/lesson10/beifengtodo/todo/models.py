#! encoding=utf8
from django.db import models

# Create your models here.

class Dream(models.Model):
    dtime = models.DateTimeField(auto_now=True,auto_created=True,verbose_name=u'做梦时间')
    content = models.CharField(max_length=300)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = u'梦想清单'
        verbose_name_plural = verbose_name
        ordering=['-dtime']
