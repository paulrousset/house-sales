"""Test fixtures."""
import pandas as pd
import pytest

from house_sales.config.core import config
from house_sales.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data() -> pd.DataFrame:
    """Sample input fixture."""
    return load_dataset(file_name=config.app_config.test_data_file)
