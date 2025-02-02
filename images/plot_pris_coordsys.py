# -*- coding: utf-8 -*-
"""
This is a script for plotting the coordinate system used in Nagy et al. (2000)
together with the local system of the prism.
"""

import Gnuplot
import numpy as np

def main():

    gp = Gnuplot.Gnuplot(persist = 1)

    output = 'coordinate_sys_raw.ps'
    #gp("set term postscript")
    #gp('set output "%s"' % (output))
    gp('unset xtics; unset ytics; unset ztics')
    gp('unset border')
    gp('set size ratio 1')
    gp('set xrange [-1:1];set yrange [-1:1];set zrange [-1:1]')
    gp("set ticslevel 0")
    gp("set view 55,40")

    # The prism sistem
    x_pris = Gnuplot.PlotItems.Data([[0,0,0, 0.5,0,0]], \
                                   with_="vectors lt 1 lw 3", title=None)
    y_pris = Gnuplot.PlotItems.Data([[0,0,0, 0,0.5,0]], \
                                   with_="vectors lt 1 lw 3", title=None)
    z_pris = Gnuplot.PlotItems.Data([[0,0,0, 0,0,0.7]], \
                                   with_="vectors lt 1 lw 3", title=None)

    # The Nagy sistem
    x_nagy = Gnuplot.PlotItems.Data([[-0.5,-0.5,0.8, 0.5,0,0]], \
                                   with_="vectors lt 1 lw 3", title=None)
    y_nagy = Gnuplot.PlotItems.Data([[-0.5,-0.5,0.8, 0,0.5,0]], \
                                   with_="vectors lt 1 lw 3", title=None)
    z_nagy = Gnuplot.PlotItems.Data([[-0.5,-0.5,0.8, 0,0,-0.7]], \
                                   with_="vectors lt 1 lw 3", title=None)

    # Prism
    w = -0.2
    e = 0.2
    n = 0.2
    s = -0.2
    t = 0
    b = -0.8
    sides1 = [[[s,w,t],[n,w,t]],[[n,w,t],[n,e,t]],[[n,e,t],[s,e,t]],[[s,e,t],[s,w,t]], \
              [[s,w,b],[s,e,b]],[[s,e,b],[n,e,b]], \
              [[s,w,t],[s,w,b]],[[s,e,t],[s,e,b]],[[n,e,t],[n,e,b]]]
    sides2 = [[[n,w,t],[n,w,b]],[[n,w,b],[n,e,b]],[[n,w,b],[s,w,b]]]

    prismdata = []
    for line in sides1:
        prismdata.append(Gnuplot.PlotItems.Data(line, with_="l lt 1 lw 1.5", title=None))
    for line in sides2:
        prismdata.append(Gnuplot.PlotItems.Data(line, with_="l lt 2 lw 1.5", title=None))



    # make the plot
    gp.splot(\
        # Prism coord system
        x_pris, y_pris, z_pris, \
        # The Nagy sistem
        x_nagy, y_nagy, z_nagy, \
        # The prism
        *prismdata
    )




if __name__ == '__main__':
    main()