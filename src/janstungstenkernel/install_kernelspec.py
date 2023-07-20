#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""Kernel installer"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

json ="""{"argv":["python","-m","janstungstenkernel", "-f", "{connection_file}"],
 "display_name":"Tungsten/Wolfram"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   id="Hexels SVG Export"
   version="1.1"
   viewBox="0 0 300 300"
   xml:space="preserve"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"><defs
   id="defs20" />
<g
   id="Root"
   transform="matrix(1.4423077,0,0,1.4423077,-249.51923,-109.61539)">

<g
   id="Layer 2">
<path
   d="m 208,80 -35,20 104,60 104,-60 -35,-20 -69,40 z"
   style="fill:#ff8300;fill-opacity:1"
   id="path9" />
<path
   d="m 173,100 v 40 l 69,40 v 80 l 35,20 V 160 Z"
   style="fill:#ff0000;fill-opacity:1"
   id="path11" />
<path
   d="m 381,100 -104,60 v 120 l 35,-20 v -80 l 69,-40 z"
   style="fill:#ffd000;fill-opacity:1"
   id="path13" />
</g>
</g></svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/janstungstenkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janstungstenkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janstungstenkernel')