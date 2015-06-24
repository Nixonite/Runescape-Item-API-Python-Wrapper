from rsitemwrapper import RunescapeAPI

rs = RunescapeAPI()
data = rs.getItemGraph(4798)#a bit too big to print out here
data = rs.getItemPriceInformation(4798)
print data