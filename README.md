jk_licenses
==========

Introduction
------------

This python module provides OS licenses.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-licenses)
* [pypi.python.org](https://pypi.python.org/pypi/jk_licenses)

Why this module?
----------------

It is quite tiresome to maintain various instances of a program using all the same data. Therefore the functionality of providing a set of licenses has been factored out into this module `jk_licenses`.

This module is intended as a building block in module/package/application management.

What licenses are supported?
----------------------------

The following table provides an overview about the licenses available in this module as well as their identifiers and variables:

| Main license ID | Alternative license IDs | Human readable name                         | Placeholders          |
| ---             | ---                     | ---                                         | ---                   |
| 0BSD            |                         | Free Public License 1.0.0                   |                       |
| AGPLv3          | AGPL-3.0, AGPLv3        | GNU Affero General Public License version 3 |                       |
| Apache2         | Apache2                 | GNU Lesser General Public License version 3 |                       |
| BSD2            | BSD2                    | The 2-Clause BSD License                    | year, copyrightHolder |
| BSD3            | BSD3                    | The 3-Clause BSD License                    | year, copyrightHolder |
| GPLv3           | GPL-3.0, GPLv3          | GNU General Public License version 3        |                       |
| LGPLv3          | LGPL-3.0, LGPLv3        | GNU Lesser General Public License version 3 |                       |
| MIT             |                         | MIT License                                 | year, copyrightHolder |
| Proprietary     | proprietary             | Propriertary License                        | year, copyrightHolder |

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_licenses
```

### What this module provides

The python module `jk_licenses` provides a constant (= global variable) and three classes:

* constant `LICENSE_MGR` that provides an instance of `LicenseMgr`
* class `LicenseMgr` that maintaines the available licenses
* class `License` that represents a single license
* class `VariableDef`: licenses may contain `VariableDef` to represent placeholders within the license text

### The class `License`

Each license is represented by an instance of class `License`.

This section gives a short explanation about the structure of an instance of `License` in pseudocode notation.

This class provides the following properties:

* `str name` : The human readable name of this license.
* `str[] licenseIDs` : A list of strings that are associated with this license as identifiers. The first license ID is always the main license ID.
* `str licenseID` : The main license ID that identifies this license.
* `str classifier` : A string that contains a possible python trove classifier. See [pypi.org](https://pypi.org/classifiers/) for details.
* `VariableDef[] variableDefinitions` : A list of variable definitions. These give information about placeholders to fill if you want to produce the license text.

This class provides the following methods:

* `str produceText(dict<str,str> variableAssignments)` : Produce the license text. If a license has placeholder, you need to provide a value for every placeholder. An exception is thrown on error.
* `void validateVariableAssignments(dict<str,str> variableAssignments)` : You can check if data is provided for all placeholders as required using this method. An exception is thrown on error.

You do not need to instantiate this class yourself. Instead you obtain an instance of this class through the license manager.

### The class `LicenseMgr`

The license manager is represented by an instance of class `LicenseMgr`.

This section gives a short explanation about the structure of the license manager in pseudocode notation.

This class provides the following properties:

* `str name` : The human readable name of this license.
* `str[] licenseIDs` : A list of strings that are associated with this license as identifiers. The first license ID is always the main license ID.
* `str licenseID` : The main license ID that identifies this license.
* `str classifier` : A string that contains a possible python trove classifier. See [pypi.org](https://pypi.org/classifiers/) for details.
* `VariableDef[] variableDefinitions` : A list of variable definitions. These give information about placeholders to fill if you want to produce the license text.

This class provides the following methods:

* `str produceText(dict<str,str> variableAssignments)` : Produce the license text. If a license has placeholder, you need to provide a value for every placeholder. An exception is thrown on error.
* `void validateVariableAssignments(dict<str,str> variableAssignments)` : You can check if data is provided for all placeholders as required using this method. An exception is thrown on error.

You do not need to instantiate this class yourself. Instead you access a default license manger instance using the constant (= variable) `LICENSE_MGR` this module provides.

### Access the licenses

You can display the licenses that are available via the license manager. Example:

```python
for licenseID in LICENSE_MGR.mainLicenseIDs:
	print(licenseID)
```

If you specify the licenses available you can use the license identifiers to access a license object. Example:

```python
license = LICENSE_MGR.getLicense("0BSD")
print(license.name)
```

### Producing a license text

Once you have a license object obtained from the license manager you can then produce the license text. Example:

```python
license = LICENSE_MGR.getLicense("0BSD")
licenseText = license.produceText()
```

And with arguments:

```python
license = LICENSE_MGR.getLicense("MIT")
licenseText = license.produceText({
	"year": 2020,
	"copyrightHolder": "Jürgen Knauth"
})
```

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



