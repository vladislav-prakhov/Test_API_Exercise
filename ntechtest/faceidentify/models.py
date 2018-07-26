from django.db import models
import os


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class FacePhoto(models.Model):
    user_name = models.CharField(max_length=100)
    photo = models.FileField(upload_to=upload_location)
    threshold = MinMaxFloat(min_value=0.0, max_value=1.0, null=True, blank=True)
    res_n = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(upload_to=upload_location,
    #                           null=True,
    #                           blank=True,
    #                           width_field="width_field",
    #                           height_field="height_field"
    #                           )  # names should be in ""
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)

    objects = PostManager()

    def filename(self):
        return os.path.basename(self.file.name)

    def __unicode__(self):  # For python 2
        return self.user_name

    def __str__(self):  # for python3
        return self.user_name
