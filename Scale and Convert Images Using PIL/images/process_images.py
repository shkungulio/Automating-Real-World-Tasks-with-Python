#!/usr/bin/env python3

import os
import glob
from PIL import Image

for x in glob.glob("ic*"):
	new_image = Image.open(x).convert("RGB")
	new_image.rotate(270).resize((128,128)).save("/opt/icons/" + x,"JPEG")
