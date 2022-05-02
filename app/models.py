from django.db import models
from django.core import validators


class Item(models.Model):

    CATEGORY_CHOICES = (
        (1, 'カテゴリー１'),
        (2, 'カテゴリー２'),
    )

    memo = models.CharField(
        verbose_name='メモ',
        max_length=200,
    )
    number = models.IntegerField(
        verbose_name='番号',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    category = models.IntegerField(
        verbose_name='カテゴリー',
        choices=CATEGORY_CHOICES,
        default=1
    )
    memo_ex = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
