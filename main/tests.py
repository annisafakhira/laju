from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        Product = Product.objects.create(
          title="BURHAN FC MENANG",
          content="BURHAN FC 1-0 PANDA BC",
          category="match",
          Product_views=1001,
          is_featured=True
        )
        self.assertTrue(Product.is_Product_hot)
        self.assertEqual(Product.category, "match")
        self.assertTrue(Product.is_featured)
        
    def test_product_default_values(self):
        Product = Product.objects.create(
          title="Test Product",
          content="Test content"
        )
        self.assertEqual(Product.category, "update")
        self.assertEqual(Product.Product_views, 0)
        self.assertFalse(Product.is_featured)
        self.assertFalse(Product.is_Product_hot)
        
    def test_increment_views(self):
        Product = Product.objects.create(
          title="Test Product",
          content="Test content"
        )
        initial_views = Product.Product_views
        Product.increment_views()
        self.assertEqual(Product.Product_views, initial_views + 1)
        
    def test_is_product_hot_threshold(self):
        # Test Product with exactly 20 views (should not be hot)
        Product_20 = Product.objects.create(
          title="Product with 20 views",
          content="Test content",
          Product_views=20
        )
        self.assertFalse(Product_20.is_product_hot)
        
        # Test Product with 21 views (should be hot)
        Product_21 = Product.objects.create(
          title="Product with 21 views", 
          content="Test content",
          Product_views=21
        )
        self.assertTrue(Product_21.is_product_hot)