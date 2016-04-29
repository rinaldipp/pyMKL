from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library
standard_library.install_aliases()

import numpy as np
import scipy.sparse as sp
from ctypes import CDLL, cdll, RTLD_GLOBAL
from ctypes import POINTER, byref, c_int, c_longlong

path = 'libmkl_intel_lp64.dylib'
MKLlib = CDLL(path, RTLD_GLOBAL)

from .pardisoInterface import pardisoinit, pardiso
from .pardisoSolver import pardisoSolver
