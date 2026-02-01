"""
This function defines the impressum text for the dash application
"""

from dash import html


impressum_titel_text = "Oral History Topic Modeling Dash Board"
impressum_text = (
    """
    Dieses Dashboard bietet eine interaktive Exploration einiger ausgewählter Interviewsammlungen von Oral-History.Digital.\n
    Die Interviews wurden mithilfe von Topic Modeling Verfahren analysiert, um thematische Strukturen und Muster in den Erzählungen zu identifizieren.\n
    Da es sich um einen Testbalon handelt, sind noch nicht alle Funktionen final ausgearbeitet und nur ein Teil des Archives eingebunden.\n
    Die einzelnen Interviews wurden anonymisiert.     
    Sollten sie bereits im Archiv Oral-History.Digital angemeldet und für dei jeweiligen Sammlungen freigeschaltet sein, können sie über die Links der einzelnen Textpassagen direkt zum Originalinterview springen"\n
    Bei Fragen, Anregungen oder Feedback wenden Sie sich gerne an Philipp Bayerschmidt (philipp.bayerschmidt@fernuni-hagen.de)\n

    In der Menüleiste können Sie entweder Tooltips aktivieren, die Ihnen bei der Bedienung des Dashboards helfen sollen.
    Zusätzlich können Sie sich Labels für die Topics anzeigen lasen, oder die Topics zu thematischen Clustern gruppieren.
    Über den IHC Schalter können sie eine spezielle Interview Heatmap aktivieren, die von Dennis Möbus entwickelt wurde.
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
