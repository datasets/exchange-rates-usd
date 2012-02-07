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

