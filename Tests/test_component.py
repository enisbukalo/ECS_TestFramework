from dataclasses import dataclass

from Core import Component


def test_component_initialization():
    """Test that components are initialized with correct IDs"""
    # Reset the component ID counter before test
    Component._next_id = 0

    # Create multiple components
    comp1 = Component()
    comp2 = Component()
    comp3 = Component()

    # Test sequential ID assignment
    assert comp1.id == 0
    assert comp2.id == 1
    assert comp3.id == 2


def test_component_unique_ids():
    """Test that each component gets a unique ID"""
    # Reset the component ID counter
    Component._next_id = 0

    # Create a list of components
    components = [Component() for _ in range(5)]

    # Get all IDs
    ids = [comp.id for comp in components]

    # Test that all IDs are unique
    assert len(set(ids)) == len(ids)
    assert sorted(ids) == list(range(5))


def test_component_inheritance():
    """Test that component inheritance works correctly"""
    # Reset the component ID counter
    Component._next_id = 0

    @dataclass
    class TestComponent(Component):
        value: int

        def __init__(self, value: int):
            super().__init__()
            self.value = value

    # Create custom components
    test_comp1 = TestComponent(42)
    test_comp2 = TestComponent(24)

    # Test ID assignment
    assert test_comp1.id == 0
    assert test_comp2.id == 1

    # Test custom attributes
    assert test_comp1.value == 42
    assert test_comp2.value == 24


def test_component_type_hints():
    """Test that generic type hints work"""

    @dataclass
    class IntComponent(Component[int]):
        value: int

        def __init__(self, value: int):
            super().__init__()
            self.value = value

    @dataclass
    class StrComponent(Component[str]):
        value: str

        def __init__(self, value: str):
            super().__init__()
            self.value = value

    int_comp = IntComponent(42)
    str_comp = StrComponent("test")

    assert isinstance(int_comp, Component)
    assert isinstance(str_comp, Component)
    assert int_comp.value == 42
    assert str_comp.value == "test"
