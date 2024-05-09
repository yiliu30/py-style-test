# ruff check import
ruffimport:
	ruff check --select ICN
	
rufffiximport:
	ruff check --select ICN --unsafe-fixes --fix