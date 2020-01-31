# -*- coding: utf-8 -*-
# Makefile
# ----------------------------------------------------------------------------
## Usage:  make [options] [target] ...
## Example:
##
##     make test
##
# ----------------------------------------------------------------------------
install:## Install prerequisities
pip install -r src/requirements.txt


# ----------------------------------------------------------------------------
# Self-Documented Makefile
# ref: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# ----------------------------------------------------------------------------
help:## (DEFAULT) This help information.
@echo ====================================================================
@echo Using $(abspath $(lastword $(MAKEFILE_LIST)))
@echo
@grep -E '^## .*$$'  \
$(MAKEFILE_LIST)  \
| awk 'BEGIN { FS="## " }; {printf "\033[33m%-20s\033[0m \n", $$2}'
@echo
@echo Targets include:
@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$'  \
$(MAKEFILE_LIST)  \
| awk 'BEGIN { FS=":.*?## " }; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'  \
#| sort
.PHONY: help
.DEFAULT_GOAL := help
