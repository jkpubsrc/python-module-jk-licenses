#!/usr/bin/python3


from jk_licenses import *
from jk_console import *



table = SimpleTable()
table.addRow("Main license ID", "Alternative license IDs", "Human readable name", "Placeholders").hlineAfterRow = True

for license in LICENSE_MGR.licenses:
	table.addRow(
		license.licenseID,
		", ".join(license.licenseIDs[1:]),
		license.name,
		", ".join([ v.name for v in license.variableDefinitions ])
	)

table.print()










