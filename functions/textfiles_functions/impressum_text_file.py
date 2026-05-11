"""
This function defines the impressum text for the dash application
"""

from dash import html


impressum_titel_text = "Oral History Topic Modeling Dash Board"
impressum_text = (
    """
        Das OHTM-Dashboard bietet eine interaktive Exploration ausgewählter Interviewsammlungen des Archivs Deutsches Gedächtnis der FernUniversität in Hagen.\n
        Die Sammlungen werden in Form von Abkürzungen dargestellt und können separat angesteuert werden. Eine Liste der Abkürzungen finden Sie im Glossar.\n
        Die Interviews wurden mithilfe von Topic-Modeling-Verfahren analysiert, um thematische Strukturen und Muster in den Erzählungen zu identifizieren.\n

        Da es sich um einen Testballon handelt, sind noch nicht alle Funktionen final ausgearbeitet, und bislang ist nur ein Teil des Archivs eingebunden.\n\n

        Die einzelnen Interviews wurden anonymisiert.\n
        Sollten Sie bereits im Archiv Oral-History.Digital angemeldet und für die jeweiligen Sammlungen freigeschaltet sein, können Sie über die Links in den einzelnen Textpassagen direkt zum Originalinterview springen.\n\n

        In der Menüleiste können Sie Tooltips aktivieren, die Ihnen bei der Bedienung des Dashboards helfen sollen.
        Zusätzlich können Sie sich Labels für die Topics anzeigen lassen oder die Topics zu thematischen Clustern gruppieren.
        Über den ICA-Schalter können Sie eine spezielle Interview-Heatmap aktivieren, die von Dennis Möbus entwickelt wurde.
    """,
    html.A(
        "Oral History Digital Projekt",
        href="https://www.oral-history.digital/",
        target="_blank",
    ),
    "\n",
    html.A(
        "Oral History Digital Archiv",
        href="https://portal.oral-history.digital/de",
        target="_blank",
    ),
)
