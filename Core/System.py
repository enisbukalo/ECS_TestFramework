from abc import ABC, abstractmethod
from typing import Set

from .Types import EntityId


class System(ABC):
    """
    Base class for all systems in the ECS.
    Systems contain the logic to process entities with specific components.
    """

    def __init__(self):
        self.enabled: bool = True
        self.priority: int = 0
        self._entities: Set[EntityId] = set()

    @abstractmethod
    def update(self, dt: float) -> None:
        """
        Update system logic. Must be implemented by derived classes.

        Args:
            dt: Delta time since last update in seconds
        """

    def add_entity(self, entity_id: EntityId) -> None:
        """Add an entity to be processed by this system"""
        self._entities.add(entity_id)

    def remove_entity(self, entity_id: EntityId) -> None:
        """Remove an entity from this system"""
        self._entities.discard(entity_id)

    def clear_entities(self) -> None:
        """Remove all entities from this system"""
        self._entities.clear()

    @property
    def entities(self) -> Set[EntityId]:
        """Get the set of entities processed by this system"""
        return self._entities.copy()
