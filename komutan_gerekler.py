#!/usr/bin/env python2
# Copyright (c) 2017 Milis İşletim Sistemi
# Author: milisarge
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <http://www.gnu.org/licenses/>.

import os
import time
import sys
import site

paketd=site.getsitepackages()
yukluler=os.listdir(paketd[0])
mps_gerekler="/tmp/komutan.gerekler"
kur="pip2 install "
mpskur="mps kur "
kontrol=["paho-mqtt"]
mpskontrol=["python-yaml","python3-yaml"]

for yuklu in yukluler:
	for kont in kontrol:
		if kont in yuklu:
			print (kont,"kurulu")
			kontrol.remove(kont)
for kont in kontrol:
	os.system(kur+kont)	

for mpsk in mpskontrol:
	if os.path.exists("/var/lib/pkg/DB/"+mpsk) is False:
		os.system("mps kur "+mpsk)
	else:
		print(mpsk,"zaten kurulu")


		
