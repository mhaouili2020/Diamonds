import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import os

def load_diamonds_data(diamonds_path):
   csv_path = os.path.join(diamonds_path, "diamonds.csv")
   return pd.read_csv(csv_path)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    diamond = load_diamonds_data('')

    carat_ix, cut_ix, color_ix, clarity_ix, depth_ix, table_ix, price_ix, x_ix, y_ix, z_ix, =[
        list(diamond.columns).index(col)
        for col in ("carat", "cut", "color", "clarity", "depth", "table", "price", "x", "y", "z")]

    