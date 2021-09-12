from bazaar.models import Category
from django.db import migrations


def seed(apps, schema_editor):
    Product = apps.get_model('bazaar', 'Product')
    Category = apps.get_model('bazaar', 'Category')
    pottery = Category(name = 'Pottery')
    arts = Category(name = 'Arts')
    crafts = Category(name = 'Crafts')
    pottery = Category(name = 'Pottery')
    pottery.save()
    arts.save()
    crafts.save()

    Product(
        category= pottery,
        created_by=1,
        name='Mug',
        description='This is a mug',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= pottery,
        created_by=1,
        name='Plate',
        description='This is a Plate',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= pottery,
        created_by=1,
        name='Vase',
        description='This is a Vase',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        created_by=1,
        name='Mona Lisa',
        description='This is the mona lisa',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        created_by=1,
        name='Self Portrait',
        description='This is a Self Potrait',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        created_by=1,
        name='Self Portrait',
        description='This is a Self Potrait',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= crafts,
        created_by=1,
        name='Knit Socks',
        description='This is a Knit Socks',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
def fallow(apps, schema_editor):
    Product = apps.get_model('bazaar', 'Product')
    Category = apps.get_model('bazaar', 'Category')
    Product.objects.all().delete()
    Category.objects.all().delete()



class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
