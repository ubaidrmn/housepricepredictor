from pydantic import BaseModel
from typing import List, Dict


class CategoricalFeatures(BaseModel):
    property_types: List[str]
    locations: Dict[str, List[str]]
    cities: List[str]
