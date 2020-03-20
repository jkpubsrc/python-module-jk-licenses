#!/usr/bin/python3


from jk_licenses import *



license = LICENSE_MGR.getLicense("0BSD")
licenseText = license.produceText()

print("=" * 120)
print()
print(licenseText)
print()
print("=" * 120)








