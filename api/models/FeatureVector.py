from pydantic import BaseModel


class FeatureVector(BaseModel):
    property_type: str
    location: str
    city: str
    baths: int
    bedrooms: int
    area_marla: float
