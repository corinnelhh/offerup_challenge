from django.db import models

from django.utils.timezone import now


def upload_image_to(instance, filename):
    return 'media/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"), filename,
    )


class Image(models.Model):
    fileName = models.ImageField(upload_to=upload_image_to, blank=True)
    Duplicate = models.BooleanField(default=False)
    Hash = models.CharField(max_length=128)

    def save(self, cel_save=False, **kwargs):
        super(Image, self).save(**kwargs)
        if not cel_save:
            from offerup_infrastructure import tasks
            tasks.check_for_duplicates.apply_async(
                args=[self.id], countdown=1
            )
