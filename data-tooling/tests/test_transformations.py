
import pytest
import pandas as pd
from src.transformations import apply_transformations

# Sample data for testing
@pytest.fixture
def sample_dataframe():
    data = {
        'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e'],
    }
    return pd.DataFrame(data)

# Test missing values transformation
def test_apply_missing_values(sample_dataframe):
    transformations = ['missing_values']
    df_transformed = apply_transformations(sample_dataframe, transformations)
    assert df_transformed.isnull().values.any(), "No missing values were introduced."

# Test duplicate rows transformation
def test_apply_duplicate_rows(sample_dataframe):
    transformations = ['duplicate_rows']
    df_transformed = apply_transformations(sample_dataframe, transformations)
    assert len(df_transformed) > len(sample_dataframe), "Duplicate rows were not added."

# Test incorrect data transformation
def test_apply_incorrect_data(sample_dataframe):
    transformations = ['incorrect_data']
    df_transformed = apply_transformations(sample_dataframe, transformations)
    assert '???' in df_transformed.values, "Incorrect data was not inserted."

