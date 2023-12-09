import requests
import numpy as np
import pyFoam
import waverange as wrg
from download_file import download_file

def encode_data(url, output_file, header_file, tolerance=1e-16):
    data = download_file(url)
    data = np.asarray(data)
    wrenc = wrg.wrenc()
    wrenc.encode(data, output_file, header_file, tolerance)