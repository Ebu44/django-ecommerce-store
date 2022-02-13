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


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        verbose_name=_("product website ID"),
        help_text=_("format: required, unique"),
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name=_("product safe URL"),
        help_text=_("format: required, letters, numbers,underscores or hyphens"),
        max_length=255,
        unique=False,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
        max_length=255,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("product description"),
        help_text=_("format: required"),
        unique=False,
        null=False,
        blank=False,
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
        unique=False,
        null=False,
        blank=False,
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name
