from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Inventory Category table implemented with MPTT
    """

    name = models.CharField(
        verbose_name=_("category name"),
        help_text=_("format: required, max-100"),
        max_length=100,
        null=False,
        unique=False,
        blank=False,
    )
    slug = models.SlugField(
        verbose_name=_("category safe URL"),
        help_text=_("format: required, letters, numbers, underscore, or hyphens"),
        max_length=150,
        null=False,
        unique=False,
        blank=False,
    )
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
        null=True,
        blank=True,
        unique=False,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name
