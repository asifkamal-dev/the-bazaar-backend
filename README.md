### Your project idea 
An online marketplace where individuals can share their wares and products that they would like to sell to customers. There are two sides to this website. There will be a customer-facing site where all products from individual sellers would be shared on the profile and customers are able to add these products to their cart and essentially checkout, and there is a seller's view where they are able to upload their wares and have access to a basic CRM to show them their sales, customers, and metrics that they can use to increase their market share. 
### Your tech stack (frontend, backend, database)
- Frontend: 
React
- Backend:
Django
- Database:
postgres sql
### List of backend models and their properties
{this is going to be an evolving model as I'm sure that the database is going to incorporate sellers wares to what they buy }
class Seller(models.Model):
    user_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Customer(models.Model):
    user_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class MerchWare(models.Model):
    tittle = models.CharField(max_length=100)
    cost = models.IntegerField()
    description: textField()
c   reated_by = models.ForeignKey(
        Seller, 
        default='Admin',
        on_delete=SET_DEFAULT, 
        related_name='MerchWare'
    )
    def __str__(self):
        return self.
### React component hierarchy (if applicable)
<Will insert hieracrhy once build />
### User stories
- As a seller, I should be able to log in and see what products I have currently available to sell on my site.
- As a seller, I should be able to see orders that were recently placed by my customers. 
- As a seller, I should be able to see my customers and sales interactions that I have so far. 
- As a seller, I should be able to enter in new products, edit old products, and delete products from my page. 
- As a seller, I should be able to see metrics about my business. 
- As a customer, I should be able to login and see what products are available to be purchased.
- As a customer, I should be able to update and delete my profile page. 
- As a customer, I should be able to add shipping details to order so that it ships properly. 
- As a customer, I should be able to checkout products within my cart. 

More to come with user stories

STRETCH
- As a seller, I should be able to have a limited time a number of my products can be purchased. 
- As a seller, I should be able to see how much my inventory is moving and evaluate which ones to make more of. 
- As a seller, I should be able to keep track of the delivery and where it's being sent to. 
- As a customer, I should be able to make requests or leave notes to the buyer when purchasing. 
- As a customer, I should be able to see my past purchases and order tracking. 
### Wireframes

### Anything else your squad lead should know