#!/usr/bin/python2
# -*- coding: utf-8 -*-
from mps import *
from arge import *
import tempfile
import filecmp
import subprocess

print "---",arger.komutCalistir("curl -s www &> /tmp/link_kontrol")
