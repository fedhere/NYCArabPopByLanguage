from __future__ import print_function, division
import pandas as pd
import geopandas as gpd
import pylab as pl
import matplotlib as mpl
import optparse


def discrete_cmap(N, base_cmap=None):
    '''Create an N-bin discrete colormap from the specified input map
    from Jake VanDerPlas with minor modifications to let it with with divergent cmaps
    https://gist.github.com/jakevdp/91077b0cae40f8f8244a#file-discrete_cmap-py-L18
    Arguments:
    N : number of colors
    base_cmap : a pylab cmap name (string) or pylab cmap object'''
    # Note that if base_cmap is a string or None, you can simply do
    #    return pl.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance:

    from matplotlib.colors import LinearSegmentedColormap
    base = pl.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return LinearSegmentedColormap.from_list(cmap_name, color_list, N)


def choroplethNYC(df, column=None, cmap='viridis', ax=None, cb=True, kind='continuous',
                  spacing=False, lw=1, width=None, side=False, loc=1):
    '''creates a choropleth from a dataframe column - NYC tuned
    Arguments:
    df : a GeoDataFrame
    column : a column name 
    cmap : colorman name (string optional)
    ax : axis in figure object (string, optiona, is None a figure is created)
    cb : put the color bar. Bool, default is True
    kind : 
    spacing : the spacing for the colorbar (bool, optional)
    lw : line width (float, optional, default is 1)
    width : with width of the color bar (figure frction, float)
    side : default False is left (west), True switches to right (east). If a float is passed that is the location
    Returns the figure and the axis, for further manipulation
    '''
    if ax == None:
        ax = pl.figure(figsize=(10, 10)).add_subplot(111)
    if column == None:
        ax = df.plot(cmap=cmap, alpha=1, ax=ax, linewidth=lw)
    else:
        ax = df.dropna(subset=[column]).plot(column=column,
                                             cmap=cmap, alpha=1, ax=ax,
                                             linewidth=lw)
    vmin, vmax = min(df[column].values), max(df[column].values)
    ax.axis('off')
    fig = ax.get_figure()

    if column == None:
        return fig, ax

    #if  discrete variable you want steps cb
    if kind is 'discrete':
        nc = df[column].unique()
        cmap = discrete_cmap(len(nc), base_cmap=cmap)

    # location of colorbar is tuned to the shape of NYC: sits above SI, west of Manhattan
    if cb:
        if not side:
            x0 = 0.2
        elif isinstance(side, float):
            x0 = side
        else:
            x0 = 0.9
        if not width:
            width = 0.03

        cax = fig.add_axes([x0, 0.41, width, 0.44])

        if kind is 'discrete':
            sm = mpl.colorbar.ColorbarBase(ax=cax, cmap=cmap,
                                norm=pl.Normalize(vmin=vmin - .5, vmax=vmax + .5),
                                #spacing='uniform',
                                orientation='vertical')

        else:
            sm = mpl.colorbar.ColorbarBase(ax=cax, cmap=cmap,
                                norm=pl.Normalize(vmin=vmin, vmax=vmax),
                                ticks=range(spacing + 1),
                                spacing='uniform',
                                orientation='vertical')
        sm._A = []

        if  kind is 'discrete':
            cb = fig.colorbar(sm, cax=cax, ticks=np.linspace(vmin, vmax, len(nc)))
            cb.ax.set_yticklabels(['%s' % (c) for c in np.sort(nc)])
        else:
            cb = fig.colorbar(sm, cax=cax)
    return fig, ax


if __name__ == '__main__':
    parser = optparse.OptionParser(usage="choroplathNYC <path to shapefile> <column name>", conflict_handler="resolve")
    parser.add_option('-d', '--discrete', default=False, action="store_true",
	                      help='discrete steps color bar')
    parser.add_option('-c', '--cmap', default='viridis', type='string',
	                      help='matplotlib colormap name')
    
    

    options,  args = parser.parse_args()
    
    if len(args) == 0:
	options, args = parser.parse_args(args=['--help'])
	sys.exit(0)
    if args[0].endswith("shp"):
        gdf = gpd.read_file(args[0])
    else:
        options, args = parser.parse_args(args=['--help'])
	sys.exit(0)
    if args[1] in gdf.columns:
        choroplethNYC(args[0], args[1])
    
        
