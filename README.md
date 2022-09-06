README.md

# Intrexx Sample Admin API - BETA

## Einführung

Administratoren müssen unterschiedliche Systeme installieren, pflegen und aktuell halten. Dies ist ein unüberblickbarer Blumenstrauß an Aufgaben, die mit unterschiedlichsten Tools umgesetzt werden müssen. Dies alles von Hand zu erledigen, gleicht einer Herkulesaufgabe. Alles, was automatisierbar ist, wird automatisiert, denn es ist schneller, einfacher und weniger fehleranfällig. 

Besonders Betreiber, die eine Skalierung haben und/oder QM-Prozessen unterworfen sind, ist daran gelegen alle Tätigkeiten, die eine Intrexx Infrastruktur betreffen, weitestgehend zu automatisieren und in bestehende Abläufe einzubinden. 

Die Administration API bietet eine stabile Infrastruktur, die es erlaubt wichtige administrative Tätigkeiten auch über gängige Werkzeuge der Automatisierung auszuüben.  Gerade DevOps nutzen Automatisierungswerkzeuge, in die problemlos das REST-basierende Administration API eingebunden werden. Die Schnittstelle stellt bereits komfortabel eine Swagger / OpenAPI kompatible Dokumentation zur Verfügung. Insbesondere das Thema Staging (Transport von Applikationen und Prozessen von Entwicklungs- zu Test- bis hin zu PreProd- bzw. Produktiksystem) kann so über ein CLI (Command Line Interface) scriptgesteuert und damit immer nachvollziehbar umgesetzt werden.

## Vorraussetzung 

- Intrexx ab 10.10 (https://www.intrexx.com)
- Python (https://www.python.org/)
- Python requests (https://pypi.org/project/requests/)
