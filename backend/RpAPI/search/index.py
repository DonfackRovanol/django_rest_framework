from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from product.models import product

@register(product)
class ProductIndex(AlgoliaIndex):
    #should_index='is_public'
    fields = [
        'name',
        'content',
        'prix',
        'public',
        'user'
    ]
    tags = "get_tags_list"
    
    settings = {
        'searchableAttributes':['name', 'content'],
        'attributesForFaceting':['user', 'public']
    }