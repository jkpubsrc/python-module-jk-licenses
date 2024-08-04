#!/usr/bin/python3



import jk_logging

from jk_licenses import *





with jk_logging.wrapMain() as log:


	license = LICENSE_MGR.getLicense("MIT")
	licenseText = license.produceText({
		"year": 2020,
		"copyrightHolder": "Jürgen Knauth"
	})

	print("=" * 120)
	print()
	print(licenseText)
	print()
	print("=" * 120)








