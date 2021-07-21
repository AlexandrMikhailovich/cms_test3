from garpix_page.models import BasePage


class Category(BasePage):
    template = 'pages/category.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import Post
        context = super().get_context(request, *args, **kwargs)
        posts = Post.on_site.filter(is_active=True, parent=kwargs['object'])
        context.update({
            'posts': posts
        })
        return context

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        default_related_name = "Content_category"
        ordering = ('-created_at',)
