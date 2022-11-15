"""Test fixtures."""
from typing import Any

import pandas as pd
import pytest
from typeguard import typechecked
from typeguard.importhook import install_import_hook

from house_sales.config.core import config
from house_sales.processing.data_manager import load_dataset


def pytest_configure() -> None:
    """Install import hook."""
    install_import_hook("house_sales")


def pytest_runtest_call(item: Any) -> None:
    """Decorate every test function with typeguard's typechecked() decorator."""
    test_func = getattr(item, "obj", None)
    if test_func is not None:
        # setattr(item, "obj", typechecked(test_func))
        item.obj = typechecked(test_func)


@pytest.fixture()
def sample_input_data() -> pd.DataFrame:
    """Sample input fixture."""
    return load_dataset(file_name=config.app_config.test_data_file)
