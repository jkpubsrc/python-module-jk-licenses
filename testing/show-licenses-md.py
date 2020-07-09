#!/usr/bin/python3


from jk_licenses import *
from jk_console import *



table = SimpleTable()
table.addRow("Main license ID", "Alternative license IDs", "Human readable name", "Variables")
table.addRow("---", "---", "---", "---")

for license in LICENSE_MGR.licenses:
	table.addRow(
		license.licenseID,
		", ".join(license.alternativeLicenseIDs),
		license.name,
		", ".join([ v.name for v in license.variableDefinitions ])
	)

for line in table.printToLines(gapChar="|"):
	print("|" + line + "|")










