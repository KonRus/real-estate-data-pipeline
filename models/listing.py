from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Listing:

    source: str
    title: Optional[str]
    price: Optional[int]
    area: Optional[float]
    city: Optional[str]
    district: Optional[str]
    rooms: Optional[int]
    url: Optional[str]