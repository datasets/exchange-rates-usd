<a href="https://datahub.io/core/exchange-rates-usd"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

Code for producing consolidated historical exchange rate data from a variety of
sources.

See <http://thedatahub.org/dataset/exchange-rates>

Instructions
============

Get the exchange-rates data package, e.g. using data package manager:

    dpm clone ckan://exchange-rates .

This will get the source data dumps into the data/ directory.

Then do:

    python run.py

Result will be at data/consolidated.csv.

