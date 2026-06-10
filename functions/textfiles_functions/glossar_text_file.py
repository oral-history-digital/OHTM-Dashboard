"""
This function defines the impressum text for the dash application
"""



glossar_titel_text = "OHTM Dashboard Glossar"
glossar_text = """

Topic Modeling: 
Topic Modeling ist ein probabilistisches Verfahren aus dem Bereich des Text Mining, einem Unterbereich des Natural Language Processing, bei dem das gemeinsame Aufkommen von Wörtern innerhalb eines Textkorpus auf Grundlage von statistischen Verteilungen berechnet und zu verschiedenen Gruppen, sogenannten Topics, zugeordnet wird. Es gibt verschiedene Algorithmen zur Berechnung der Topics, hier wurde das „Latent-Dirichlet-Allocation-Verfahren“ (LDA) verwendet. 
LDA geht von der Grundannahme aus, dass jedes Dokument eine Zusammensetzung verschiedener Themen ist. Das Verfahren berechnet die statistische Verteilung und Nähe der Wörtern zueinander und teilt diese einzelnen Topics zu, die Anzahl der Topics ist dabei frei wählbar.

Topic:
Ein Topic ist eine Gruppe von Wörtern, die innerhalb von Dokumenten häufig zusammen auftreten. 

Corpus
Das Corpus besteht aus allen für diese Berechnungen verwendeten Daten und setzt sich aus verschiedenen Interviewtranskripten aus verschiedenen thematischen Sammlungen zusammen. 

Sammlung:
Eine Sammlung ergibt sich aus einem Forschungsprojekt, in dessen Rahmen mehrere lebensgeschichtliche Interviews geführt worden sind.

Chunk:
Da die Interviewtranskripte für die Berechnung und Rückführung der Ergebnisse zu lang sind, wurden sie vorher in kleinere Abschnitte, sogenannte Chunks, unterteilt. Ein Chunk besteht aus 500 Wörtern. 

Topic-Wort-Verteilung:
Die Liste von Wörtern, die Teil eines Topics sind, absteigend nach der Wahrscheinlichkeit. Theoretisch wird für jedes Wort die Wahrscheinlichkeit berechnet, Teil des Topics zu sein, der hier verwendete Algorithmus gibt jedoch nur die ersten 1000 Wörter pro Topic aus. Es ist wichtig anzumerken, dass die Wortlisten der Topics allein auf der statistischen Verteilung der Wörter innerhalb des Forschungskorpus gebildet werden und keine externen Informationen für die Berechnung verwendet werden. Die Wortlisten besitzen dennoch semantische Gemeinsamkeiten, die aus dem gemeinsamen Auftreten innerhalb von Sätzen oder Textabschnitten resultieren.

Topic-Dokument-Verteilung:
Die Topic-Dokument-Verteilung enthält die Wahrscheinlichkeiten, die jedes Topic innerhalb eines Chunks besitzt.


Hier finden Sie in kürze eine Auswahl an weiterführenden Aufsätzen:

    """
