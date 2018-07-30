"""Functions for download and preprocess data."""

import os
import pandas as pd

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