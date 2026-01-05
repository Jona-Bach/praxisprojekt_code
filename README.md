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

Hier ist eine korrigierte und erweiterte Version Ihres Grundlagen-Abschnitts:

---

## 2. Grundlagen

Der folgende Abschnitt beschreibt die theoretischen und fachlichen Grundlagen, die für das Verständnis dieses Projektes notwendig sind. Dabei werden sowohl finanzwirtschaftliche Konzepte als auch technische Grundlagen erläutert, die in der Implementierung der Analyseplattform zur Anwendung kommen.

### 2.1 Finanzmarktgrundlagen

Da diese Plattform auf die Analyse von Finanzdaten ausgelegt ist, ist ein grundlegendes Verständnis zentraler Begriffe und Konzepte der Finanzwirtschaft erforderlich. Die nachfolgend erläuterten Begriffe und Kennzahlen bilden die Basis für die im Dashboard implementierten Analysefunktionen und werden sowohl für grundlegende Datenvisualisierungen als auch als Input für Machine Learning-Algorithmen verwendet.

#### 2.1.1 Grundlegende Begriffe

**OHLCV-Daten**

OHLCV steht für "Open, High, Low, Close, Volume" und bezeichnet die fundamentalen Preisdaten, die die Kursentwicklung einer Aktie innerhalb eines definierten Zeitraums beschreiben. Diese Datenstruktur ist der Standard für die Darstellung von Kursbewegungen an Finanzmärkten:

- **Open**: Der Eröffnungskurs der Aktie zu Beginn der betrachteten Zeitperiode
- **High**: Der höchste Kurs, den die Aktie während der Zeitperiode erreicht hat
- **Low**: Der niedrigste Kurs, den die Aktie während der Zeitperiode erreicht hat
- **Close**: Der Schlusskurs der Aktie am Ende der Zeitperiode
- **Volume**: Die Anzahl der gehandelten Aktien während der Zeitperiode

Diese Datenpunkte werden typischerweise in Form von Candlestick-Charts (Kerzencharts) visualisiert, die eine kompakte Darstellung der Kursbewegungen ermöglichen (Murphy, 1999). OHLCV-Daten bilden die Grundlage für technische Analysen und sind essenziell für die Anwendung von Machine Learning-Algorithmen auf Finanzzeitreihen.

**Aktien**

Aktien (englisch: Stocks oder Shares) sind Unternehmensanteile, die von Kapitalgesellschaften ausgegeben und an Börsen gehandelt werden. *Wenn ein Unternehmen selbst neue Aktien ausgibt und an Investoren verkauft, geschieht dies über den Primärmarkt. Nach dieser ersten Transaktion zwischen den Unternehmen und den Investoren werden die Aktien am Sekundärmarkt unter den Investoren gehandelt, und zwar ohne Mitwirken der Aktiengesellschaft. Wenn man beispielsweise 100 Aktien von Starbucks Coffee kaufen möchte, platziert man eine Order an einer Börse, an der Starbucks unter dem Tickersymbol SBUX gehandelt wird. Man würde die Aktien von jemandem erwerben, der bereits Aktien von Starbucks hält, und nicht von Starbucks selbst.* (Berk & DeMarzo, 2015, S. 32).

Für die vorliegende Plattform sind insbesondere die am Sekundärmarkt gehandelten Aktien relevant, da die verwendeten APIs historische und aktuelle Kursdaten dieser Sekundärmarkttransaktionen bereitstellen.

**Ticker-Symbole**

Ticker-Symbole (oder kurz: Tickers) sind standardisierte Abkürzungen, die zur eindeutigen Identifikation von Wertpapieren an Börsen verwendet werden. Diese Kürzel ermöglichen eine effiziente Referenzierung und Abfrage von Finanzdaten über APIs. Beispiele für Ticker-Symbole sind AMZN (Amazon), GOOGL (Alphabet/Google) oder MSFT (Microsoft). Die Verwendung von Ticker-Symbolen ist zentral für die Datenbeschaffung in dieser Plattform, da sowohl die Alpha Vantage API als auch die Yahoo Finance API Ticker-Symbole als primären Identifikator verwenden.

**Adjusted Close**

Der bereinigte Schlusskurs (Adjusted Close) ist eine Modifikation des regulären Schlusskurses, die Kursanpassungen aufgrund von Dividendenausschüttungen, Aktiensplits und anderen Kapitalmaßnahmen berücksichtigt. Diese Bereinigung ist für historische Analysen von großer Bedeutung, da sie eine verzerrungsfreie Betrachtung der tatsächlichen Wertentwicklung ermöglicht (Yahoo Finance, 2024). Für Machine Learning-Anwendungen wird daher empfohlen, Adjusted Close-Werte anstelle der nominalen Schlusskurse zu verwenden, um Modellverzerrungen zu vermeiden.

#### 2.1.2 Wichtige Finanzkennzahlen

Finanzielle Kennzahlen (Key Performance Indicators, KPIs) dienen der quantitativen Bewertung von Unternehmen und werden sowohl in der Fundamentalanalyse als auch als Features für Machine Learning-Modelle eingesetzt.

**Marktkapitalisierung (Market Capitalization)**

Die Marktkapitalisierung gibt den Börsenwert eines Unternehmens an. *Der Unternehmenswert von börsennotierten Unternehmen zeigt sich im Börsenwert (auch Marktkapitalisierung genannt), der dem Gesamtwert aller börsennotierten Aktien der Aktiengesellschaft entspricht* (Amely & Immenkötter, 2023). 

Die Berechnung erfolgt nach der Formel:

**Marktkapitalisierung = Aktienkurs × Anzahl ausstehender Aktien**

Die Marktkapitalisierung dient als Indikator für die Unternehmensgröße und wird häufig zur Kategorisierung von Aktien verwendet (Large-Cap, Mid-Cap, Small-Cap).

**Kurs-Gewinn-Verhältnis (KGV / P/E Ratio)**

*Das Kurs-Gewinn-Verhältnis (KGV), oder auch Price-Earnings-Ratio (PER), ist der am häufigsten verwendete Multiplikator. Es setzt die Marktkapitalisierung ins Verhältnis zum Jahresüberschuss beziehungsweise – auf eine Aktie bezogen – den Aktienkurs zum Gewinn je Aktie. Das KGV sagt aus, mit dem Wievielfachen des Gewinns ein Unternehmen an der Börse gehandelt wird. Das KGV teilt also Aktionären mit, wie viele Jahre das Unternehmen den angesetzten Gewinn erwirtschaften und ausschütten müsste, bis sie ihren Kaufpreis wieder »reinbekommen«* (Amely & Immenkötter, 2023).

Die Interpretation des KGV ist kontextabhängig: Ein hohes KGV kann auf hohe Wachstumserwartungen hindeuten, während ein niedriges KGV eine Unterbewertung oder geringe Wachstumsaussichten signalisieren kann.

**Kurs-Buchwert-Verhältnis (Price-to-Book Ratio, P/B)**

Das Kurs-Buchwert-Verhältnis vergleicht den aktuellen Börsenkurs einer Aktie mit ihrem bilanziellen Buchwert (Eigenkapital pro Aktie). Die Interpretation erfolgt wie folgt:

- **P/B ≈ 1**: Der Markt bewertet das Unternehmen etwa zu seinem bilanziellen Eigenkapitalwert
- **P/B > 1**: Der Markt erwartet einen Mehrwert durch immaterielle Faktoren wie Markenwert, Wachstumspotenzial oder hohe Profitabilität
- **P/B < 1**: Kann auf eine Unterbewertung, operative Probleme oder bilanzielle Besonderheiten hindeuten

Es ist zu beachten, dass der Buchwert stark von Bilanzierungsvorschriften abhängt und insbesondere bei wissensintensiven Unternehmen mit hohen immateriellen Vermögenswerten weniger aussagekräftig sein kann (Damodaran, 2012).

**Eigenkapitalrendite (Return on Equity, ROE)**

Die Eigenkapitalrendite gibt an, wie effizient ein Unternehmen das eingesetzte Eigenkapital verzinst. Ein höherer ROE indiziert eine höhere Profitabilität im Verhältnis zum Eigenkapital. Die Berechnung erfolgt nach:

**ROE = (Jahresüberschuss / Eigenkapital) × 100%**

Der ROE ist eine zentrale Kennzahl zur Bewertung der Rentabilität und wird häufig im Branchenvergleich herangezogen (Eayrs et al., 2011; Investopedia, 2024a).

**Gewinnmarge (Profit Margin)**

Die Gewinnmarge gibt an, welcher Anteil des Umsatzes als Gewinn verbleibt, nachdem alle Kosten berücksichtigt wurden. Sie wird typischerweise in Prozent ausgedrückt und berechnet sich als:

**Gewinnmarge = (Nettogewinn / Umsatz) × 100%**

Je nach Betrachtung kann zwischen verschiedenen Gewinnmargen unterschieden werden: Bruttogewinnmarge (Gross Margin), operative Gewinnmarge (Operating Margin) und Nettogewinnmarge (Net Profit Margin). Höhere Gewinnmargen deuten auf eine effiziente Kostenstruktur und starke Preissetzungsmacht hin (Investopedia, 2024b).

**Beta-Faktor**

Der Beta-Faktor misst die systematische Volatilität einer Aktie im Verhältnis zu einem Referenzmarkt oder Index. Die Interpretation erfolgt wie folgt:

- **Beta = 1**: Die Aktie schwankt im Durchschnitt genau wie der Referenzindex
- **Beta > 1**: Die Aktie weist höhere Volatilität auf und reagiert stärker auf Marktbewegungen (höheres Risiko)
- **Beta < 1**: Die Aktie ist weniger volatil als der Markt (defensiver Charakter)

*Ein Beta-Faktor (auch kurz Beta oder β) gibt an, wie stark die Aktie im Vergleich zum Markt beziehungsweise zu einem Index schwankt. Man sagt auch, er misst also die Schwankungsintensität (Volatilität) einer Aktie im Vergleich zu einem Index. Hat eine Aktie ein Beta von 1, so verhält sie sich genau wie der Index. Ist das Beta größer als 1, so reagiert die Aktie stärker als der Index. Bei einem Beta zwischen 0 und 1 würde die Aktie auch steigen, wenn der Markt an Wert gewinnt. Der Kursanstieg der Aktie wäre jedoch nicht so groß. Bei einem negativen Beta verhalten sich Index und Aktie gegenläufig: Wenn der Index steigt, verliert die Aktie an Wert und anders herum. Diesen Fall werden Sie aber nur sehr selten antreffen. Beta-Faktoren werden aus der Historie abgeleitet. Sie geben also wieder, wie sich die Aktie in der Vergangenheit im Vergleich zum Markt verhalten hat. Das bedeutet aber nicht, dass dies in Zukunft genauso sein muss* (Amely & Immenkötter, 2023).

Wichtig zu beachten ist, dass der Beta-Faktor vom gewählten Referenzindex, der Branchenzugehörigkeit des Unternehmens und dem betrachteten Zeitraum abhängt. Für Machine Learning-Anwendungen kann Beta als Feature zur Risikoquantifizierung genutzt werden.

#### 2.1.3 Zeitreihenanalyse im Finanzkontext

Finanzdaten weisen typischerweise eine zeitliche Struktur auf, wodurch Zeitreihenanalysemethoden für ihre Verarbeitung besonders relevant sind. Aktienkurse, Handelsvolumina und Finanzkennzahlen werden in regelmäßigen Intervallen erfasst und bilden somit Zeitreihen, deren Analyse spezifische statistische und algorithmische Ansätze erfordert.

Zeitreihenprognosen gehören zu den klassischen Anwendungsfällen des Machine Learning im Finanzbereich. *Eine weitere verbreitete Anwendung ist die Vorhersage von Zeitreihen (wie etwa Aktienkursen)* (Müller & Guido, 2017). Die Besonderheit von Finanzzeitreihen liegt in ihrer Nicht-Stationarität, ihrer hohen Volatilität und der Präsenz von Autokorrelationen, die bei der Modellierung berücksichtigt werden müssen (Box et al., 2015).

Für die vorliegende Plattform sind insbesondere folgende Aspekte der Zeitreihenanalyse relevant:

- **Historische Datenmuster**: Die Identifikation von Trends, Saisonalität und zyklischen Mustern in historischen Kursdaten
- **Feature Engineering**: Die Ableitung zeitabhängiger Features wie gleitende Durchschnitte, Momentum-Indikatoren oder Volatilitätsmaße
- **Sequenzielle Datenverarbeitung**: Die Berücksichtigung der zeitlichen Reihenfolge bei der Modellierung, insbesondere bei der Aufteilung in Trainings- und Testdaten

Diese Konzepte bilden die Grundlage für die Implementierung sowohl der traditionellen Machine Learning-Algorithmen als auch der LLM-basierten Analysen in der Plattform.


### 2.2 Machine Learning Grundlagen

 - Supervised vs. Unsupervised learning: Das Supervised und unsupervised Learning also überwachtes und unüberwachtrs lernen sind beides Begriffe aus der KI. Es beschreibt die Trainingsart eines Modelles und hat 2 verschiedene FUbktionen. Bei dem überwachten lernen handelt es sich um die Trainignsmethode bei dem ein Modell mit vorgefertigten Daten die "gelabelt" also beschrieben sind und versucht darauf zu lernen. Bei Regressionen oder Vorgersagen wird diese Arz von lernen genutzt um vorhgersagen auf Daten machen zz können.

 Bei dem Unüberwahcten lernen, bekommt der alogrithmus keine gelabelten Daten sondern lernt sozusagen "blind" auf den ihm gegebene nDatebn. Diese Art von lernen kann so zuum Beispiel für Clustering oder Reinforcment Learning eingesetzt werden, indem das Modell die Daten nahc ihm logisch erscheinendnen Cluster neinteilt.

# Literatur:
- Berk, Jonathan B.; DeMarzo, Peter M. 2015: Grundlagen der Finanzwirtschaft: Analyse, Entscheidung und Umsetzung, 3., aktualisierte Aufl., Pearson Deutschland GmbH
- Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
- Damodaran, A. (2012). Investment Valuation. Wiley Finance.
- Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control. Wiley.
- Yahoo Finance (2024). Adjusted Close Definition.
- Amely, Tobias, and Christine Immenkötter. Investition und Finanzierung Für Dummies, John Wiley & Sons, Incorporated, 2023
- Müller, Andreas C., and Sarah Guido. Einführung in Machine Learning mit Python : Praxiswissen Data Science, o'Reilly, 2017.
- Eayrs, Willis E., et al. Corporate Finance Training : Planung, Bewertung und Finanzierung Von Unternehmen, Schaffer-Poeschel Verlag fur Wirtschaft Steuern Recht GmbH, 2011.
- https://www.investopedia.com

