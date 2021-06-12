from django.db import models


class BaseModelManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(BaseModelManager, self) \
            .get_queryset(*args, **kwargs) \
            .filter(is_delete=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
