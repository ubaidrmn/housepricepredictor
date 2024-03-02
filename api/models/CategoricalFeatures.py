from pydantic import BaseModel
from typing import List


class CategoricalFeatures(BaseModel):
    property_types: List[str]
    locations: List[str]
    cities: List[str]
