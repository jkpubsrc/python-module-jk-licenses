#!/usr/bin/python3



import jk_logging

from jk_licenses import *
from jk_console import *




bWithVariables = False





with jk_logging.wrapMain() as log:

	print("{| class=\"wikitable\"")
	print("|-")

	if bWithVariables:
		for columnName in [ "Main license ID", "Alternative license IDs", "Human readable name", "Variables" ]:
			print("! " + columnName)

		for license in LICENSE_MGR.licenses:
			print("|-")
			print("| <c>" + license.licenseID + "</c>")
			print("| " + ", ".join([ ("<c>" + x + "</c>") for x in license.alternativeLicenseIDs ]))
			print("| " + license.name)
			print("| " + ", ".join([ v.name for v in license.variableDefinitions ]))

	else:
		for columnName in [ "Main license ID", "Alternative license IDs", "Human readable name" ]:
			print("! " + columnName)

		for license in LICENSE_MGR.licenses:
			print("|-")
			print("| <c>" + license.licenseID + "</c>")
			print("| " + ", ".join([ ("<c>" + x + "</c>") for x in license.alternativeLicenseIDs ]))
			print("| " + license.name)

	print("|}")














