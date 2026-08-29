### Changelog

All notable changes to FEMMInterpreter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*(ISO-DATE is used for all updates)*

---

[0.1.1] - 2026-08-18

### Fixed
- Namespace problem with 0.1.0

---

[0.1.2] - 2026-08-30

### Added
- Namespace is now `ifemm`
- Extra constants to the constant files "numarcsegments" & "beginpoint"
- Updated referencing in `__init__.py` files to `ifemm` instead of `FEMMInterpreter`
- Improved the readme and /docs file. 
- Returns the interpolated B field from vector potential A for graphing.
- Returns the point B field for calculations using finite differences.

### Fixed
- Missing constants extra when loading solutions that used arc segments

--- 