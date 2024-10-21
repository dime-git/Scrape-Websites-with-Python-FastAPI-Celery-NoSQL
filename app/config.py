import os
from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

# load_dotenv() is used to load values from a .env file into the environment so they can be accessed easily in the code.
load_dotenv() 

# config.py is the setup team that sets the stage, loads the necessary data, and ensures that everything is ready to go. 

## PURPOSE
# config.py -> is all about configuration and settings. It is where we define application settings, environment variables, and parameters that we want to manage centrally. It ensures that any sensitive data or configurable parameters (like API keys, database credentials) are easily accessible but not hardcoded.

## HOW IT FITS
# config.py aCTs as the setup/configuration brain of the application—it handles the configurations that the application needs to operate. It is independent of the app logic; it focuses only on loading, validating, and providing configurations.

## ENVIRONMENT MANAGEMENT
# We use environment variables to manage values that might change based on the environment (e.g., local development, testing, production).

if os.getenv("CQLENG_ALLOW_SCHEMA_MANAGEMENT") is None:
    os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"

##CLASS SETTINGS 
# This class is where we define our settings and specify where the values should come from. It uses BaseSettings from Pydantic, which helps in managing these settings with type validation. Each attribute of the Settings class maps to an environment variable, making sure they are pulled in from the system/environment, and ensuring they are correctly validated.

class Settings(BaseSettings):
    class Settings(BaseSettings):
        project_name: str = Field(..., env="PROJECT_NAME")
        db_client_id: str = Field(..., env="ASTRA_DB_CLIENT_ID")
        db_client_secret: str = Field(..., env="ASTRA_DB_CLIENT_SECRET")
        db_app_token: str = Field(..., env="ASTRA_DB_APP_TOKEN")
        cqleng_allow_schema_management: str = Field(..., env="CQLENG_ALLOW_SCHEMA_MANAGEMENT")

    class Config:
        env_file = ".env"
        extra = "allow"  


##CACHING
# We use lru_cache() to ensure that the settings are loaded only once and reused whenever needed, which is more efficient than loading them multiple times.
@lru_cache
def get_settings():
    settings = Settings()
    return settings