from __future__ import annotations

from typing import Any


class PytestRunner:
    """Runs pytest to discover and run tests."""

    def __init__(
        self, verbosity: int = 1, *, failfast: bool = False, keepdb: bool = False, **kwargs: Any
    ):
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb

    @classmethod
    def add_arguments(cls, parser) -> None:
        """Add arguments to the parser."""
        parser.add_argument(
            "--keepdb", action="store_true", help="Preserves the test DB between runs."
        )

    def run_tests(self, test_labels: list[str], **kwargs: Any) -> int:
        """Run pytest and return the exitcode.

        It translates some of Django's test command option to pytest's.
        """
        import pytest

        argv = []
        if self.verbosity == 0:
            argv.append("--quiet")
        if self.verbosity == 2:
            argv.append("--verbose")
        if self.verbosity == 3:
            argv.append("-vv")
        if self.failfast:
            argv.append("--exitfirst")
        if self.keepdb:
            argv.append("--reuse-db")

        argv.extend(test_labels)
        return pytest.main(argv)
