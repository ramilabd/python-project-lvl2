# Gendiff

[![Actions Status](https://github.com/ramilabd/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ramilabd/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/721080dd6da4bae85e5d/maintainability)](https://codeclimate.com/github/ramilabd/python-project-lvl2/maintainability)
[![Build Status](https://travis-ci.com/ramilabd/python-project-lvl2.svg?branch=main)](https://travis-ci.com/ramilabd/python-project-lvl2)
[![Python CI](https://github.com/ramilabd/python-project-lvl2/actions/workflows/python-ci.yml/badge.svg?branch=main)](https://github.com/ramilabd/python-project-lvl2/actions/workflows/python-ci.yml)
[![time tracker](https://wakatime.com/badge/github/ramilabd/python-project-lvl2.svg)](https://wakatime.com/badge/github/ramilabd/python-project-lvl2)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## Description

Difference calculator – a program that determines the difference between two
data structures. This is the second training project from the Python-developer
profession on [Hexlet.io](https://ru.hexlet.io/programs/python/projects/50).

Utility features:

* Support for different input formats: yaml, json
* Generating a report in plain text, stylish, and json format

Usage example:

```
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```