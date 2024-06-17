from __future__ import annotations

__all__ = (
    "login",
    "str_to_html",
    "to_html",
)

from collections.abc import Callable
from typing import TYPE_CHECKING

import pytest
from django.template import Context, Engine

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, TypeVar

    T = TypeVar("T", default=None)
    P = ParamSpec("P")

# flake8: noqa


def login() -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Login ``client`` as a user

    .. code-block::

        @login
        def test_teacher_thing(client):
            # client is logged in
    """
    return pytest.mark.usefixtures(f"client_login")


# we define these helper functions to avoid hardcoding
# stuff like the html escape code for '
def to_html(s: str, ctx: dict[str, str]) -> str:
    """Convert template code to an html string

    .. code-block:: pycon

        >>> template_logic = "Hello, my name is {{ username }}!"
        >>> context = {"username": "2027adeshpan"}
        >>> to_html(template_logic, context)
        'Hello, my name is 2027adeshpan!'

    Args:
        s: The template string (see :class:`~django.template.Template`)
        ctx: The variables/context to use for ``s`` (see :class:`~django.template.Context`)
    """
    template = Engine().from_string(s)
    context = Context(ctx)
    return template.render(context)


def str_to_html(s: str) -> str:
    """Converts a string to it's html representation

    .. code-block:: pycon

        >>> text = "It's annoying to remember HTML escape codes"
        >>> str_to_html(text)
        'It&#x27;s annoying to remember HTML escape codes'
    """
    template = "{{ var }}"
    ctx = {"var": s}
    return to_html(template, ctx)
