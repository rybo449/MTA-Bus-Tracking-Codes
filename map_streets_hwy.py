import shapefile, sys
import matplotlib.pyplot as m_plot
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.ticker import MaxNLocator

if __name__=='__main__':
    if len(sys.argv)!=3:
        print 'Usage: python %s <SHAPEFILE_PREFIX> <OUTPUT_PDF>' % sys.argv[0]
        sys.exit(1)


    fig = m_plot.figure(figsize=(4.5, 7.2))


    fig.suptitle('New York City Street Maps', fontsize=20)


    ax = fig.add_subplot(111, aspect='equal')


    sf = shapefile.Reader(sys.argv[1])


    for sr in sf.shapeRecords():


        color = '0.8'


        if sr.record[1]!='      ': color='orange'


        parts = list(sr.shape.parts) + [-1]


        for i in xrange(len(sr.shape.parts)):
            path = Path(sr.shape.points[parts[i]:parts[i+1]])
            patch = PathPatch(path, edgecolor=color, facecolor='none', lw=0.5, aa=True)
            ax.add_patch(patch)


    ax.set_xlim(sf.bbox[0], sf.bbox[2])
    ax.set_ylim(sf.bbox[1], sf.bbox[3])


    ax.xaxis.set_major_locator(MaxNLocator(3))


    fig.savefig(sys.argv[2])
