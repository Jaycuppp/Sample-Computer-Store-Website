from import_export import resources
from .models import *

class StoreProductImports(resources.ModelResource):
    class Meta:
        model = StoreProducts
        import_id_fields = ('Name', 'Brand', 'Price', 'UPC', 'SKU', 'Stock', 'Summary', 'Key_Feat_1', 'Key_Feat_2',
            'Key_Feat_3', 'Key_Feat_4', 'Key_Feat_5', 'Key_Feat_6', 'Key_Feat_7', 'Key_Feat_8', 'Key_Feat_9',
            'Key_Feat_10', 'Picture', 'Spec_Sheet', 'Coupon', 'Category', 'Discontinued')