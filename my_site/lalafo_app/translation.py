from modeltranslation.translator import TranslationOptions,register
from .models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'descriptions')



