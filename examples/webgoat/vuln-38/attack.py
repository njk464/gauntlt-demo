usernames = ("bob", "ted", "dylan", "rob", "jeff", "admin")
a_user = "admin"
colors = ("yellow", "red", "blue", "black", "purple", "green")
a_color = "green"
got_it = False
for u in usernames:
	# make the request here for the username
	if u is a_user: # test if request is good here
		for c in colors:
			# make the request here for the color
			if c is a_color: # test if request is good here
				got_it = True
				print (u+":", c)
if not got_it:
	print "none found"
