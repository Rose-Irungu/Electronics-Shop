# from django.core.management.base import BaseCommand
# from electronics.models import Product
#
# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         Product.objects.all().delete()  # Clear existing
#         Product.objects.create(name="Laptop", description="Powerful laptop", price=999.99, image_url="https://via.placeholder.com/150")
#         Product.objects.create(name="Smartphone", description="Latest smartphone", price=699.99, image_url="https://via.placeholder.com/150")
#         Product.objects.create(name="Headphones", description="Noise cancelling", price=199.99, image_url="https://via.placeholder.com/150")
#         self.stdout.write(self.style.SUCCESS('Dummy products loaded.'))
