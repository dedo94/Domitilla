# Domitilla
Domitilla it's a Global Graph elaboration tool.

The main function that can be executed are: 

- DRAWING: take one graph and give it a graphic representation in PDF.
- PARALLEL COMPOSITION: take two different graphs and give their parallel composition. 
- SYNCHRONIZATION: take two different graphs and allow to fuse a pair of nodes. 
- MULTIPLEXING: take two different graphs and allow to do a more complex fusion.
- TRANSLATION TO PETRI NET: take one graph and give a relative translation in Petri net in [_.ndr_](http://projects.laas.fr/tina/manuals/formats.html#3) type supported in [TINA](http://projects.laas.fr/tina/download.php).

## Requirement
- [Python](https://www.python.org/downloads/) (3.7)
- [Graphviz](https://www.graphviz.org/download/) (0.10.1)
- [KIVY](https://kivy.org/#download) (1.10.1)

## CrossPlatform?

Tested on macOs Mojave 10.14.4 and Ubuntu 18.04.2 LTS.
Not tested on windows yet.

## Syntax of Structured Global Graphs

The grammar used for Structured Global Graph is based on [chorgram](https://bitbucket.org/emlio_tuosto/chorgram/wiki/Home) grammar.

However, to simplify things, Domitilla's grammar is easier.

```
G ::= (o)                                       * empty graph
        |  Ptp -> Ptp : str                     * interaction
        |  '|{' G '|' G '}'                     * fork
        |  '+{' G '+' ... '+' G '}'             * choice
        |  G ';' G                              * sequential
        |  '*{' G '}' '@' P                     * loop
        |  '{' G '}'

```

## Syntax of Unstructured Global Graphs

The grammar used for Untructured Global Graph is [DOT](https://graphviz.gitlab.io/_pages/doc/info/lang.html) language.

## Running Domitilla

Open terminal, find the right directory and execute:
```sh
python3 dom.py
```
and the tool will run.

## Usage example

- CHOOSE FILE: Click on "select" button under the "graph1" and/or "graph2" section and browse till the desired file and then select it, next click on "OK".
For dismissing the selection popup click outside the selection area or click on "OK" without any file selected. 

- DRAW: Select at least one graph.

- PARALLEL COMPOSITION: select two graphs.

- SYNCRONIZATION: Select two graphs. Manually write into the dedicated text area the pair of nodes that you would fuse. 
There are two type of input accepted.
    * First: a couple of node for each row, for example "A -> H : n ; K -> B : n".
    * [NEW] Second: a couple of partecipant, for example "[A,B]"

- MULTIPLEX: Select two graphs. Manually write into the dedicated text area the pair of nodes that you would fuse. Following the given example for the correct syntax.
 
- TRANSLATE TO PETRI NET: Select at least one graph.

- It's possible to change the save path for output saving in "Save Path" section. Click on "find", select the desired folder and then click "OK". 
For dismissing the selection popup click outside the selection area. Unfortunately, at the moment,  if you click "OK" without any file selected the program will crash. 

- Inside "example/par_ch" folder there are some example of graphs:
    * The ones with _(.txt)_ extension are STRUCTURED GLOBAL GRAPH; 
    * The ones with _(.gv)_ extension are UNSTRUCTURED GLOBAL GRAPH;
    * The ones with _(.ndr)_ extension are PETRI NET.

## Example

SYNCHRONIZATION: Select "compose.gv" and "parallel.gv" leave the example node given in the text area and click on syncronization. The result will be a simple fusion of the decribed node.

## Known Issue/Bugs or Missing Function 

- SYNCHRONIZATION has undergone some changes, and isn't well tested. 
- MULTIPLEX button it has no function yet.
- structured Global Graph TRANSLATION to Petri net doesen't work.

## Release History

* 2.0.3
    * ADD: popup messages, warnings and errors.
    * CHANGE: improved SYNCHRONIZATION, now recognize two different tipe of input and execute different operation. Check usage example for more detail.
* 2.0.2
    * ADD: Clear All button.
    * CHANGE: modified graph folder, now has a better organization (renamed "grafi" in "example").
    * CHANGE: modified label naming in Petri net translation.
    * CHANGE: now able to execute syncronization using onli one graph.
    * CHANGE: fixed problem saving directory.
    * CHANGE: fixed various problem (parser, fusion, added some more comment in-line code, ecc.).
* 2.0.1
    * CHANGE: better path handling function.
    * CHANGE: graphic bug in UI solved.
* 2.0.0
    * ADD: help button.
    * CHANGE: restyled graphic interface written using KIVY library.
    * CHANGE: cross platform support.
* 1.0.0
    * ADD: graphic interface written using PySimpleGui library.
* 0.1.1
    * ADD: more sophisticated command line function.
* 0.1.0
    * ADD: different command line function.
    
## File List

* composition.py: contain two functions. 
    * composition(gr1, gr2, name, draw): merge two graph in one.
        * gr1: first graph;
        * gr2: second graph;
        * name: name of the composition;
        * draw: 1 give as output also the PDF whit the result, 0 otherwise.
    * refusion(gr_st, nome, node_fus, draw): provide the syncronization of the node inside of one graph.
        * gr_str: new empty list;
        * nome: name of the fusion;
        * node_fus: list of the node waiting for syncronization;
        * draw: 1 give as output also the PDF whit the result, 0 otherwise.

* convert.py: contain one fuction.
    *  petri2(path, nome_grafo, gr_str, save): provide the translation of an Unstructured Global Graph in Perti net.
       * paht: path of the original file (at the moment unsed, this parameter will be removed soon);
       * nome_grafo: name of the graph;
       * gr_str: new empty list;
       * save: path of the save folder.

* dom.py: contain a lot of function required for the GUI.

* domitilla.kv: it's a style file required by kivy for the GUI.

* dottogr.py: contain one function.
    * dot_not_struct(path, nome_grafo, struct, draw): fill an empty list with data belonging to an Unstructured Global Graph.
        * path: path of the graph;
        * nome_grafo: name of the graph;
        * struct: new empty list;
        * draw: 1 give as output also the PDF whit the result, 0 otherwise.
        
* draw.py: contain one function:
    * draw_graph(struct, name): provide a PDF with a drowing of the graph.
         * struct: full list of the graph;
         * nome_grafo: name of the graph;
         
* function.py: contain a lot of side function.

* myfunc.py: contain a lot of side function.

* strtogr.py: contain one function:
    * struct_gr(path, nome_grafo, struct, draw): fill an empty list with data belonging to a Structured Global Graph.
        * path: path of the graph;
        * nome_grafo: name of the graph;
        * struct: new empty list;
        * draw: 1 give as output also the PDF whit the result, 0 otherwise.
        
* fuseplus.py: contain one function:
    * fuseplus(cmp, n1, n2): transform two partecipant in a list that contain every possible couple of fusion.
       * cmp: struct that contain one graph;
       * n1: first partecipant,
       * n2; second partecipant.
        
* path.txt: text file that memorize some usefull path.
    

## Author
**Davide Schiavi** - [dedo94](https://github.com/dedo94) – davideschiavi94@gmail.com

Distributed under the MIT license. See [LICENSE](LICENSE) for more information.
