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
        name='Mug',
        description='This is a mug',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= pottery,
        name='Plate',
        description='This is a Plate',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= pottery,
        name='Vase',
        description='This is a Vase',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        name='Mona Lisa',
        description='This is the mona lisa',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        name='Self Portrait',
        description='This is a Self Potrait',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= arts,
        name='Self Portrait',
        description='This is a Self Potrait',
        image='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png',
        price=22.99,
        in_stock=True,
        is_active=True
    ).save()
    Product(
        category= crafts,
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


# steps to get this up and going 
#  PSQL COMMAND INTERFACE 
#  psql
# \L to list the database
# DROP DATABASE <database name>; (check if the data base is still there)
# (recreate the database)
# psql - f settings.py

# recreate the models within the databse
# python manage.py makemigrations
# python manage.py migrate

# create the super User
# python manage.py createsupseruser

# create the empty seed file 
# python manage.py makemigrations --empty <appname>

# put the seed data within the newly created seed File. 

# python manage.py migrate. 