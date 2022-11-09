"""Testing custom transformers."""
from house_sales.config.core import config
from house_sales.processing.features import TemporalVariableTransformer


def test_temporal_variable_transformer(sample_input_data):
    """Test the temporal variable transformer."""
    # Given
    transformer = TemporalVariableTransformer(
        variables=config.model_config.temporal_vars,  # YearRemodAdd
        reference_variable=config.model_config.ref_var,
    )
    assert sample_input_data["YearRemodAdd"].iat[0] == 1961

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["YearRemodAdd"].iat[0] == 49
