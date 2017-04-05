#!/usr/bin/python2
# -*- coding: utf-8 -*-
from mps import *
from arge import *
import tempfile

temp = tempfile.mktemp()

mps=Mps()
mps.paket_kur("gvim")

