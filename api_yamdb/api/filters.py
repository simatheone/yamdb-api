from django_filters import FilterSet, CharFilter

from reviews.models import Title


class TitleFilterBackend(FilterSet):
    """
    Кастомный фильтр для Title.
    Добавляет возможность поиска по полю slug жанра и категории.
    """
    genre = CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    category = CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')