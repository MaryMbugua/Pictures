from django.test import TestCase
from .models import Category,Location, Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.cinderella = Image(name = 'cinderella', description = 'a cinderella pic')
        self.cinderella.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.cinderella, Image))

    def test_save_method(self):
        self.cinderella.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)            

    def test_delete_method(self):
        self.new_image = Image(name = 'intercontinental', description = 'a birds eye view of the Intercontinental hotel')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

    def test_update_method(self):
        self.jug = Image(name = 'jug', description = 'a blue jug')
        self.jug.save_image()
        self.jug = Image(name = 'cup', description = 'a blue jug')        
        self.jug.update_image(name = 'cup')
        self.jug.save_image()
        images = Image.objects.filter(name = 'cup)
        pics = Image.objects.all()       
        self.assertEqual(len(images), 1)

class LocationTestClass(TestCase):    
    def setUp(self):
        self.Kenya = Location(locname = 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, Location))

    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location = Location(locname = 'Kericho')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

    def test_update_method(self):
        self.Nairobi = Location(name = 'Nairobi')
        self.Nairobi.save_location()
        self.Nairobi = Location(name = 'Nai')
        self.Nairobi.save_location()
        self.Nairobi.update_location(name = 'Nai')
        locations = Location.objects.filter(name = 'Nai')
        self.assertEqual(len(locations), 1)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Danger = Category(catname = 'danger')

    def test_instance(self):
        self.assertTrue(isinstance(self.Danger, Category))

    def test_save_method(self):
        self.Danger.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.new_category = Category(catname = 'colours')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_category(self):
        self.pop = Category(catname = 'pop')
        self.pop.save_category()
        self.pop = Category(catname = 'popculture')
        self.pop.save_category()
        self.pop.update_category(catname = 'popculture')
        categories = Category.objects.filter(catname = 'popculture')
        self.assertEqual(len(categories), 1)