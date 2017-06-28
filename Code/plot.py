#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

n = 200

def plot(s, r, R, xaxis, out):
    x = np.arange(0., s, s / n)
    xr = (x - r) / (R -r)
    y = (x <= r) + (r < x) * (x < R) * (xr - 1) ** 2 * (xr + 1) ** 2

    fig = plt.figure(figsize=(4, 2.7))
    plt.plot(x, y)

    ax = fig.axes[0]

    plt.tick_params(which='both', top='off')
    plt.yticks([0, 1])
    xvals, xlabels = zip(*xaxis)
    plt.xticks(xvals)
    ax.xaxis.set_major_formatter(FixedFormatter(xlabels))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.savefig(out)

s = 0.4
plot(s=s, r=0, R=0.15, out='img/cutoff.pdf', xaxis=[
    (0, '0'), (0.15, 'r = 0.15'), (s, str(s))
])

r = 0.2
R = 0.3
plot(s=s, r=r, R=R, out='img/theta.pdf', xaxis=[
    (0, '0'), (r, 'r = {}'.format(r)), (R, 'R = {}'.format(R)), (s, str(s))
])

