import numpy as np
import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey

Sankey(flows=[ 0.50, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['Input', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[0, -1, 1, -1, 1, 0] ).finish()
plt.title("The default settings produce a diagram like this.")
plt.show()

#https://matplotlib.org/gallery/api/sankey_basics.html#sphx-glr-gallery-api-sankey-basics-py
