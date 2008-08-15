all: help

help:
	@echo 'Choose one:'
	@echo
	@echo 'filings - create (clobber) the filings.db database.'
	@echo 'test-parse - run parse_*() unit tests.'
	@echo 'test-normalize - run normalize() unit tests.'
	@echo 'test-import - run import_*() unit tests.'
	@echo 'test - run all unit tests.'
	@echo 'help - this message.'

test-parse:
	PYTHONPATH=.:$$PYTHONPATH python tests/test_parse.py

test-normalize:
	PYTHONPATH=.:$$PYTHONPATH python tests/test_normalize.py

test-import:
	PYTHONPATH=.:$$PYTHONPATH python tests/test_import.py

test: test-parse test-normalize test-import

filings:
	sqlite3 filings.db < filings.sql
