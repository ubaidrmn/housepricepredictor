from pydantic import BaseModel


class LabelVector(BaseModel):
    price: str
