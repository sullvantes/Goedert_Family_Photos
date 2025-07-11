from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from taggit.managers import TaggableManager
from wagtail.admin.panels import FieldPanel

class CustomImage(AbstractImage):
    tags = TaggableManager(blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'tags',
    )

class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        'CustomImage',
        on_delete=models.CASCADE,
        related_name='renditions'
    )

    class Meta:
        unique_together = (('image', 'filter_spec', 'focal_point_key'),)