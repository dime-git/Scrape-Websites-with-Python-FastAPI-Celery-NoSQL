from pydantic import BaseModel
from typing import Optional
from uuid import UUID

##EXPLANATION
# schema.py -> defines the data validation and serialization schemas used by FastAPI.

# The classes in schema.py (ProductSchema, ProductScrapeEventSchema) are used to validate incoming data, define the structure of request/response bodies, and serialize data.

# These classes inherit from Pydantic's BaseModel and provide a way to enforce type checks and validate input/output data.

# Fields are annotated with type hints (e.g., str, UUID), and optional fields use Optional.

# These schemas are primarily used in your API endpoints to enforce data validation.

# For instance, when a user makes a POST request to create a product, ProductSchema can be used to validate the request body before inserting it into the database.

# They are also used when returning responses to ensure data is formatted correctly.

##TOOLS USED
# schema.py uses Pydantic to define the structure and validation of data at the API layer.

##ROLE IN APPLICATION
# schema.py is an intermediary used to ensure that data coming into your system and going out of your system is properly structured and validated.


class ProductSchema(BaseModel):
    asin:str
    title: Optional[str]
    

class ProductScrapeEventSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]