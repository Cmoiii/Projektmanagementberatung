# Projektmanagementberatung

Welche Projektmanagementmethode ist die richtige für mein Projekt?
Dieses Tool hilft Ihnen bei der Entscheidung.

Das Programm wurde mit PyInstaller kompiliert, die ausführbare Datei befindet sich in den Releases.
Das Programm kann man selber mit PyInstaller kompilieren: 
```
python -m PyInstaller --onefile --add-data "./icons/projectmanagement.ico;./icons" --add-data "sidebar/sidebar_home.png;./sidebar" --add-data "sidebar/sidebar_overview.png;./sidebar" --add-data "sidebar/sidebar_result.png;./sidebar" --add-data "sidebar/sidebar_step1.png;./sidebar" --add-data "sidebar/sidebar_step2.png;./sidebar" --windowed --name Projektmanagementberatung --icon=.\icons\projectmanagement.ico main.py
```

Der Python-Code kann  direkt ausgeführt werden mit der Datei main.py.
Dazu  wird das Modul Pillow benötigt.
