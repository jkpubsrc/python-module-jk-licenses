#!/usr/bin/python3



import jk_logging

from jk_licenses import *





with jk_logging.wrapMain() as log:

	#for licenseID in LICENSE_MGR.allLicenseIDs:
	#	print(licenseID)

	for license in LICENSE_MGR.licenses:
		print(license.licenseID)
		for licenseID in license.licenseIDs:
			if licenseID == license.licenseID:
				continue
			print("\t" + licenseID)









