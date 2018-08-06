"""Utility functions."""

import os
import pandas as pd
import numpy as np

ISL_URL = 'http://www-bcf.usc.edu/~gareth/ISL'
ALT_URL = 'https://raw.githubusercontent.com/selva86/datasets/master'
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

def get_data(filename: str, reload: bool = False) -> pd.DataFrame:
    """Get data from ISL website and store locally for future."""
    
    from urllib.request import urlretrieve, urlopen

    
    src_path = os.path.join(ISL_URL, filename)
    
    try:
        urlopen(src_path)
    except:
        src_path = os.path.join(ALT_URL, filename)
    
    dst_path = os.path.join(DATA_PATH, filename)

    # Download file.
    if not os.path.exists(dst_path) or reload:
        urlretrieve(src_path, dst_path)
        
    df = pd.read_csv(dst_path)
    
    return df

def make_mesh(X:np.ndarray, step_size:float=0.1, dim:int=2, return_2d=False) -> np.ndarray:
    """Make mesh grid that covers the range of input features X.
    
    A meshgrid is the coordinates of all the points in a grid
        arranged in a grid form.
    
    Example:
        x_mesh, (X0, X1) = make_mesh(X)
        plt.pcolormesh(X0, X1, x_mesh.mean(axis=-1))
    
    Args:  
        X : feature matrix [samples, features]
        step_size : step size along single dimension of the grid
        dim : first n dimensions to make grid from
    
    Return:
        if return_2d:
            x_mesh : [samples*dim, dim]
        else:
            x_mesh : [samples along X_0, ..., samples along X_i, dim]
            
        x_samples : list of length = dim
    """
    
    x_min = np.min(X, axis=0)
    x_max = np.max(X, axis=0)
    x_samples = [np.arange(mi-step_size, ma+step_size, step_size)
                 for mi, ma in zip(x_min, x_max)]
    x_mesh = np.stack(np.meshgrid(*x_samples[:dim]), axis=-1)
    
    if return_2d:
        return x_mesh.reshape(-1, dim), x_samples[:dim]
    else:
        return x_mesh, x_samples[:dim]