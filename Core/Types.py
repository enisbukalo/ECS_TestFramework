from typing import TypeVar
from dataclasses import dataclass

# Basic type definitions
EntityId = int
ComponentId = int

# Type variable for generic components
T = TypeVar("T")


@dataclass
class EntityHandle:
    """Represents a handle to an entity in the ECS system"""

    id: EntityId
    is_active: bool = True
