unfound = set([1,2,3,4])
followers = set([2,3,5,6])
to_be_connected = unfound & followers
print to_be_connected
unfound = unfound - followers
print unfound
unfound.remove(1)
print unfound