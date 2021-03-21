import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def convert_to_binary(df, col):
    """Converts binary values t and f into 1 and 0 values and nan values into 0."""
    df[col] = df[col].replace({"t": 1, "f": 0, "nan": "NaN"}).fillna(0)
    return df[col]

def create_dummy_cols(df, cat_cols, dummy_na):
    """Creates dummy variables from categorical variables"""
    for col in cat_cols:
        try:
            dummy_df = pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)
            df=pd.concat([df.drop(col, axis=1), dummy_df], axis=1)
        except:
            continue
    return df

def map_substring(s, dict_map):
    """Map dictionary values to keys if a column contains the dictionary keys"""
    for key in dict_map.keys():
        if key in s.lower(): return dict_map[key]
    return 'other'

def remove_special_char(df, col):
    """Removes special characters such as % and $ from numeric variables and converts them into float"""
    df[col] = df[col].replace(regex = True, to_replace = r'[^0-9.\-]', value=r'')
    df[col] = df[col].astype("float")
    return df[col]


def plot_heatmap(df, figsize=(20,20)):
    """
    Creates a heatmap of correlations between features in the df.
    """
    # Set the style of the visualization
    sns.set(style="white")
    # Create a covariance matrix
    corr = df.corr()
    # Generate a mask the size of our covariance matrix
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=figsize)
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, vmax=corr[corr != 1.0].max().max());


