"""
This function defines the impressum text for the dash application
"""

from dash import html


impressum_titel_text = "Oral History Topic Modeling Dashboard (OHTM)"
impressum_text = (
    """
Das OHTM-Dashboard unterstützt eine interaktive Exploration ausgewählter Interviewsammlungen des Archivs „Deutsches Gedächtnis“ der FernUniversität in Hagen. Mit dem statistikbasierten Topic-Modeling-Verfahren können thematische Strukturen und Muster in den Erzählungen identifiziert werden. Derzeit sind hier 681 Interviews aus 24 Sammlungen analysierbar. Die Sammlungen (Abkürzungen unten) können auch einzeln ausgewählt werden.

Die Interviews sind im OHTM-Dashboard anonymisiert. Wenn Sie für das Archiv „Deutsches Gedächtnis“ freigeschaltet sind, können Sie über die Links in den einzelnen Textpassagen direkt zum Originalinterview springen.

In der Menüleiste können Sie Tooltips aktivieren, die Ihnen bei der Bedienung des Dashboards helfen.

Zusätzlich können Sie sich die manuell vergebenen Labels für die Topics anzeigen lassen oder die Topics zu thematischen Clustern gruppieren. Über den ICA-Schalter können Sie eine spezielle Interview-Heatmap aktivieren, die von Dennis Möbus entwickelt wurde. 

Das OHTM-Dashboard und die zugrundeliegende Topic Modeling-Pipeline wurden im DFG-geförderten Projekt „Oral-History.Digital“ von Philipp Bayerschmidt und Dennis Möbus entwickelt. Darauf basieren auch automatische Inhaltsverzeichnisse und Register für 681 Interviews im Archiv „Deutsches Gedächtnis“.
Weitere Informationen finden sich unter https://www.oral-history.digital/dokumente/index.html#tm.


Abkürzungen der Sammlungsnamen:
BDD = Bombardierung Dresdens
BJ = Berliner Jugend
BUS = Bildung und Sucht
DEK = Deutschsprachige Einwanderinnen und Einwanderer nach Kanada
DFB = Deutsche Frauen und Besatzungssoldaten
DKP = Der klassische Punk
DVE = Die Volkseigene Erfahrung
EEE=Einsetzung und Einpassung neuer Eliten im Ruhrgebiet nach 1945
F24 = Frauenstraße 24 - Hausbesetzung in Münster
GFU = Geschichte der FernUniversität
GMB = Generation Mauerbau
HUI = Holocaust- Überlebende in Israel
KDU = Kinder des Umbruchs
LUSIR = Leben und Sterben im Ruhrgebiet
NAC = Neuapostolische und apostolische Christen im Umgang mit der „Botschaft“ - Geschichte eines Schismas
NNRW = Naturschutz in NRW
PDG = Pioniere des Gedenkens
SLB = Speziallager Buchenwald
SLJ = Speziallager Jamlitz/Lieberose
TB = Technobiographien
VHSS = Verarbeitung der Haft in sowjetischen Speziallagern
VJ = Verschwiegene Jahre
WH = Wehrmachtshelferinnen
ZGD = Zwangsaussiedlungen aus dem Grenzgebiet der DDR

    """,
    html.A(
        "Archiv „Deutsches Gedächtnis",
        href="https://deutsches-gedaechtnis.fernuni-hagen.de/de",
        target="_blank",
    ),
    "\n",
    html.A(
        "Interviewportal „Oral-History.Digital“",
        href="https://portal.oral-history.digital/de",
        target="_blank",
    ),
    "\n",
    html.A(
        "Projekt „Oral-History.Digital“",
        href="https://www.oral-history.digital",
        target="_blank",
    ),
    "\n",
    html.A(
        "Impressum",
        href="https://deutsches-gedaechtnis.fernuni-hagen.de/de/legal_info",
        target="_blank",
    ),
)
