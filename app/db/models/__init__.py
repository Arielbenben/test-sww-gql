from sqlalchemy.orm import declarative_base

Base =declarative_base()

from .mission import Mission
from .country import Country
from .city import City
from .target import Target
from .targettypes import TargetType
