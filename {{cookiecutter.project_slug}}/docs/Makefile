SHELL := /bin/bash

.PHONY: help clean html

help:
\techo "Possible targets: clean, html"

clean:
\trm -rf _build

html:
\tsphinx-build -b html . _build/html
