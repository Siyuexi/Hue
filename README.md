# HybridLogParser
tring to parse all types of log including table text, multi-line message and normal logs.

## demo.log
demo.log is a raw log data demo.

## meta.log
meta.log is a meta file of the origin log. 

Its  format is:

```csv
TEMPLATE_SYMBOL,BEGINING_LINE,TEMPLATE
```

## test.py

a test case. You can simply run 

``` shell
python test.py
```

to start parsing.

## config.yml

a yaml file for preprocessing and hyperparameters

## Parser.py

Implements class Parser and also defines some data structures.