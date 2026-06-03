from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")

class APIResponse(GenericModel, Generic[T]):
    result: Optional[T] = None
    status_code: int = 200
    message: str = "success"

APIResponse.model_rebuild()