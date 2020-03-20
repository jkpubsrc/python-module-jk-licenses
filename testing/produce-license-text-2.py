#!/usr/bin/python3


from jk_licenses import *



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








