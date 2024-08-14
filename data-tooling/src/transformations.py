
# transformations.py

# ========== IMPORTS ========== #
import pandas as pd

# ========== MAIN TRANSFORMATION FUNCTION ========== #

def apply_transformations(df, transformations):
    """Apply a list of transformations to the DataFrame."""
    for transformation in transformations:
        if transformation == 'missing_values':
            # Introduce missing values
            df = introduce_missing_values(df)
        elif transformation == 'duplicate_rows':
            # Add duplicate rows
            df = add_duplicate_rows(df)
        elif transformation == 'incorrect_data':
            # Insert incorrect data
            df = insert_incorrect_data(df)
        # Add more transformations as needed
        else:
            print(f"Unknown transformation: {transformation}")

    return df

# ========== INDIVIDUAL TRANSFORMATIONS ========== #

# Function to introduce missing values
def introduce_missing_values(df):
    """Randomly introduce missing values into the DataFrame."""
    for col in df.columns:
        df.loc[df.sample(frac=0.1).index, col] = None
    return df

# Function to add duplicate rows
def add_duplicate_rows(df):
    """Randomly add duplicate rows to the DataFrame."""
    df = pd.concat([df, df.sample(frac=0.1)], ignore_index=True)
    return df

# Function to insert incorrect data
def insert_incorrect_data(df):
    """Randomly insert incorrect data into the DataFrame."""
    for col in df.columns:
        df.loc[df.sample(frac=0.1).index, col] = 'incorrect'
    return df


