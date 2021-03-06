# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import qiime2
import sys
import skbio
import numpy as np

a = qiime2.Artifact.load(sys.argv[1]).view(skbio.DistanceMatrix)
b = qiime2.Artifact.load(sys.argv[2]).view(skbio.DistanceMatrix)

assert np.all(a.ids == b.ids)
assert np.allclose(a.data, b.data)
