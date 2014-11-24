
# API Key: efaaaff3-ebd3-48b6-a80c-6affb45f8812
import shapefile, sys
import matplotlib.pyplot as m_plot
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.ticker import MaxNLocator
import urllib2
import json
import pyproj
def printResults(data):
	theJSON = json.loads(data)
	count = 0
	I = theJSON["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	
	count = len(I)
	proj = pyproj.Proj(init = "esri:26918")
	
	points = []
	for i in xrange(count):
		K = I[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
		J = I[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]		
		points.append(proj(J,K))
		

	return points,count
if __name__=='__main__':
    if len(sys.argv)!=5:
        print 'Usage: python %s xxx-xxx-xxx-xxx-xxx M20 <SHAPEFILE_PREFIX> <OUTPUT_PDF>' % sys.argv[0]
        sys.exit(1)

    line = str(sys.argv[2])
    key = str(sys.argv[1])
    urlData = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="+ key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ line
    webUrl = urllib2.urlopen(urlData)


    fig = m_plot.figure(figsize=(4.5, 7.2))

    title = "Current "+line+" Bus Locations"
    fig.suptitle(title, fontsize=20)


    ax = fig.add_subplot(111, aspect='equal')


    sf = shapefile.Reader(sys.argv[3])


    for sr in sf.shapeRecords():


        color = '0.8'




	if sr.record[1]!='      ': color='orange'

        parts = list(sr.shape.parts) + [-1]


        for i in xrange(len(sr.shape.parts)):
            path = Path(sr.shape.points[parts[i]:parts[i+1]])
            patch = PathPatch(path, edgecolor=color, facecolor='none', lw=0.5, aa=True)
            ax.add_patch(patch)
    points = []
    if(webUrl.getcode() == 200):
	data = webUrl.read()
	#print data
	points, num = printResults(data)
    for i in points:


	ax.plot(i[0],i[1],'bo', ms = 5, color = "cyan")
    '''print points
    x,y = zip(*points)
    ax.plot(y,x,'bo',color = "blue", ms = 10)'''

    ax.set_xlim(sf.bbox[0], sf.bbox[2])
    ax.set_ylim(sf.bbox[1], sf.bbox[3])
    

    ax.xaxis.set_major_locator(MaxNLocator(3))
    

    fig.savefig(sys.argv[4])
    
