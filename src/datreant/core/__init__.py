# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# datreant.core

"""
datreant.core --- persistent, pythonic trees for heterogeneous data
===================================================================

.. SeeAlso:: :class:`datreant.core.treants.Treant`

"""

# Bring some often used objects into the current namespace
from .manipulators import discover
from .treants import Treant
from .trees import Veg, Leaf, Tree
from .collections import View, Bundle

__all__ = ['Treant', 'Tree', 'Leaf', 'Bundle', 'discover', 'Veg',
           'attach', 'View']
__version__ = "0.8.0-dev"  # NOTE: keep in sync with RELEASE in setup.py
