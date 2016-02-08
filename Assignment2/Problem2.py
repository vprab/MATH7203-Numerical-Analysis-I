__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import soundfile as sf


def determine_number(mags):
    rows = [697, 770, 852, 941]
    cols = [1209, 1336, 1477]
    vals = [[1, 2, 3],[4, 5, 6],[7,8,9],['*',0,'#']]

    max_row = max(range(len(rows)), key=lambda i:mags[rows[i]])
    max_col = max(range(len(cols)), key=lambda j:mags[cols[j]])

    return vals[max_row][max_col]

if __name__ == "__main__":
    files = ['DtmfA.ogg', 'DtmfB.ogg', 'DtmfC.ogg', 'DtmfD.ogg', 'DtmfE.ogg', 'DtmfF.ogg', 'DtmfG.ogg']

    for f in files:
        data, samplerate = sf.read(f)
        fft_data = np.fft.fft(data)
        magnitude = np.abs(fft_data)

        print determine_number(magnitude)

