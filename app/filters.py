from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    memo = filters.CharFilter(label='メモ', lookup_expr='contains')
    memo_ex = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('memo', 'memo'),
            ('number', 'number'),
        ),
        field_labels={
            'memo': 'メモ',
            'number': '番号',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('memo', 'category', 'memo_ex',)
