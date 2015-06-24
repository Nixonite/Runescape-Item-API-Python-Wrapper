# Runescape-Item-API-Python-Wrapper
A simple wrapper for the Runescape Item API

Incredibly easy to use!
```
from rsitemwrapper import RunescapeAPI

rs = RunescapeAPI()

data = rs.getItemGraph(4798)
data = rs.getItemPriceInformation(4798)
```

It's good for collecting item price history and a basic description for each item.

Created on June 2015, so hopefully it won't break anytime soon due to API changes.
