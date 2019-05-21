# Domitilla
Domitilla it's a Global Graph elaboration tool.

The main function that can be executed are: 

- DRAWING: take one graph and give it a graphic representation in PDF.
- PARALLEL COMPOSITION: take two different graphs and give their parallel composition. 
- SYNCHRONIZATION: take two different graphs and allow to fuse a pair of nodes. 
- MULTIPLEXING: take two different graphs and allow to do a more complex fusion.
- TRANSLATION TO PETRI NET: take one graph and give a relative translation in Petri net in _.ndr_ type supported in [TINA](http://projects.laas.fr/tina/download.php).

## Requirement
- Python 3.7
- Graphviz
- KIVY

## CrossPlatform?

Tested on macOs Mojave 10.14.4 and Ubuntu 18.04.2 LTS

## Running Domitilla

Open terminal, find the right directory and execute:
```sh
python3 pagelayout.py
```
and the tool will run.

## Usage example

- CHOOSE FILE: Click on "select" button under the "graph1" and/or "graph2" section and browse till the desired file and then select it, next click on "OK".
For dismissing the selection popup click outside the selection area or click on "OK" without any file selected. 

- DRAW: Select at least one graph.

- PARALLEL COMPOSITION: select two graphs.

- SYNCRONIZATION: Select two graphs. Manually write into the dedicated text area the pair of nodes that you would fuse. Following the given example for the correct syntax.

- MULTIPLEX: Select two graphs. Manually write into the dedicated text area the pair of nodes that you would fuse. Following the given example for the correct syntax.
 
- TRANSLATE TO PETRI NET: Select at least one graph.

- It's possible to change the save path for output saving in "Save Path" section. Click on "find", select the desired folder and then click "OK". 
For dismissing the selection popup click outside the selection area. Unfortunately, at the moment,  if you click "OK" without any file selected the program will crash. 

- Inside "grafi" folder there are some example of graphs:
    * The ones with _(.txt)_ extension are STRUCTURED GLOBAL GRAPH; 
    * The ones with _(.gv)_ extension are UNSTRUCTURED GLOBAL GRAPH;
    * The ones with _(.ndr)_ extension are PETRI NET. They can be opened with an external program called [TINA](http://projects.laas.fr/tina/download.php).

## Example

Select "compose.gv" and "parallel.gv" leave the example node given in the text area and click on syncronization.
The result will be a simple fusion of the decribed node.

## Release History

* 2.0.0
    * CHANGE: restyled graphic interface written using KIVY library
    * CHANGE: cross platform support
    * ADD: new function added: MULTIPLEX 
* 1.0.0
    * ADD: graphic interface written using PySimpleGui library
* 0.1.0
    * more sophisticated command line function
* 0.0.1
    * different command line function

## Author
**Davide Schiavi** - [dedo94](https://github.com/dedo94) – davideschiavi94@gmail.com

Distributed under the MIT license. See [LICENSE](LICENSE) for more information.
