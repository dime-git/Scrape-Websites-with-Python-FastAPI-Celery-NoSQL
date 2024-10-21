from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# model.py -> represents the structure of the database tables using the Cassandra ORM (cqlengine in this case).

data = {
    "asin": "TESTING123D",
    "title": "Mark 1adsf"
}

# The classes in models.py (like Product and ProductScrapeEvent) are used to define how data is stored in your database.
# The fields in these classes (like asin, title, etc.) are mapped directly to the database columns.
# models.py is responsible for interacting directly with the database — this includes performing CRUD operations (create, read, update, delete).

##TOOLS USED
# models.py uses Cassandra's ORM (cqlengine) to define the structure of the database and interact with it.

##ROLE IN APPLICATION
# models.py is closely tied to the backend data store (Cassandra) and is responsible for how data is saved and retrieved.


class Product(Model): # -> table
    __keyspace__ = "scraper_app" 
    #asin is defined as a primary key, meaning it uniquely identifies each Product record in the database.
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")

#The Product and ProductScrapeEvent classes are models that describe tables in Cassandra database (scraper_app keyspace).

#These models will be used when you want to perform operations like querying the database, inserting new rows, or deleting records.

class ProductScrapeEvent(Model): # -> table
    __keyspace__ = "scraper_app" #
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")

# def this -> ProductScrapeEvent.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")