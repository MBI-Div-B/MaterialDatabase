# MBI Material Database Concept

Due to the general demand for collecting, storing, and exchanging material parameters, we provide a text-file-based solution, as well as several Python scripts and GUIs to read, change, and store material parameters.

Initially, we will only support the [YAML](https://en.wikipedia.org/wiki/YAML) format as a data source, but the general design will allow also for other data sources, such as SQL databases or other file formats, e.g. XML or JSON.

## YAML Format

An very simple example of a YAML file is given below:

```yaml
meta:
  name: iron
  formula: Fe
  description: pure crystallien iron in beta phase
  comment: maybe there is something to say here
  last_updated: 2020-04-28
  references:
    @article{curtiss2013unicorn,
    author = "Curtiss, Michael and Becker, Iain and Bosman, Tudor and Doroshenko, Sergey and Grijincu, Lucian and Jackson, Tom and Kunnatur, Sandhya and Lassen, Soren and Pronin, Philip and Sankar, Sriram and others",
    title = "Unicorn: A system for searching the social graph",
    journal = "Proceedings of the VLDB Endowment",
    volume = "6",
    number = "11",
    pages = "1150--1161",
    year = "2013",
    publisher = "VLDB Endowment",
    doi = "10.14778/2536222.2536239"
    }
data:
  thermal_conductivity:
    curtiss2013unicorn:
      value: 80
      uncertainty: 1
      unit: J/m
      comment: some value comment here
  refractive_index:
    curtiss2013unicorn:
      value:
        wavelength:
          values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
          arg_values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
          arg_unit: nm
          comment: maybe one can write a fit of the data here
      unit: ''
      comment: n = n' + i k
```

First, there is `meta` section which holds meta-data of the material.
Most importantly, there must be references defined, in order to link paramters to them.
The `references` entry must be in plain `bibtex` format, which can hold any type of reference and as many as necessary.

In the `data` section the actual physical parameters are declared.
It is possible to have multiple values stored for a single parameter, by indexing each by a `citation_key`, which must be defined above in the `meta` section.
The actual parmaters, must have `value` and `unit` and can optionally have `uncertainty` and `comment`.

In case of a functional dependence of a parameter, the name of the `argument` must be given as new index. The actual parameter `values`, the `arg_values` and `arg_unit` are mandatory.
The `comment` is optional.
With this format even multiple functional dependencies are possible from one and the same or multiple references.

## Python Scripts

The YAML file format allows for human readability and does not require any programmatic access.
However, we provide several Python (other languages such as MATLAB can be implemented in the future as well) modules in order to inteact with the material database:

The `Parser` module is dedicated for reading and writing data from and to e.g. a YAML file.
New data must be provided as a `dict` in Python with a well-defined structure.

The `Material` module implements a class for `Material`, `Paramter`, and `References` and should allow for easy interaction in a Python script with the material database.

The `GUI` module even builds a graphical interface to read, change, and create data files.

An example of programmatic access to the database could look like this:

```python
import material_database as md

parser = md.parser.PyYamlParser(r'C:\Users\borchert\Documents\repos\MaterialDatabase\Data')

iron = md.Material(parser.load('fe'), log_level=10)

print(iron.thermal_conductivity['curtisss2013unicorn'].value)
..80

```