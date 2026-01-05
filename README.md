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

---

## 2. Grundlagen

Der Folgende abschnitt beschreibt die Grundlagen, die für das weitere Verstehen dieses Projektes nötig sind.

### 2.1 Finanzmarktgrundlagen

Da dieses Dahsbaoed auf Finanzanalyse ausgelegt ist, werden viele wichtige Funktionen und Begriffe  / Methoen die mit der Finanzwelt zu tun haben verwendet, daher sind Finanzmarkttgrundlagen wichtig um das Projekt zu verstehen. Einige Finanzbegriffe werden für die analyse auf der "Data" Seite verwendet, wärhend andere für Machine Learning algorthmen verwendet werden können oder als Grunddaten hier eimgebaut sind

- **Grundlegende Begriffe** 
    - OHLCV = OHLCV steht für "Open High Low Close Volume", und steht für die Priesentwicklung die Aktiens innerhalb eines definerten Zeitraums durchläuft. Der Open Preis ist der Preis der Aktie zum Start der Zeitperiode hat, High ist der höchste Preis der die Aktie in dem Zeitraum erreicht, low ist der niedrigste Preis der Aktie in dem Zeitraum, close ist der Letzte Preis der Akite im Zeitraun, Volume ist die Anzahl der Aktien die in dem Zeitraum gehandelt wurden. Typischerweise werden diese Zustände in einer sogenannten Candle "Kerze" dargestellt um diese veränderungen zu visualiseren.
    - Aktien = Aktien( auf Englisch Stocks) sind Unternehmensanteile die am Markt von großen Unternehmen verkauft werden. *Wenn ein Unternehmen selbst neue Aktien ausgibt und an Investoren verkauft, geschieht dies über den Primärmarkt . Nach dieser ersten Transaktion zwischen den Unternehmen und den Investoren werden die Aktien am Sekundärmarkt unter den Investoren gehandelt, und zwar ohne Mitwirken der Aktiengesellschaft. Wenn man beispielsweise 100 Aktien von Starbucks Coffee kaufen möchte, platziert man eine Order an einer Börse, an der Starbucks unter dem Tickersymbol SBUX gehandelt wird. Man würde die Aktien von jemandem erwerben, der bereits Aktien von Starbucks hält, und nicht von Starbucks selbst.*
    (Berk, Jonathan B.; DeMarzo, Peter M. 2015: Grundlagen der Finanzwirtschaft: Analyse, Entscheidung und Umsetzung, 3., aktualisierte Aufl., Pearson Deutschland GmbH, S. 32, verfügbar über ProQuest Ebook Central, Zugriff am 05.01.2026).
    - TICKERS = Tickers ist die Englische Bezeichnung der Börsen Kürzel welche für Aktien an den Märkten verwendet werden: BSP: AMZN, GOOGL, MSFT.
    - Adjustet Close = Die adjustet Close angabe, gibt an, dass die Close Preise bei einem Dividenden Split korrigiert worden sind. Somit sind diese niícht verfälscht und eignen sich besser für Analysen.
    

- **Wichtige Finanzkennzahlen**
    - Market Capitalization: Die Markt Kapitalisierung gibt den Börsenwert eines Unternehmens an. *Der Unternehmenswert von börsennotierten Unternehmen zeigt sich im Börsenwert (auch MarktkapitalisierungMarktkapitalisierung genannt), der dem Gesamtwert aller börsennotierten Aktien der Aktiengesellschaft entspricht.*
    Amely, Tobias, and Christine Immenkötter. Investition und Finanzierung Für Dummies, John Wiley & Sons, Incorporated, 2023

    Die Marktkapitalisierung wird durch Marktkapitalisierung = Aktienkurs × Anzahl ausstehender Aktien berechnet

    - PE-Ratio (KGV)
    Das Kurs-Gewinn-Verhältnis (KGV)Kurs-Gewinn-Verhältnis (KGV), oder auch Price-Earnings-Ratio (PER), ist der am häufigsten verwendete Multiplikator. Es setzt die Marktkapitalisierung ins Verhältnis zum Jahresüberschuss beziehungsweise – auf eine Aktie bezogen – den Aktienkurs zum Gewinn je Aktie. 
    Das KGV sagt aus, mit dem Wievielfachen des Gewinns ein Unternehmen an der Börse gehandelt wird. Das KGV teilt also Aktionären mit, wie viele Jahre das Unternehmen den angesetzten Gewinn erwirtschaften und ausschütten müsste, bis sie ihren Kaufpreis wieder »reinbekommen«.
    Amely, Tobias, and Christine Immenkötter. Investition und Finanzierung Für Dummies, John Wiley & Sons, Incorporated, 2023. 

    - Kurs-Buchwert-Verhältnis (Price/Book):
    Vergleicht den Börsenkurs mit dem Buchwert (Eigenkapital aus der Bilanz).
    Interpretation:
	•	P/B ≈ 1: Markt bewertet etwa “auf Buchwert”.
	•	P/B > 1: Markt erwartet Mehrwert (Marke, Wachstum, hohe Profitabilität).
	•	P/B < 1: kann auf Probleme/Unterbewertung hindeuten, oder auf bilanzielle Besonderheiten.

    Wichtig! Der Buchwert ist von der Bilanz des Unternehmens abhängig, kann also varriieren

    - ROE (Return on Equity): 
    Der ROE gibt an wie stark das Unternehmen das Eigenkapital verzinst. Ein Höherer ROE bedeutet, dass ein Unternehmen viel Gewinn macht im Zusammengang mit seinem Eigenkapital. ROE = Jahresüberschuss / Eigenkapital × 100%
    Siehe: Vergleich:
    Eayrs, Willis E., et al. Corporate Finance Training : Planung, Bewertung und Finanzierung Von Unternehmen, Schaffer-Poeschel Verlag fur Wirtschaft Steuern Recht GmbH, 2011.
    Weitere Quelle: https://www.investopedia.com/terms/r/returnonequity.asp

    - Gewinnmarge (Profit Margin): Die Gewinnmarge gibt an wie viel Gewinn (oder operativer Gewinn) pro Euro Umsatz übrig bleibt. (hier wieter ausführen)
    Quelle: https://www.investopedia.com/ask/answers/122314/what-difference-between-gross-margin-and-profit-margin.asp

    - Beta:
    beta misst wie stark eine Aktie im Vergleich zum Gesamtmarkt schwank.

    Interpretation:
	•	Beta = 1: schwankt etwa wie der Markt.
	•	Beta > 1: schwankt stärker (mehr Risiko/Volatilität).
	•	Beta < 1: schwankt weniger (defensiver).


    *Ein Beta-Faktor (auch kurz Beta oder β) gibt an, wie stark die Aktie im Vergleich zum Markt beziehungsweise zu einem Index schwankt. Man sagt auch, er misst also die Schwankungsintensität (Volatilität) einer Aktie im Vergleich zu einem Index. Hat eine Aktie ein Beta von 1, so verhält sie sich genau wie der Index. Ist das Beta größer als 1, so reagiert die Aktie stärker als der Index. Bei einem Beta zwischen 0 und 1 würde die Aktie auch steigen, wenn der Markt an Wert gewinnt. Der Kursanstieg der Aktie wäre jedoch nicht so groß. Bei einem negativen Beta verhalten sich Index und Aktie gegenläufig: Wenn der Index steigt, verliert die Aktie an Wert und anders herum. Diesen Fall werden Sie aber nur sehr selten antreffen. Beta-Faktoren werden aus der Historie abgeleitet. Sie geben also wieder, wie sich die Aktie in der Vergangenheit im Vergleich zum Markt verhalten hat. Das bedeutet aber nicht, dass dies in Zukunft genauso sein muss.*
    Amely, Tobias, and Christine Immenkötter. Investition und Finanzierung Für Dummies, John Wiley & Sons, Incorporated, 2023. 

    **Wichtig zu beachte ist:** Beta hängt davon ab, welcher Marktindex genutzt wird, in welcher Industrie sich das Unternehmen befindet und welcher Zeitraum betrachtet wird.

    - Die Wichtigkeit von Zeitreihenanalyse bei der Finanzbewertung: (hier bitte kurz ergänzen, eine weitere Quelle wäre diese Zitat hier "Eine weitere verbreitete Anwendung ist die Vorhersage von Zeitreihen (wie etwa Aktienkursen)", der ebenfalls ein Stapel Bücher gewidmet ist.
    Müller, Andreas C., and Sarah Guido. Einführung in Machine Learning mit Python : Praxiswissen Data Science, o'Reilly, 2017., baue diese ein)

### 2.2 Machine Learning Grundlagen

 - Supervised vs. Unsupervised learning: Das Supervised und unsupervised Learning also überwachtes und unüberwachtrs lernen sind beides Begriffe aus der KI. Es beschreibt die Trainingsart eines Modelles und hat 2 verschiedene FUbktionen. Bei dem überwachten lernen handelt es sich um die Trainignsmethode bei dem ein Modell mit vorgefertigten Daten die "gelabelt" also beschrieben sind und versucht darauf zu lernen. Bei Regressionen oder Vorgersagen wird diese Arz von lernen