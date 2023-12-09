import requests
import numpy as np
import pyFoam
import waverange as wrg
from download_file import download_file

def decode_data(url, header_file, reconstructed_file):
    wrdec = wrg.wrdec()
    reconstructed_data = wrdec.decode('output.wrb', 'header.wrh',
    'reconstructed.dat')
    print(reconstructed_data)