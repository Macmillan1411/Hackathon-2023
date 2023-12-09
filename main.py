import requests
import numpy as np
import pyFoam
import waverange as wrg
from download_file import download_file

def process_file(url, operation, tolerance=1e-16):
    data = download_file(url)
    if operation == 'encode':
        data = np.asarray(data)
        wrenc = wrg.wrenc()
        wrenc.encode(data, 'output.wrb', 'header.wrh', tolerance)
    elif operation == 'decode':
        wrdec = wrg.wrdec()
        reconstructed_data = wrdec.decode('output.wrb', 'header.wrh',
        'reconstructed.dat')
        print(reconstructed_data)
    else:
        raise Exception('Invalid operation: {}'.format(operation))
        if __name__ == '__main__':
            url = 'https://example.com/data.dat'
            operation = 'encode'
            process_file(url, operation)