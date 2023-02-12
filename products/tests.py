from django.test import TestCase
from .models import ProductsModel
from django.core.exceptions import ValidationError

class ProductsModelTestCase(TestCase):
    def setUp(self):
        ProductsModel.objects.create(
            name='Super Mario Odyssey',
            price=197.88,
            score=100,
            image='super-mario-odyssey.png'
        )
        ProductsModel.objects.create(
            name='Call Of Duty Infinite Warfare',
            price=49.99,
            score=80,
            image='call-of-duty-infinite-warfare.png'
        )

    def test_product_name_is_not_null(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertIsNotNone(product.name)

    def test_product_price_is_not_null(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertIsNotNone(product.price)

    def test_product_score_is_not_null(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertIsNotNone(product.score)

    def test_product_image_is_not_null(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertIsNotNone(product.image)

    def test_product_name_is_not_blank(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertNotEqual(product.name, '')

    def test_product_price_is_not_blank(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertNotEqual(product.price, '')

    def test_product_score_is_not_blank(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertNotEqual(product.score, '')

    def test_product_image_is_not_blank(self):
        product = ProductsModel.objects.get(name='Super Mario Odyssey')
        self.assertNotEqual(product.image, '')
        
