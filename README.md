# Praxisprojekt Berichtheft Jonathan 

---

## 1. Einleitung

### 1.1 Problemstellung

Die Analyse von Aktien und anderen Anlagemöglichkeiten stellt für viele Privatanleger eine erhebliche Herausforderung dar. Insbesondere Einsteiger stoßen auf mehrere grundlegende Probleme:

Erstens fehlt es häufig an einer fundierten Datengrundlage und dem notwendigen Fachwissen, um fundierte Investitionsentscheidungen zu treffen. Die Komplexität der Finanzmärkte und die Vielzahl verfügbarer Kennzahlen überfordern unerfahrene Anleger und erschweren den Einstieg in die eigenständige Aktienanalyse.

Zweitens werden zunehmend Large Language Models (LLMs) für finanzielle Entscheidungen und Investitionsempfehlungen herangezogen, ohne dass ein systematischer Vergleich mit etablierten quantitativen Analysemethoden vorliegt. Es besteht ein Bedarf, die Leistungsfähigkeit von LLMs im Vergleich zu traditionellen Machine Learning-Algorithmen im Kontext der Finanzmarktanalyse zu evaluieren.

Drittens mangelt es vielen Interessierten an Kenntnissen über die Implementierung und Anwendung von Machine Learning-Algorithmen für die Analyse von Finanzdaten. Die technische Einstiegshürde verhindert, dass potenzielle Nutzer von den Möglichkeiten moderner Analysemethoden profitieren können.

### 1.2 Zielsetzung

Ziel dieses Praxisprojekts ist die Entwicklung einer webbasierten Analyseplattform, die Nutzern einen niedrigschwelligen Zugang zur datengestützten Aktienanalyse ermöglicht. Die Plattform verfolgt folgende Kernziele:

1. **Datenintegration und -bereitstellung**: Implementierung einer Funktionalität zum automatisierten Download und zur Verwaltung von Finanzdaten, um Nutzern eine solide Datengrundlage für ihre Analysen zu bieten.

2. **Standardisierte Finanzanalyse**: Bereitstellung grundlegender Analysewerkzeuge und Kennzahlen, die eine erste Bewertung von Aktien ohne tiefgreifende Vorkenntnisse ermöglichen.

3. **Machine Learning-Integration**: Implementierung vorgefertigter Machine Learning-Algorithmen, die es Nutzern erlauben, sowohl heruntergeladene Finanzdaten als auch eigene Datensätze zu trainieren und auszuwerten, ohne selbst Programmierkenntnisse besitzen zu müssen.

4. **Vergleichende Evaluation von Analysemethoden**: Entwicklung einer Funktionalität zum Training und Vergleich von traditionellen Machine Learning-Modellen und Large Language Models auf identischen Datensätzen. Dabei soll insbesondere die Möglichkeit geschaffen werden, zusätzliches Kontextwissen (z.B. politische Informationen) in die LLM-Analyse zu integrieren.

5. **Nutzerunterstützung durch Conversational AI**: Integration eines Chatbot-basierten Sprachassistenten, der Nutzer bei der Bedienung der Plattform unterstützt und den Umgang mit den verschiedenen Analysewerkzeugen erleichtert.

Durch die Kombination dieser Komponenten soll eine Plattform entstehen, die sowohl als Lernumgebung für Einsteiger als auch als praktisches Analysewerkzeug für fortgeschrittene Nutzer dient und gleichzeitig einen empirischen Vergleich verschiedener Analysemethoden im Finanzkontext ermöglicht. Die Plattform wird auf Englisch bereitgestellt, da Englisch die führende Sprache in Wirtschaft und Finanzwesen ist und so eine breite, internationale Nutzung ermöglicht.

### 1.3 Herangehensweise

Die Entwicklung der Analyseplattform erfolgt in einem iterativen Prozess und basiert auf einer modularen Softwarearchitektur, die eine klare Trennung zwischen Frontend, Backend und Datenverarbeitung gewährleistet.

#### 1.3.1 Technologie-Stack

Für die Realisierung des Projekts wird ein moderner Technologie-Stack eingesetzt:

- **Frontend**: Das Benutzerinterface wird mit Streamlit implementiert, einem Framework für die schnelle Entwicklung von datenorientierten Webanwendungen in Python. Dies ermöglicht eine intuitive Bedienoberfläche ohne umfangreiche Webentwicklungskenntnisse.

- **Datenvisualisierung**: Zur grafischen Darstellung von Finanzdaten und Analyseergebnissen wird Plotly verwendet, das interaktive und professionelle Visualisierungen ermöglicht.

- **Machine Learning**: Für die Implementierung der Machine Learning-Algorithmen dient Scikit-Learn als primäres Framework, das eine breite Palette standardisierter Algorithmen und Werkzeuge für das Training und die Evaluation von Modellen bereitstellt.

- **Large Language Model Integration**: Die LLM-Funktionalität wird über Ollama realisiert, das sowohl lokal auf dem System des Nutzers als auch in einem Docker-Container betrieben werden kann.

- **Deployment**: Die gesamte Anwendung wird als Docker-Container bereitgestellt, um Plattformunabhängigkeit und eine unkomplizierte Installation ohne manuelle Konfiguration von Abhängigkeiten zu gewährleisten. Der Quellcode wird über GitHub versioniert und öffentlich zugänglich gemacht.

#### 1.3.2 Datengrundlage

Die Plattform integriert Finanzdaten aus zwei Hauptquellen:

1. **Alpha Vantage API**: Ermöglicht den Zugriff auf umfassende Finanzdaten und erfordert einen individuellen API-Schlüssel, den Nutzer (eingeschränkt) kostenlos beziehen können.

2. **Yahoo Finance API**: Dient als ergänzende, frei zugängliche Datenquelle für historische und aktuelle Marktdaten.

Die verfügbaren Daten umfassen:
- **OHLCV-Daten** (Open, High, Low, Close, Volume) für historische Kursentwicklungen
- **Unternehmensmetriken** wie Kennzahlen zur Fundamentalanalyse
- **Aktuelle Preisinformationen**, die auf Abruf aktualisiert werden können
- **Nutzerdefinierte Datensätze**, die Anwender für eigene Analysen hochladen können

#### 1.3.3 Softwarearchitektur

Das Projekt folgt einer klaren Strukturierung in Frontend und Backend:

- **Backend**: Umfasst die Datenverarbeitungslogik, Datenbankanbindungen, API-Services und die Implementierung der Machine Learning-Algorithmen. Diese Komponenten sind modular aufgebaut und voneinander entkoppelt, um Wartbarkeit und Erweiterbarkeit zu gewährleisten.

- **Frontend**: Das Streamlit-basierte Dashboard greift auf die Backend-Funktionen zu und stellt die Ergebnisse benutzerfreundlich dar.

- **Datenverwaltung**: Alle persistenten Daten werden strukturiert in einem dedizierten Data-Ordner gespeichert, wobei eine Datenbankstruktur die effiziente Verwaltung und Abfrage von Finanzdaten ermöglicht.

#### 1.3.4 Entwicklungsprozess

Die Implementierung erfolgt in folgenden Schritten:

1. **Datenschicht**: Aufbau der Datenbankstruktur und Implementierung der API-Anbindungen für den automatisierten Datenimport.

2. **Backend-Funktionalität**: Entwicklung der Datenverarbeitungslogik und Implementierung der Machine Learning-Algorithmen sowie der LLM-Integration.

3. **Frontend-Entwicklung**: Gestaltung des Streamlit-Dashboards mit Zugriff auf alle Backend-Funktionen und intuitive Nutzerführung.

4. **Integration und Testing**: Verbindung aller Komponenten und Sicherstellung der Funktionalität über verschiedene Deployment-Szenarien (lokal, Docker-Container).


