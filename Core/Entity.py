from typing import Dict

from .Types import EntityId, ComponentId
from .Component import Component


class Entity:
    """
    Represents an entity in the ECS system.
    An entity is a collection of components.
    """

    def __init__(self, entity_id: EntityId):
        self.id: EntityId = entity_id
        self.components: Dict[ComponentId, Component] = {}
        self.is_active: bool = True

    def add_component(self, component: Component) -> None:
        """Add a component to this entity"""
        self.components[component.id] = component

    def remove_component(self, component_id: ComponentId) -> None:
        """Remove a component from this entity"""
        self.components.pop(component_id, None)

    def has_component(self, component_id: ComponentId) -> bool:
        """Check if entity has a specific component"""
        return component_id in self.components

    def has_components(self, *component_ids: ComponentId) -> bool:
        """Check if entity has all specified components"""
        return all(self.has_component(cid) for cid in component_ids)

    def get_component(self, component_id: ComponentId) -> Component | None:
        """Get a component from this entity"""
        return self.components.get(component_id)
