# DOMITILLA

Domitlla è un tool per l'elaborazione di Unstructured Global Graph

### Prerequisiti

Per poter utilizzare Domitilla è necessario installare i seguenti pacchetti:

Python:

```
sudo add-apt-repository ppa:jonathonf/python-3.6

sudo apt-get update

sudo apt-get install python3.6
```

Graphviz:

```
sudo apt-get install graphviz
```

PySimpleGUI:

```
sudo pip install PySimpleGUI
```

## Utilizzo

Per poter avviare il programma recarsi nella cartella da terminale e utilizzare il comando:
```
python3 gui.py
```

Quali operazioni svolgono i bottoni?

 - COMPOSE: selezionare due grafi tramite i bottone Browse appartenenti rispettivamente a FIRST GRAPH e SECOND GRAPH,
 (cambiare il nome di salvataggio). Compose mette in parallelo i due grafi in input e ne restituisce il file DOT
 e il disegno in PDF relativi alla composizione.

 - FUSE: selezionare un grafo tramite i bottone Browse e inserire le coppie di nodi che vogliamo fondere separate da ";".
 Selezionare due grafi in FIRST GRAPH e SECOND GRAPH nel caso in cui si voglia eseguire l'operazione su
 due grafi separati (COMPOSE + FUSE). (Cambiare il nome di salvataggio).
 Fuse realizzerà una composizione dei grafi e in aggiunta fonderà i nodi che rispettano i requisiti e ne restituisce
 il file DOT e il disegno in PDF relativo.

 - DRAW: inserire in almeno uno dei due campi di ricerca di file un grafo, indicare se si tratta di un grafo stutturato
 o non strutturato. Draw restituirà il disegno in .pdf (se vengono inseriti due grafi verranno disegnati entrambi).

 - PETRINET: l'utilizzo è il medesimo di DRAW. Dato in input un Unstructured Global Graph (.gv) restituisce la traduzione
 in rete di Petri (.ndr)

 - E' possibile, inoltre, modificare il path di salvataggio dei file (in alto).

 All'interno della cartella grafi sono presenti alcuni esempi di grafo. Quelli strutturati sono in formato .txt mentre
 quelli non strutturati sono in formato DOT (.gv).

 N.B.: sfortunatamente ogni volta che viene portata a termine un'operazione Domitilla termina. Per poter continuare a
 lavorare con il tool è necessario riavviarlo tramite il comando "python3 gui.py" da terminale.

 NOTE:

  - Non è possibile fare una fusione utilizzando un grafo strutturato; tuttavia è possibile renderlo non strutturato e quindi
    succesivamente eseguirne la fusione.

## Librerie usate

* [Graphviz](https://www.graphviz.org/) - Per generare i grafi
* [PySimpleGUI](https://pysimplegui.readthedocs.io/) - Per generare l'interfaccia grafica

## Autore

* **Davide Schiavi** - [dedo94](https://github.com/dedo94)

## Licenza

Questo software è rilasciato sotto la MIT License - vedere [LICENSE.md](LICENSE.md) per i dettagli
