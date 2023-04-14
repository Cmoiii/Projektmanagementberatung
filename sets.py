import classes

def init():
    global startSet
    startSet = ["Personen", "Teams"]
    global deadlineSet 
    deadlineSet = ["Fest", "Leicht flexibel", "Flexibel"]
    global anforderungsSet
    anforderungsSet = ["Fest", "Einzelne Änderungen", "Leichte Änderungen", "Mehrere Änderungen", "Sehr flexibel"]
    global clientSet
    clientSet = ["Nur auf Absprache", "Selten", "Häufig"]
    global dependencySet
    dependencySet = ["Minimal", "Mäßig", "Stark"]


    global methods
    methods = []
    waterfall = classes.ProjectMethod("waterfall", "Wasserfall-Modell",
                                      classes.MethodAttribute("teams",0,1,1,20,20), 
                                      classes.MethodAttribute("teamsize",0,1,1,20,20), 
                                      classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Selten","Häufig"),
                                      classes.MethodAttribute("dependency",dependencySet,"Minimal","Mäßig","Stark","Stark"),
                                      classes.MethodAttribute("deadline",deadlineSet,"Fest","Fest","Leicht flexibel","Flexibel"),
                                      classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Fest","Fest","Einzelne Änderungen")
                                      )
    methods.append(waterfall)
    v = classes.ProjectMethod("v", "V-Modell",
                              classes.MethodAttribute("teams",0,1,1,20,20),
                              classes.MethodAttribute("teamsize",0,1,1,20,20),
                              classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Nur auf Absprache","Häufig"),
                              classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Mäßig","Stark"),
                              classes.MethodAttribute("deadline",deadlineSet,"Fest","Fest","Leicht flexibel","Flexibel"),
                              classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Fest","Einzelne Änderungen","Leichte Änderungen")
                              )
    methods.append(v)
    spiral = classes.ProjectMethod("spiral", "Spiralmodell",
                                   classes.MethodAttribute("teams",0,1,1,20,20), 
                                   classes.MethodAttribute("teamsize",0,1,1,20,20),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Häufig","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Mäßig","Stark","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Fest","Fest","Leicht flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Fest","Leichte Änderungen","Mehrere Änderungen")
                                   )
    methods.append(spiral)
    scrum = classes.ProjectMethod("scrum", "Scrum",
                                   classes.MethodAttribute("teams",0,1,1,1,2),
                                   classes.MethodAttribute("teamsize",0,3,3,10,12),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Häufig","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Stark","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Leicht flexibel","Flexibel","Flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Einzelne Änderungen","Mehrere Änderungen","Sehr flexibel")
                                   )
    methods.append(scrum)
    kanban = classes.ProjectMethod("kanban", "Kanban",
                                   classes.MethodAttribute("teams",0,1,1,4,5),
                                   classes.MethodAttribute("teamsize",0,1,1,20,20),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Häufig","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Stark","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Leicht flexibel","Flexibel","Flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Einzelne Änderungen","Sehr flexibel","Sehr flexibel")
                                   )
    methods.append(kanban)
    safeEssential = classes.ProjectMethod("safeEssential", "SAFe (Scaled Agile Framework) Essential",
                                   classes.MethodAttribute("teams",0,4,5,15,16),
                                   classes.MethodAttribute("teamsize",0,3,3,10,12),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Selten","Häufig","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Mäßig","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Leicht flexibel","Leicht flexibel","Flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Einzelne Änderungen","Sehr flexibel","Sehr flexibel") #verify
                                   )
    methods.append(safeEssential)
    safeLarge = classes.ProjectMethod("safeLarge", "SAFe (Scaled Agile Framework) Large Solution",
                                   classes.MethodAttribute("teams",0,15,16,20,20),
                                   classes.MethodAttribute("teamsize",0,3,3,10,12),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Selten","Häufig","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Mäßig","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Leicht flexibel","Leicht flexibel","Flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Einzelne Änderungen","Sehr flexibel","Sehr flexibel") #verify
                                   )
    methods.append(safeLarge)
    nexus = classes.ProjectMethod("nexus", "Nexus",
                                   classes.MethodAttribute("teams",0,2,3,9,11),
                                   classes.MethodAttribute("teamsize",0,3,3,10,12),
                                   classes.MethodAttribute("client",clientSet,"Nur auf Absprache","Nur auf Absprache","Selten","Häufig"),
                                   classes.MethodAttribute("dependency",dependencySet,"Minimal","Minimal","Stark","Stark"),
                                   classes.MethodAttribute("deadline",deadlineSet,"Leicht flexibel","Leicht flexibel","Flexibel","Flexibel"),
                                   classes.MethodAttribute("anforderung",anforderungsSet,"Fest","Einzelne Änderungen","Mehrere Änderungen","Sehr flexibel")
                                   )
    methods.append(nexus)

    global descriptionDict
    descriptionDict = {
        "waterfall": "Das Wasserfallmodell ist eine der klassischen Methoden des Projektmanagements. Es handelt sich um ein lineares Planungsmodell, das in aufeinanderfolgende Projektphasen unterteilt ist. Das neue Projekt beginnt mit der ersten Phase und läuft in einer strikten Reihenfolge ab. Sobald eine Phase abgeschlossen ist, beginnt automatisch die nächste.",
        "v" : "Das V-Modell definiert zusätzlich zu den Entwicklungsphasen auch die Vorgehensweise für die Qualitätssicherung (Testen), indem Testphasen den einzelnen Entwicklungsphasen gegenübergestellt werden. Auf der linken Seite wird mit einer funktionalen/fachlichen Spezifikation begonnen, die immer detaillierter zu einer technischen Spezifikation und Implementierungsgrundlage ausgebaut wird. Die Implementierung erfolgt in der Spitze, die anschließend auf der rechten Seite gegen die entsprechenden Spezifikationen der linken Seite getestet wird.",
        "spiral" : "Das Spiralmodell ist ein zyklischer Prozess mit vielen Schleifen. Die Anzahl der Schleifen variiert je nach Projekt und wird vom Projektleiter festgelegt. Jede Phase des Softwareentwicklungsprozesses ist eine Schleife der Spirale.\n\nDas Spiralmodell ermöglicht es, schrittweise ein Produkt in jeder Phase der Spirale zu verfeinern und zu verbessern. Außerdem können Prototypen in jeder Phase erstellt werden. Das Modell bietet die Möglichkeit, unbekannte Risiken nach Beginn des Projekts zu bewältigen. Durch die Erstellung eines Prototyps wird dies ermöglicht.",
        "scrum" : "Das Scrum-Team agiert in autonomer Arbeitsweise. Es besteht aus drei Rollen, die zusammenarbeiten. Es entscheidet darüber, was in welcher Reihenfolge von wem und wie umgesetzt wird. Der Scrum-Master ist hierbei für den Prozess verantwortlich. Sein Ziel ist es, eine hohe Effektivität des Scrum Teams zu erreichen. Die Aufgabe des Produktverantwortlichen (Product-Owner) besteht darin, sicherzustellen, dass immer am wertvollsten gearbeitet wird. Die Entwickler treffen die technischen Entscheidungen und gewährleisten eine angemessene Qualität und Wartbarkeit des Produkts.\nDie Entwickler arbeiten in Entwicklungszyklen von einer bis vier Wochen (Sprints) an einem Sprint-Ziel. In regelmäßigen Abständen kontrolliert das Team seine Arbeit und passt seine Vorgehensweise und sein Produkt Backlog an. Durch den kontinuierlichen Verbesserungsprozess erreichen Scrum Teams schneller ihr Ziel.\n\nEmpfohlen wir die Kombination aus Scrum und Kanban, Scrumban:\nDas Scrum-Framework und die Kanban-Prinzipien ermöglichen es dem Team, seine Arbeit besser zu organisieren. Die Feedback-Schleifen von Scrum gewährleisten, dass das Team weiterhin den maximalen Wert für das Projekt oder Produkt liefert. Ein Kanban-Board ermöglicht dem Team, flexibel und konzentriert zu arbeiten. Um Scrumban zu verstehen, sind Grundkenntnisse in Scrum und Kanban erforderlich.",
        "kanban" : "Die Implementierung des Frameworks erfolgt mithilfe von Kanban-Boards. Diese Methode stellt eine visuelle Form der Projektplanung dar, die Teams dabei unterstützt, ihr Arbeitspensum und ihre Arbeitsabläufe zu visualisieren. Ein Kanban Board ist eine Projekttafel, die die Arbeitsphasen in Spalten organisiert. Jede Spalte steht für eine Phase. Die einfachsten Boards verfügen über Spalten wie z. B. To-do, in Bearbeitung und erledigt. Auf dem Board werden einzelne Aufgaben mit visuellen Karten dargestellt und bewegen sich von einer Spalte in die nächste, bis sie erledigt sind.\n\nEmpfohlen wir die Kombination aus Scrum und Kanban, Scrumban:\nDas Scrum-Framework und die Kanban-Prinzipien ermöglichen es dem Team, seine Arbeit besser zu organisieren. Die Feedback-Schleifen von Scrum gewährleisten, dass das Team weiterhin den maximalen Wert für das Projekt oder Produkt liefert. Ein Kanban-Board ermöglicht dem Team, flexibel und konzentriert zu arbeiten. Um Scrumban zu verstehen, sind Grundkenntnisse in Scrum und Kanban erforderlich.",
        "safeEssential" : "SAFe fördert die Zusammenarbeit und Abstimmung zwischen zahlreichen agilen Teams. Die drei Themenbereiche agile Softwareentwicklung, Lean Produktentwicklung und Systemdenken stehen im Mittelpunkt. SAFe Essential bringt Teams in einem Agile Release Train zusammen, welches an der Entwicklung des Produkts arbeitet.",
        "safeLarge": "SAFe fördert die Zusammenarbeit und Abstimmung zwischen zahlreichen agilen Teams. Die drei Themenbereiche agile Softwareentwicklung, Lean Produktentwicklung und Systemdenken stehen im Mittelpunkt. SAFe Large Solution ist für sehr große Projekte gedacht, wo ein einziger Agile Release Train (siehe SAFe Essential) nicht ausreicht. Agile Release Trains und Supplier werden in einem Solution Train zusammengeführt und koordiniert.",
        "nexus" : "Nexus ist ein Scrum-basiertes Framework, das Wert skalieren soll. Entscheidend ist die Nexus-Gruppe. Eine Nexus-Gruppe umfasst drei bis neun Scrum-Teams, die zusammenarbeiten, um ein einzelnes Produkt zu liefern. Sie besteht aus den Menschen und den Dingen, die für die Lieferung des Produkts erforderlich sind. Ein Nexus verfügt nur über einen Product Owner, der das Product Backlog steuert und aus dem die Scrum-Teams ihre Aufgaben ableiten."
    }

    global attributeNameDict 
    attributeNameDict = {
        "teams": "Anzahl an Teams",
        "teamsize": "Personen pro  Team",
        "client": "Involvierung von Kunden und Stakeholdern",
        "dependency": "Abhängigkeit von äußeren Faktoren",
        "deadline":  "Flexibilität der Deadline",
        "anforderung": "Flexibilität der Anforderungen"
    }