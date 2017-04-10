#!/usr/bin/python2
# -*- coding: utf-8 -*-
from mps import *
from arge import *
import tempfile
import filecmp
import subprocess
import binascii
from imgurpython import ImgurClient

client_id = '873f9d40aa94a1d'
client_secret = '8e80e7eb2ce5559a225505993a2cc8f668e28ca8'

client = ImgurClient(client_id, client_secret)

# Example request
path="static/exit.png"
rid=client.upload_from_path(path, config=None, anon=True)
print rid["link"]
