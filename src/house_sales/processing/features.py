"""Custom feature transformers."""
from typing import List

import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin


class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
    """Temporal elapsed time transformer."""

    def __init__(self, variables: List[str], reference_variable: str):
        """Construct."""
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        """Fit method."""
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, x: pd.DataFrame) -> pd.DataFrame:
        """Transform method."""
        # so that we do not over-write the original dataframe
        x = x.copy()

        for feature in self.variables:
            x[feature] = x[self.reference_variable] - x[feature]

        return x


class Mapper(BaseEstimator, TransformerMixin):
    """Categorical variable mapper."""

    def __init__(self, variables: List[str], mappings: dict):
        """Construct."""
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.mappings = mappings

    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        """Fit method."""
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, x: pd.DataFrame) -> pd.DataFrame:
        """Transform method."""
        x = x.copy()
        for feature in self.variables:
            x[feature] = x[feature].map(self.mappings)

        return x
