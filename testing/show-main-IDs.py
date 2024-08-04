#!/usr/bin/python3



import jk_logging

from jk_licenses import *





with jk_logging.wrapMain() as log:

	for licenseID in LICENSE_MGR.mainLicenseIDs:
		print(licenseID)











