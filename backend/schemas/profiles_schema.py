""" profiles schema Pyd2.0  """
""" had Q clean and polish it up and add cute icons lol"""

from pydantic import BaseModel, EmailStr, HttpUrl, Field, ConfigDict, UUID4
from datetime import datetime, date, UTC
from enum import Enum
from typing import Optional, List, Dict, Any, Annotated
from uuid import UUID, uuid4


# --- 🐍 Pydantic 2.0 Configuration from GEMENI Template ---
class PydanticBaseModel(BaseModel):
    """Base model for Pydantic 2.0 with custom config"""
    # model_config = ConfigDict(
    #     populate_by_name=True,
    #     json_encoders={
    #         datetime: lambda v: v.isoformat(),
    #         date: lambda v: v.isoformat(),
    #     },
    #     schema_extra={
    #         "example": {
    #             "id": 1,
    #             "name": "Example",
    #             "created_at": "2023-10-01T00:00:00Z"
    #         }git json_schema_serialization_defaults_required=
    #     }
    # )

# --- 📍 Address & Phone Models (Nested) ---
class Address(BaseModel):
    street_address: str
    city: str
    state: str
    zip_code: str
    country: str

# --- 📞 Phone Type Enum ---
class PhoneType(str, Enum):
    MOBILE = "MOBILE"
    LANDLINE = "LANDLINE"
    FAX = "FAX"

# --- 📞 Phone Model (Nested) ---
class Phone(BaseModel):
    phone_number: str
    phone_type: PhoneType


# --- 🚻 Gender Enum ---
class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    CONFUSED = "CONFUSED"


# --- 🧑‍🚀 Profile Model (Base Identity Schema) ---
class Profile(BaseModel):
    uuid: Optional[UUID4] = Field(default=None, description="Unique identifier (UUID)")
    id: int

    phone: Optional[Phone] = Field(default=Phone)
    address: Optional[Address] = Field(default=Address)
    email: EmailStr
    website: Optional[HttpUrl] = Field(default=None)
    social_media: Optional[Dict[str, HttpUrl]] = Field(default=None, description="Social media links)")
    tags: List[str] = Field(default_factory=list, description="Tags for queries")
    notes: Optional[str] = Field(default=None, description="Additional notes or comments")

    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now(UTC))]
    updated_at:  Annotated[datetime, Field(default_factory=lambda: datetime.now(UTC))]

# --- 🧑‍🚀 Person Model (Base Identity Schema) ---
class Person(Profile):

    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(default=None)
    suffix: Optional[str] = Field(default=None)
    nickname: Optional[str] = Field(default=None)

    birth_date: Optional[date] = Field(default=None)
    hire_date: Optional[date] = Field(default=None)
    termination_date: Optional[date] = Field(default=None)
    rehire_date: Optional[date] = Field(default=None)
    gender: Optional[Gender] = Field(default=None)

# --- 🏢 Organization Model (inherits Profile) ---
class Organization(Profile):
    """Organization Model (inherits Profile)"""
    type: str = Field(default="organization", description="Type of organization")
    name: str = Field(..., description="Name of the organization")
    tax_id: Optional[str] = Field(default=None, description="Tax ID")
    industry: Optional[str] = Field(default=None, description="Industry type")
    poc: Optional[Person] = Field(default=None, description="Point of contact person")

# --- 🔐 User Model (inherits Person) ---
class User(Person):
    username: str
    password: str  # Consider securing with hashing/secret-handling later
    is_active: bool = Field(default=True, description="Is user active?")

# --- 🧑‍💼 Customer Model (inherits Person, adds customer-specific fields) ---
class Customer(Person):
    loyalty_points: int = Field(default=0, description="Customer loyalty/rewards points")
    preferred_store_id: Optional[int] = Field(default=None, description="Preferred store 'number'")
    preferences: Dict[str, Any] = Field(default_factory=dict, description="Cust prefs")
    notes: Optional[str] = Field(default=None, description="Additional notes")

# --- 🧑‍🏭 Employee Model (inherits Person, adds assignments) ---
class Employee(Person):
    stores: List["Store"] = Field(default_factory=list)
    positions: List[str] = Field(default_factory=list) #! need to define Position model later

# --- 🏢 Owner Model (inherits Person or Organization) ---
class Owner(Person | Organization):
    """Owner Model (inherits Person or Organization)"""
    owner_tag: str = Field(default="CORPORATE", description="Owner tag for the store")
    type: str = Field(default="owner", description="Type of owner (Person or Organization)")
    name: str = Field(..., description="Name of the owner")
    tax_id: Optional[str] = Field(default=None, description="Tax ID for the owner")
    industry: Optional[str] = Field(default=None, description="Industry type for the owner")
    poc: Optional[Person] = Field(default=None, description="Point of contact person for the owner")

# --- 🏬 Store Model (Pydantic 2.0-compliant) ---
class Store(BaseModel):
    """Store Model """

    id: int = Field(..., description="Internal store ID")
    uuid: Annotated[UUID, Field(default_factory=uuid4)]  #for DW
    store_id: str = Field(..., description="Franchise store number", max_length=12)

    owner_id: Optional[str] = Field(default="CORPORATE", description="Owner/Company")
    territory_id: Optional[str] = Field(default="MAIN", description="Territory group")
    brand_id: Optional[int] = Field(default=0, description="Concept or brand ID")

    #Often these 2 are the same but not necessarily
    store_name: Optional[str] = Field(default=None, description="Store name")
    store_location: Optional[str] = Field(default=None, description="Called location")

    created_by: Optional[str] = Field(default=None)
    updated_by: Optional[str] = Field(default=None)
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now(UTC))]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now(UTC))]

    model_config = ConfigDict(
        populate_by_name=True,

        # Replace to do camelCase conversion
        # alias_generator=lambda x: x.replace("_", ""),
        alias_generator=lambda x: ''.join([x.split('_')[0]] + [s.capitalize() for s in x.split('_')[1:]]),

        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
        },
        schema_extra={
            "example": {
                "id": 69,
                "store_no": "001",
                "owner_id": "CORPORATE",
                "territory_id": "MAIN",
                "brand_id": 789,
                "store_name": "Main Store",
                "store_location": "123 Main St, Anytown, USA",
                "created_by": "admin",
                "updated_by": "admin",
                "created_at": "2025-06-29T12:00:00",
                "updated_at": "2025-06-29T12:30:00"
            }
        }
    )
