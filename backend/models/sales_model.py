"""Generally will partition models per 'components'"""

### models.py
from sqlmodel import SQLModel, Field
from datetime import date


class Stores:
    id: int | None = Field(default=None, primary_key=True)


class Owners:
    id: int | None = Field(default=None, primary_key=True)


class Franchise:
    id: int | None = Field(default=None, primary_key=True)


class Sales(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date_business: date
    store_no: int
    loc_alias: str
    city: str
    state: str
    zip: str
    net_sales: float
    gross_sales: float
    sales_tax: float
    trans_cnt: int
    avg_ticket_price: float
    cust_cnt: int
    labor_pct: float
    adj_food_cost_pct: float


# *** Menu/'recipe' and Inventory
class Menu_Items:
    id: int | None = Field(default=None, primary_key=True)


class Menu_LineItems:
    id: int | None = Field(default=None, primary_key=True)


class Inventory_Items:
    id: int | None = Field(default=None, primary_key=True)


class Inventory_Measures:
    id: int | None = Field(default=None, primary_key=True)


class Inventory_Orders:
    id: int | None = Field(default=None, primary_key=True)


class Inventory_Invoices:
    id: int | None = Field(default=None, primary_key=True)


# *** Labor / Scheduling
class Labor_Shifts:
    id: int | None = Field(default=None, primary_key=True)


class Labor_Payroll:
    id: int | None = Field(default=None, primary_key=True)


class Staffing:
    id: int | None = Field(default=None, primary_key=True)


class Schedules:
    id: int | None = Field(default=None, primary_key=True)
