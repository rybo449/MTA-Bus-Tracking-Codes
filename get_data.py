# API Key: efaaaff3-ebd3-48b6-a80c-6affb45f8812
import urllib2
import json
import sys
def printResults(data):
	theJSON = json.loads(data)
	count = 0
	I = theJSON["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	#print I[1]	
	#print len(I)
	count = len(I)
	print "Number of Active Buses  :", count	
	print "Locations:\t Lat/Lon"

	for i in xrange(count):
		print "(",I[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],",",I[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"],")"
	'''for "latitude" in theJSON["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]:
		count +=1'''



def main():
	line = str(sys.argv[1])
	key = str(sys.argv[2])
	print "Bus Line","\t\t",":", line
	urlData = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="+ key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ line
	webUrl = urllib2.urlopen(urlData)

	
	if(webUrl.getcode() == 200):
		data = webUrl.read()
		#print data
		printResults(data)

if __name__ == "__main__":
	main()
