"""crud.py

# For now put  these in one
#but later Sales, Profiles, Menu_Items, Inventory, Labor etc
#will be the modules (componenets?)

"""

from fastapi import APIRouter, Request, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Tuple, List, Optional  # for Hints/std use

from ...database.db_SQLModel import get_session  # probably won't use here
from ...models.sales_model import Sales  # import models

router = APIRouter


# Placeholder for now
def get_sales_data():
    with get_session() as session:
        return session.exec(Sales).limit(100).all()


# * MongoDB Template from Aleks

# # default - now /test
# @router.get("/test", response_description="List all cars")

# # Now true root is List All Cars
# @router.get("/", response_description="List all cars")
# async def list_all_cars(
#     request: Request,
#     min_price: int = 0,
#     max_price: int = 100000,
#     brand: Optional[str] = None,
#     # now add pagination
#     page: int = 1,
# ) -> List[CarDB]:

#     RESULTS_PER_PAGE = 25
#     skip = (page - 1) * RESULTS_PER_PAGE

#     query = {
#         "price": {"$lt": max_price, "$gt": min_price}
#     }  # * this is a mongo command usage
#     if brand:
#         query["brand"] = brand

#     # Modified to add pagination
#     fully_query = (
#         request.app.mongodb["cars1"]
#         .find(query)
#         .sort("_id", 1)
#         .skip(skip)
#         .limit(RESULTS_PER_PAGE)
#     )

#     results = [CarDB(**raw_car) async for raw_car in full_query]
#     return results


# # create new car
# @router.post("/", response_description="Add new car")
# async def create_car(request: Request, car: CarBase = Body(...)):

#     # * used to convert a Pydantic model instance into a JSON-serializable dictionary
#     # * This is mainly because of ObjectID to string
#     car_dict = jsonable_encoder(car)

#     # will first create the new car and then see if it worked right....
#     new_car = await request.app.mongodb["cars1"].insert_one(car_dict)
#     created_car = await request.app.mongodb["cars1"].find_one(
#         {"_id": new_car.inserted_id}
#     )

#     # now return the status by showing the 'document' as Py Dictionary
#     return JSONResponse(status_code=status.HTTP_201_CREATE, content=created_car)


# # show a single car (by ID)
# @router.get("/{id}", response_description="Get a single car")
# async def show_car(id: str, request: Request):
#     if (car := await request.app.mongodb["cars1"].find_one({"_id": id})) is not None:
#         return CarDB(**car)
#     raise HTTPException(status_code=404, detail=f"Car with {id} not found")


# # * Update a car - use PATCH
# @router.patch("/", response_description="Update car")
# async def update_car(id: str, request: Request, car: CarUpdate = Body(...)):
#     await request.app.mongodb["cars1"].update_one(
#         {"_id": id}, {"$set": car.dict(exclude_unset=True)}
#     )
