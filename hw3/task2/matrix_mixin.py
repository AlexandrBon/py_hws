import numpy as np
import pickle

class Matrix(np.ndarray, pickle):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj
