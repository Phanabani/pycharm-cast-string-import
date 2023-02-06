from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    # This import is marked as unused and will be optimized away, even though
    # it is being used by the type system in the `cast` on line 16.
    #
    # If `ValueContainer` were used as a type annotation along with
    # `from __future__ import annotations`, it would not be marked as unused
    from .value_container import ValueContainer


def get_value(obj: object):
    if not hasattr(obj, "item"):
        return
    # We need to use a string type here because otherwise we'd get a NameError
    obj = cast("ValueContainer", obj)
    # The following line should give an error because we have correctly cast
    # `obj` to `ValueContainer` using a string type
    obj.this_attr_doesnt_exist
    # The following line should not give an error for the same reason as above
    return obj.value
