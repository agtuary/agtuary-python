from dataclasses import dataclass
from typing import Any, List, Optional, Union
from numbers import Number


@dataclass
class Region:
    id: str
    user: str
    team: str
    project: str
    created: Optional[str] = None
    cropType: Optional[str] = None
    values: Optional[Any] = None
    geojson: Optional[str] = None
    address: Optional[str] = None
    state: Optional[str] = None
    broadacre: Optional[str] = None
    lga: Optional[str] = None
