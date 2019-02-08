# Tirocinio GUI

LIBRERIE NECESSARIE:
  - Graphviz
  - PySimpleGUI
  
UTILIZZO: 
  Per avviare il programma recarsi nella cartella e utilizzare il comando "python3 guy.py".
  Cosa fanno i bottoni?
  COMPOSE: selezionare due grafi tramite i bottone Browse appartenenti rispettivamente a FIRST GRAPH e SECOND GRAPH,
  (e cambiare il nome di salvataggio). Compose meterà in parallelo i due grafi in input e ne restituisce il file .dot
  e il disegno in .pdf
  FUSE:selezionare un grafo tramite i bottone Browse, inserire nodi appartenenti ad esso e che vogliamo fondere.
  Eseguire questa operazione sia per FIRST GRAPH che SECOND GRAPH. (Cambiare il nome di salvataggio).
  Fuse realizzerà una composizione dei grafi e in aggiunta fonderà i nodi che rispettano i requisiti e ne restituisce 
  il file .dot e il disegno in .pdf
  DRAW: inserire in almeno uno dei due slot di ricerca di file un grafo, indicare se si tratta di un grafo stutturato 
  o non strutturato. Draw restituirà il disegno in .pdf (se vengono inseriti due grafi verranno disegnati entrambi).
  E' possibile, inoltre, modificare il path di salvataggio dei file.
  
  All'interno della cartella grafi sono presenti alcuni esempi di grafo. Quelli strutturati sono in formato .txt;
  quelli non strutturati no in formato .dot

NOTE:
  - Non è possibile fare una fusione utilizzando un grafo strutturato; tuttavia è possibile renderlo non strutturato e quindi
    succesivamente eseguirne la fusione.