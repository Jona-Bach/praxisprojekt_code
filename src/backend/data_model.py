kpi_list = [
    "Kurs-Buchwert-Verhältnis (KBV)",
    "Kurs-Cashflow-Verhältnis (KCV)",
    "Dividendenrendite",
    "Ausschüttungsquote (Payout Ratio)",
    "Eigenkapitalrendite (ROE)",
    "Gesamtkapitalrendite (ROA)",
    "Return on Capital Employed (ROCE)",
    "Return on Invested Capital (ROIC)",
    "Bruttogewinnmarge",
    "EBIT-Marge",
    "EBITDA-Marge",
    "Nettogewinnmarge",
    "Umsatzwachstum",
    "Gewinnwachstum",
    "Kapitalumschlag",
    "Working Capital",
    "Cashflow-Marge",
    "Liquidität 1. Grades (Cash Ratio)",
    "Liquidität 2. Grades (Quick Ratio)",
    "Liquidität 3. Grades (Current Ratio)",
    "Eigenkapitalquote",
    "Fremdkapitalquote",
    "Dynamischer Verschuldungsgrad",
    "Zinsdeckungsgrad",
    "Anlagendeckungsgrad I",
    "Anlagendeckungsgrad II",
    "Kurs-Gewinn-Verhältnis (Wachstum) (KGV)",
    "Kurs-Umsatz-Verhältnis (KUV)",
    "PEG Ratio",
    "Free Cashflow",
    "Operativer Cashflow",
    "Gewinn je Aktie (EPS)",
    "Verschuldungsgrad",
    "EV/EBITDA",
    "Beta",
    "Graham-Number"
]

alpha_vantage_kpis = {
    "Kurs-Buchwert-Verhältnis (KBV)": "PriceToBookRatio",
    "Dividendenrendite": "DividendYield",
    "Ausschüttungsquote (Payout Ratio)": "PayoutRatio",
    "Eigenkapitalrendite (ROE)": "ReturnOnEquityTTM",
    "Gesamtkapitalrendite (ROA)": "ReturnOnAssetsTTM",
    "Nettogewinnmarge": "ProfitMargin",
    "Umsatzwachstum": "QuarterlyRevenueGrowthYOY",  # *4 für annualisiert
    "Gewinnwachstum": "QuarterlyEarningsGrowthYOY",  # *4 für annualisiert
    "Kapitalumschlag": "AssetTurnover",
    "Cashflow-Marge": "operating_cashflow_margin",   # operatingCashFlow / revenue (selbst berechnen)
    "Eigenkapitalquote": "equityRatio",
    "Fremdkapitalquote": "debtRatio",
    "Kurs-Gewinn-Verhältnis (Wachstum) (KGV)": "PERatio",
    "Kurs-Umsatz-Verhältnis (KUV)": "PriceToSalesRatioTTM",
    "PEG Ratio": "PEGRatio",
    "Free Cashflow": "freeCashFlow",                 # operatingCashFlow - capex
    "Operativer Cashflow": "operatingCashFlow",
    "Gewinn je Aktie (EPS)": "EPS",
    "EV/EBITDA": "EVToEBITDA",
    "Beta": "Beta"
}

initial_tickers = [
    "AAPL",   # Apple
    "MSFT",   # Microsoft
    "GOOGL",  # Alphabet (Google)
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "TSLA",   # Tesla
    "NVDA",   # Nvidia
    "JPM",    # JPMorgan Chase
    "V",      # Visa
    "NFLX"    # Netflix
]





TICKERS = [
    "NVDA",   # 1
    "OPEN",   # 2
    "ONDS",   # 3
    "PLUG",   # 4
    "INTC",   # 5
    "TSLA",   # 6
    "BBAI",   # 7
    "SOFI",   # 8
    "GOOGL",  # 9
    "F",      # 10
    "NU",     # 11
    "PFE",    # 12
    "GRAB",   # 13
    "PLTR",   # 14
    "AMZN",   # 15
    "AMD",    # 16
    "DNN",    # 17
    "AAL",    # 18
    "ACHR",   # 19
    "AAPL",   # 20
    "T",      # 21
    "MARA",   # 22
    "CIFR",   # 23
    "NIO",    # 24
    "BMNR",   # 25
    "BBD",    # 26
    "RGTI",   # 27
    "SOUN",   # 28
    "IREN",   # 29
    "WULF",   # 30
    "KVUE",   # 31
    "NOK",    # 32
    "ORCL",   # 33
    "PCG",    # 34
    "BAC",    # 35
    "GOOG",   # 36
    "VALE",   # 37
    "WMT",    # 38
    "NFLX",   # 39
    "SNAP",   # 40
    "QBTS",   # 41
    "RIVN",   # 42
    "HOOD",   # 43
    "RIG",    # 44
    "CRWV",   # 45
    "ABEV",   # 46
    "WBD",    # 47
    "BE",     # 48
    "APLD",   # 49
    "MU",  # 50
    "BULL",   # 51
    "NBIS",   # 52
    "RKT",    # 53
    "UBER",   # 54
    "RXRX",   # 55
    "HBAN",   # 56
    "VZ",     # 57
    "QS",     # 58
    "MSFT",   # 59
    "CMCSA",  # 60
    "BTE",    # 61
    "AMCR",   # 62
    "EOSE",   # 63
    "AVGO",   # 64
    "MSTR",   # 65
    "IONQ",   # 66
    "BBWI",   # 67
    "JOBY",   # 68
    "SMCI",   # 69
    "CLSK",   # 70
    "BTG",    # 71
    "KO",     # 72
    "GGB",    # 73
    "AGNC",   # 74
    "QUBT",   # 75
    "SMR",    # 76
    "CSCO",   # 77
    "ET",     # 78
    "HL",     # 79
    "VICI",   # 80
    "MRK",    # 81
    "GAP",    # 82
    "HPE",    # 83
    "CMG",    # 84
    "OKLO",   # 85
    "CLF",    # 86
    "META",   # 87
    "TSM",    # 88
    "PYPL",   # 89
    "SLB",    # 90
    "CDE",    # 91
    "STLA",   # 92
    "SNDK",   # 93
    "OWL",    # 94
    "ITUB",   # 95
    "DOW",    # 96
    "CRCL",   # 97
    "EXAS",   # 98
    "PATH", 
    "LYFT",   # 101
    "NVO",    # 102
    "FCX",    # 103
    "RKLB",   # 104
    "VLY",    # 105
    "HIMS",   # 106
    "RIOT",   # 107
    "CCL",    # 108
    "CSX",    # 109
    "LEN",    # 110
    "UUUU",   # 111
    "ANET",   # 112
    "INFY",   # 113
    "CPRT",   # 114
    "PBR",    # 115
    "COMP",   # 116
    "KEY",    # 117
    "BABA",   # 118
    "MRVL",   # 119
    "WFC",    # 120
    "CORZ",   # 121
    "AUR",    # 122
    "B",      # 123 (Barrick Mining Corporation → Ticker wirklich nur "B")
    "XOM",    # 124
    "CVE",    # 125
    "TTD",    # 126
    "AG",     # 127
    "KDP",    # 128
    "KMI",    # 129
    "DKNG",   # 130
    "LRCX",   # 131
    "NCLH",   # 132
    "IQ",     # 133
    "ON",     # 134
    "C",      # 135 (Citigroup Inc.)
    "CAG",    # 136
    "BMY",    # 137
    "RF",     # 138
    "COLD",   # 139
    "NEE",    # 140
    "ERIC",   # 141
    "MRNA",   # 142
    "PTON",   # 143
    "BSX",    # 144
    "ASTS",   # 145
    "HAL",    # 146
    "GLXY",   # 147
    "JNJ",    # 148
    "XYZ",    # 149 (Block, Inc. → Ticker “SQ” existiert, aber du listest “XYZ” als Symbol)
    "PINS",   # 150
    "NGD",    # 151
    "CARR",   # 152
    "LUMN",   # 153
    "TGT",    # 154
    "NKE",    # 155
    "COIN",   # 156
    "OBDC",   # 157
    "PG",     # 158
    "LYG",    # 159
    "JD",     # 160
    "KHC",    # 161
    "MCHP",   # 162
    "JPM",    # 163
    "TXN",    # 164
    "CPNG",   # 165
    "ZETA",   # 166
    "TOST",   # 167
    "UMC",    # 168
    "VG",     # 169
    "EXK",    # 170
    "DVN",    # 171
    "MDT",    # 172
    "OSCR",   # 173
    "STUB",   # 174
    "PL",     # 175
    "NUVB",   # 176
    "MDLZ",   # 177
    "WDC",    # 178
    "MP",     # 179
    "CZR",    # 180
    "UEC",    # 181
    "GM",     # 182
    "QCOM",   # 183
    "DIS",    # 184
    "EQT",    # 185
    "VRT",    # 186
    "XPEV",   # 187
    "EQX",    # 188
    "RBLX",   # 189
    "GILD",   # 190
    "PRMB",   # 191
    "SHOP",   # 192
    "SBUX",   # 193
    "UAL",    # 194
    "NEM",    # 195
    "KIM",    # 196
    "BA",     # 197
    "CNH",    # 198
    "TJX",    # 199
    "CX",     #
    "IBRX",   # 201
    "HLN",    # 202
    "TEVA",   # 203
    "VFC",    # 204
    "UWMC",   # 205
    "CNQ",    # 206
    "PR",     # 207
    "DAL",    # 208
    "MPW",    # 209
    "CRGY",   # 210
    "FSM",    # 211
    "MO",     # 212
    "PDD",    # 213
    "PPTA",   # 214
    "ABT",    # 215
    "S",      # 216
    "AES",    # 217
    "CVX",    # 218
    "TFC",    # 219
    "CAVA",   # 220
    "OXY",    # 221
    "HRL",    # 222
    "MS",     # 223
    "BTDR",   # 224
    "CWAN",   # 225
    "VTRS",   # 226
    "ESTC",   # 227
    "V",      # 228
    "UPS",    # 229
    "DBK.DE", # 230
    "CLVT",   # 231
    "BP",     # 232
    "BB",     # 233
    "CFLT",   # 234
    "U",      # 235
    "AMAT",   # 236
    "HST",    # 237
    "NXE",    # 238
    "STNE",   # 239
    "TME",    # 240
    "UNH",    # 241
    "CRDO",   # 242
    "DELL",   # 243
    "GEHC",   # 244
    "MGM",    # 245
    "FAST",   # 246
    "AEG",    # 247
    "BAX",    # 248
    "SCHW",   # 249
    "ELAN",   # 250
      "PPL",     # 251
    "APH",     # 252
    "PANW",    # 253
    "WMB",     # 254
    "BKR",     # 255
    "ABBV",    # 256
    "BKD",     # 257
    "DTE.DE",  # 258
    "CTSH",    # 259
    "VNET",    # 260
    "PTEN",    # 261
    "ACI",     # 262
    "CNC",     # 263
    "PEP",     # 264
    "USB",     # 265
    "GENI",    # 266
    "ROST",    # 267
    "ASX",     # 268
    "LCID",    # 269
    "FLNC",    # 270
    "GT",      # 271
    "WU",      # 272
    "TU",      # 273
    "LITE",    # 274
    "JHX",     # 275
    "SE",      # 276
    "CL",      # 277
    "BEKE",    # 278
    "KGC",     # 279
    "CRM",     # 280
    "HD",      # 281
    "GIS",     # 282
    "AZN",     # 283
    "BCS",     # 284
    "NLY",     # 285
    "FIG",     # 286
    "FLG",     # 287
    "HUT",     # 288
    "O",       # 289
    "AEO",     # 290
    "CCJ",     # 291
    "DOC",     # 292
    "LUV",     # 293
    "CELH",    # 294
    "AHR",     # 295
    "COP",     # 296
    "GLW",     # 297
    "EXC",     # 298
    "WIT",     # 299
    "COMM",    # 300
      "IBKR",   # 301
    "WY",     # 302
    "M",      # 303
    "ABNB",   # 304
    "RITM",   # 305
    "PM",     # 306
    "ALAB",   # 307
    "SNOW",   # 308
    "ENPH",   # 309
    "VOD",    # 310
    "PAGS",   # 311
    "EQNR",   # 312
    "ONON",   # 313
    "FRMI",   # 314
    "SBSW",   # 315
    "DASH",   # 316
    "QXO",    # 317
    "KR",     # 318
    "RUN",    # 319
    "FITB",   # 320
    "ORLY",   # 321
    "CVS",    # 322
    "TEM",    # 323
    "XP",     # 324
    "HBI",    # 325
    "AXTA",   # 326
    "SO",     # 327
    "AVTR",   # 328
    "ZTS",    # 329
    "MRP",    # 330
    "CPB",    # 331
    "CHWY",   # 332
    "CTRA",   # 333
    "VST",    # 334
    "TMUS",   # 335
    "YMM",    # 336
    "WRD",    # 337
    "ADT",    # 338
    "ARM",    # 339
    "ENR.DE", # 340
    "GEN",    # 341
    "IAG",    # 342
    "IVZ",    # 343
    "DDOG",   # 344
    "UPST",   # 345
    "RTX",    # 346
    "LOW",    # 347
    "LYB",    # 348
    "CCC",    # 349
    "BRK-B",  # 350
      "BEN",     # 351
    "APP",     # 352
    "OGE",     # 353
    "PBR-A",   # 354
    "AR",      # 355
    "SW",      # 356
    "TECK",    # 357
    "ACN",     # 358
    "KKR",     # 359
    "FE",      # 360
    "STM",     # 361
    "KMB",     # 362
    "GTM",     # 363
    "TMC",     # 364
    "SEDG",    # 365
    "ESI",     # 366
    "CSGP",    # 367
    "APA",     # 368
    "LI",      # 369
    "IBM",     # 370
    "WSC",     # 371
    "MBLY",    # 372
    "IOT",     # 373
    "FLO",     # 374
    "MOS",     # 375
    "PCAR",    # 376
    "ZIM",     # 377
    "CART",    # 378
    "GE",      # 379
    "TSCO",    # 380
    "AIG",     # 381
    "PONY",    # 382
    "D",       # 383 (Dominion Energy)
    "FTNT",    # 384
    "IP",      # 385
    "GME",     # 386
    "CNP",     # 387
    "PSKY",    # 388
    "INVH",    # 389
    "DXCM",    # 390
    "LHA.DE",  # 391
    "BN",      # 392
    "AFRM",    # 393
    "KMX",     # 394
    "DHI",     # 395
    "GTLB",    # 396
    "MIR",     # 397
    "IFX.DE",  # 398
    "BRBR",    # 399
    "CFG",     # 400
    "CLS",     # 401
    "HOG",     # 402
    "LVS",     # 403
    "GNW",     # 404
    "MNST",    # 405
    "BF-B",    # 406
    "CRBG",    # 407
    "CTVA",    # 408
    "AA",      # 409
    "EIX",     # 410
    "JCI",     # 411
    "IBN",     # 412
    "ADPT",    # 413
    "ARCC",    # 414
    "IPG",     # 415
    "BJ",      # 416
    "TTEK",    # 417
    "COHR",    # 418 # AB HIER NUR NOCH HINZUGEFÜGTE:


    # AB HIER NUR NOCH HINZUGEFÜGTE:


]


metrics_list = [
    "symbol",
    "revenuePerShare",
    "netIncomePerShare",
    "operatingCashFlowPerShare",
    "freeCashFlowPerShare",
    "cashPerShare",
    "bookValuePerShare",
    "tangibleBookValuePerShare",
    "interestDebtPerShare",

    "marketCap",
    "enterpriseValue",
    "peRatio",
    "priceToSalesRatio",
    "pocfratio",
    "pfcfRatio",
    "pbRatio",
    "evToSales",
    "enterpriseValueOverEBITDA",

    "earningsYield",
    "freeCashFlowYield",

    "debtToEquity",
    "debtToAssets",
    "netDebtToEBITDA",

    "currentRatio",
    "quickRatio",
    "cashRatio",

    "daysSalesOutstanding",
    "daysPayablesOutstanding",
    "daysOfInventoryOnHand",

    "receivablesTurnover",
    "payablesTurnover",
    "inventoryTurnover",

    "returnOnAssets",
    "returnOnEquity",
    "returnOnCapitalEmployed",

    "operatingCashFlowSalesRatio",
    "freeCashFlowOperatingCashFlowRatio",

    "priceToFreeCashFlowsRatio",
    "priceToOperatingCashFlowsRatio",
    "enterpriseValueMultiple",
      "interestCoverage",
    "incomeQuality",
    "dividendYield",
    "payoutRatio",
    "researchAndDdevelopementToRevenue",
    "capexToOperatingCashFlow",
    "capexToRevenue",
    "capexToDepreciation",
    "stockBasedCompensationToRevenue",
    "roic",
    "returnOnTangibleAssets",
    "workingCapital",
    "tangibleAssetValue",
    "netCurrentAssetValue",
    "investedCapital",
    "assetTurnover",
    "fixedAssetTurnover",
    "operatingProfitMargin",
    "pretaxProfitMargin",
    "netProfitMargin",
    "grossProfitMargin",
    "debtRatio",
    "totalDebtToCapitalization",
    "cashConversionCycle",
    "operatingCycle",
]

extra_metrics_explanations = [
    "Umsatz pro Aktie – guter Indikator für Wachstum je Einheit.",
    "Gewinn pro Aktie – zentrale Kennzahl für Bewertung & Kursbewegungen.",
    "Operativer Cashflow pro Aktie – misst Cash-Qualität je Aktie.",
    "Free Cash Flow pro Aktie – entscheidend für Dividenden/Rückkäufe.",
    "Cash pro Aktie – Liquidität je Aktie, stark risikoreduzierend.",
    "Buchwert pro Aktie – fundamentaler Bewertungsanker.",
    "Tangible Book Value pro Aktie – Vorsichtiger Vermögensindikator.",
    "Zinsbelastende Schulden pro Aktie – Risikoindikator.",

    "Marktkapitalisierung – Marktwert, stark preisrelevant.",
    "Enterprise Value – Kernmetrik für fundamentale Bewertung.",
    "P/E Ratio – misst Bewertung relativ zum Gewinn.",
    "Preis-Umsatz-Verhältnis – wichtig für Wachstumsfirmen.",
    "Preis/OCF – Bewertung des operativen Cashflows.",
    "Preis/FCF – wichtigste Cashflow-Bewertungskennzahl.",
    "Preis/Buchwert – Value-Indikator.",
    "EV/Sales – kapitalstrukturunabhängige Bewertung.",
    "EV/EBITDA – meistgenutzte Bewertungskennzahl.",

    "Earnings Yield – inverse P/E, direkter Renditeindikator.",
    "Free Cash Flow Yield – bester Value-Indikator für Cash.",
    
    "Debt-to-Equity – Risikoindikator für Leverage.",
    "Debt-to-Assets – zeigt Verschuldungsgrad des Unternehmens.",
    "Net Debt / EBITDA – Standardrisikokennzahl in Finance.",

    "Current Ratio – kurzfristige Zahlungsfähigkeit.",
    "Quick Ratio – strenger Liquiditätsindikator.",
    "Cash Ratio – pure Cash-Liquidität.",

    "Days Sales Outstanding – Effizienz des Forderungsmanagements.",
    "Days Payables Outstanding – Finanzierungsstruktur im Working Capital.",
    "Days of Inventory on Hand – Effizienz in der Lagerverwaltung.",

    "Receivables Turnover – Umschlagshäufigkeit der Forderungen.",
    "Payables Turnover – Umschlag der Verbindlichkeiten.",
    "Inventory Turnover – Effizienz der Warenrotation.",

    "Return on Assets – Effizienz der Vermögensnutzung.",
    "Return on Equity – Profitabilität pro Eigenkapital.",
    "Return on Capital Employed – operative Effizienz des Kapitals.",

    "Operating Cash Flow / Sales Ratio – Cash-basiertes Effizienzmaß.",
    "Free Cash Flow / Operating Cash Flow – Qualitätsindikator.",

    "Preis/Free Cash Flow – Cashflow-Bewertung.",
    "Preis/Operating Cash Flow – Cashflow-basierte Bewertung.",
    "Enterprise Value Multiple – Bewertung vs. Cashflows.",
        "Wie gut das Unternehmen seine Zinsen mit EBIT decken kann – hoher Wert = geringes Risiko.",
    "Vergleicht Cashflow vs. Gewinn – zeigt, ob die Gewinne 'echt' oder buchhalterisch sind.",
    "Wertsteigerung durch Dividenden; wirkt oft als Kursunterstützung.",
    "Wie viel des Gewinns als Dividende ausgeschüttet wird – Indikator für Nachhaltigkeit.",
    "R&D-Intensität – zentraler Treiber zukünftigen Wachstums (v.a. bei Apple).",
    "Wie viel des operativen Cashflows in Investitionen fließt – wichtiger Kapitalindikator.",
    "Investitionsintensität relativ zum Umsatz – Frühindikator für Expansion.",
    "Vergleich CAPEX vs Abschreibungen → Investitionszyklus.",
    "Dilution durch Aktienkompensation – oft stark kurswirksam in Tech.",
    "Return on invested capital – wichtigste Kennzahl für Kapitalrendite, extrem relevant für Marktpreise.",
    "Wie effizient das Unternehmen reale Assets nutzt.",
    "Kurzfristige Liquidität – negative Werte können Risiken anzeigen.",
    "Wert der materiellen Vermögenswerte – unterstützend für fundamentale Bewertung.",
    "NCAV – klassischer Value-Faktor.",
    "Gesamtes eingesetztes Kapital – Grundlage für ROIC.",
    "Effizienz der gesamten Asset-Nutzung – wichtig bei niedrigen Margen.",
    "Wie effizient Anlagen genutzt werden.",
    "Kernprofitabilität – stärker als Brutto oder Netto für einige Modelle.",
    "Profitabilität vor Steuern – hilft Vergleiche zu normalisieren.",
    "Nettoeffizienz – ein Klassiker für Value/Growth Bewertung.",
    "Bruttomarge – Pricing-Power und Kosteneffizienz.",
    "Verschuldungsgrad relativ zu Aktiva – Risikoindikator.",
    "Kapitalstruktur – Anteil der Finanzierung über Schulden.",
    "Wie schnell ein Unternehmen Cash generiert – extrem prognoserelevant.",
    "Dauer vom Einkauf bis zum Umsatz – Indikator für Effizienz.",
]


tickers_list_new_for_ml = [
    "A", "AAL", "AAP", "AAPL", "ABA", "ABBV", "ABI", "ABMD", "ABNB", "ABS",
    "ABT", "ABX", "ACAS", "ACF", "ACGL", "ACN", "ACS", "ACV", "ACY", "AD",
    "ADBE", "ADCT", "ADI", "ADL", "ADM", "ADP", "ADS", "ADSK", "ADT", "AEE",
    "AEP", "AES", "AET", "AFL", "AFS-A", "AGC", "AGM", "AGN", "AH", "AHM",
    "AHS", "AIG", "AIN", "AIT", "AIV", "AIZ", "AJG", "AKAM", "AKS", "ALB",
    "ALGN", "ALK", "ALL", "ALLE", "ALS", "ALTR", "ALXN", "AM", "AMAT", "AMBC",
    "AMCR", "AMD", "AME", "AMG", "AMGN", "AMH", "AMI", "AMO", "AMP", "AMT",
    "AMTM", "AMZN", "AN", "ANDV", "ANDW", "ANET", "ANF", "ANR", "ANSS", "AON",
    "AOS", "APA", "APC", "APCC", "APD", "APH", "APO", "APOL", "APP", "APTV",
    "ARC", "ARE", "ARG", "ASC", "ASH", "ASN", "ASND", "ASO", "ASR", "AST",
    "AT", "ATGE", "ATI", "ATO", "ATVI", "AV", "AVB", "AVGO", "AVY", "AW",
    "AWE", "AWK", "AXON", "AXP", "AYE", "AYI", "AZA-A", "AZO", "BA", "BAC",
    "BALL", "BAW", "BAX", "BAY", "BBBY", "BBI", "BBL", "BBWI", "BBY", "BC",
    "BCR", "BCW", "BDK", "BDX", "BEAM", "BEC", "BEL", "BEN", "BEV", "BF-B",
    "BFI", "BFO", "BG", "BGEN", "BHF", "BIG", "BIIB", "BIO", "BJS", "BK",
    "BKB", "BKI", "BKNG", "BKR", "BLDR", "BLK", "BLS", "BLY", "BMC", "BMET",
    "BMGCA", "BMS", "BMY", "BNI", "BNL", "BOAT", "BOL", "BR", "BRCM", "BRK",
    "BRK-B", "BRL", "BRNO", "BRO", "BS", "BSC", "BSET", "BSX", "BT", "BTU",
    "BU", "BUD", "BUR", "BV", "BVSN", "BWA", "BWY", "BX", "BXLT", "BXP",
    "BYK", "C", "CA", "CAG", "CAH", "CAM", "CAR", "CARR", "CAT", "CB",
    "CBB", "CBE", "CBH", "CBK", "CBL", "CBOE", "CBRE", "CBSS", "CC", "CCE",
    "CCI", "CCK", "CCL", "CCN", "CDNS", "CDW", "CE", "CEG", "CELG", "CEM",
    "CEPH", "CERN", "CF", "CFC", "CFG", "CFL", "CFN", "CGG", "CGM", "CGN",
    "CGP", "CH", "CHA", "CHD", "CHG", "CHI", "CHIR", "CHK", "CHRS", "CHRW",
    "CHTR", "CHU", "CI", "CIC", "CIEN", "CIN", "CINF", "CIT", "CK", "CKL",
    "CL", "CLF", "CLN", "CLO", "CLU", "CLX", "CMA", "CMB", "CMCSA", "CMCSK",
    "CME", "CMG", "CMI", "CMK", "CMR", "CMS", "CMVT", "CMX", "CNA", "CNC",
    "CNG", "CNO", "CNP", "CNT", "CNW", "CNX", "CNXT", "COC-B", "COE", "COF",
    "COIN", "COL", "COMS", "COO", "COOP", "COP", "COR", "COST", "COT", "COTY",
    "COV", "CPAY", "CPB", "CPGX", "CPN", "CPQ", "CPRI", "CPRT", "CPS", "CPT",
    "CPWR", "CPX", "CR", "CRD", "CRL", "CRM", "CRR", "CRWD", "CS", "CSC",
    "CSCO", "CSE", "CSGP", "CSP", "CSR", "CSRA", "CSX", "CTAS", "CTB", "CTC",
    "CTCO", "CTLT", "CTRA", "CTSH", "CTVA", "CTX", "CTXS", "CUL", "CVA", "CVG",
    "CVH", "CVN", "CVS", "CVX", "CW", "CXO", "CYM", "CYR", "CZ", "CZR",
    "D", "DAL", "DAN", "DASH", "DAY", "DD", "DDOG", "DDS", "DE", "DEC",
    "DECK", "DELL", "DEN", "DF", "DFS", "DG", "DGN", "DGR", "DGX", "DHI",
    "DHR", "DI", "DIGI", "DIS", "DISCK", "DISH", "DJ", "DLR", "DLTR", "DLX",
    "DM", "DMG", "DML", "DNA", "DNB", "DNR", "DO", "DOC", "DOV", "DOW",
    "DPH", "DPL", "DPS", "DPT", "DPZ", "DRE", "DRI", "DTE", "DTV", "DUK",
    "DVA", "DVN", "DWD", "DWDP", "DXC", "DXCM", "DYN", "E", "EA", "EAF",
    "EAL", "EBAY", "EC", "ECH", "ECK", "ECL", "ECO", "ED", "EDS", "EFX",
    "EG", "EHC", "EIX", "EJN", "EL", "ELV", "EMC", "EME", "EMN", "EMR",
    "ENDP", "ENPH", "EOG", "EOP", "EP", "EPAM", "EQ", "EQIX", "EQR", "EQT",
    "ERIE", "ES", "ESM", "ESRX", "ESS", "ESY", "ETFC", "ETN", "ETR", "ETS",
    "ETSY", "EVHC", "EVRG", "EVT", "EVY", "EW", "EXC", "EXE", "EXPD", "EXPE",
    "EXR", "F", "FALB", "FANG", "FAST", "FBF", "FBIN", "FBO", "FCI", "FCN",
    "FCX", "FDC", "FDO", "FDP", "FDS", "FDX", "FE", "FFB", "FFIV", "FFS",
    "FG", "FHI", "FHN", "FHP", "FI", "FICO", "FIN", "FIR", "FIS", "FITB",
    "FJ", "FL", "FLA", "FLC", "FLE", "FLIR", "FLM", "FLR", "FLS", "FMC",
    "FMCC", "FMIF", "FMY", "FN", "FNB", "FNMA", "FO", "FOSL", "FOX", "FOXA",
    "FPA", "FPC", "FRC", "FRO", "FRT", "FRX", "FSH", "FSLB", "FSLR", "FST",
    "FTI", "FTL-A", "FTNT", "FTV", "G", "GAS", "GCO", "GCR", "GD", "GDDY",
    "GDT", "GDV", "GDW", "GE", "GEHC", "GEN", "GENZ", "GEV", "GF", "GFS-A",
    "GGP", "GH", "GHB", "GHC", "GI", "GIDL", "GILD", "GIS", "GL", "GLBC",
    "GLD", "GLK", "GLM", "GLW", "GM", "GMCR", "GME", "GN", "GNN", "GNO",
    "GNRC", "GNT", "GNW", "GOOG", "GOOGL", "GOSHA", "GPC", "GPN", "GPS", "GPU",
    "GR", "GRA", "GRL", "GRMN", "GRN", "GS", "GSX", "GT", "GTW", "GTY",
    "GUX", "GWW", "H", "HAL", "HAR", "HAS", "HBAN", "HBI", "HBL", "HBOC",
    "HCA", "HCBK", "HCR", "HD", "HDLM", "HES", "HFC", "HFS", "HIA", "HIG",
    "HII", "HIR", "HJ", "HLT", "HLY", "HM", "HMA", "HMX", "HNG", "HOB",
    "HOG", "HOI", "HOLX", "HON", "HOOD", "HOT", "HP", "HPE", "HPH", "HPQ",
    "HRB", "HRL", "HSH", "HSIC", "HSP", "HST", "HSY", "HT", "HUBB", "HUM",
    "HW", "HWC", "HWM", "HWR", "HYST", "I", "IAC", "IBKR", "IBM", "IC",
    "ICE", "ID", "IDL", "IDXX", "IEX", "IFC", "IFF", "IGT", "IHRT", "IK",
    "IKN", "ILMN", "IMNX", "IMS", "IMSI", "IN", "INA", "INCY", "INFO", "INGR",
    "INTC", "INTU", "INVH", "IP", "IPG", "IPGP", "IQ", "IQV", "IR", "IRM",
    "ISRG", "IT", "ITT", "ITW", "IVZ", "J", "JAVA", "JBHT", "JBL", "JCI",
    "JCP", "JEF", "JERR", "JH", "JHF", "JJN", "JKHY", "JNJ", "JNPR", "JNS",
    "JNY", "JOS", "JOY", "JP", "JPM", "JWN", "JWP", "K", "KATE", "KBH",
    "KCC", "KDP", "KEY", "KEYS", "KG", "KHC", "KIM", "KKR", "KLAC", "KMB",
    "KMG", "KMI", "KMX", "KO", "KODK", "KOP", "KR", "KRB", "KRI", "KSE",
    "KSS", "KSU", "KTY", "KVUE", "KWP", "KYR", "L", "LCE", "LDG", "LDOS",
    "LEG", "LEHMQ", "LEN", "LG", "LGT", "LH", "LHX", "LI", "LIFE", "LII",
    "LIN", "LINB", "LIT", "LJ", "LKQ", "LKS", "LLL", "LLTC", "LLY", "LM",
    "LMT", "LN", "LNC", "LNT", "LO", "LOR", "LOTS", "LOW", "LPT", "LPX",
    "LRCX", "LSI", "LT", "LTC", "LTV", "LU", "LUB", "LULU", "LUMN", "LUV",
    "LVI", "LVLT", "LVS", "LW", "LXK", "LYB", "LYV", "M", "MA", "MAA",
    "MAC", "MAE", "MAG", "MAI", "MAN", "MAR", "MAS", "MAT", "MB", "MBC",
    "MBI", "MCAWA", "MCD", "MCHP", "MCIC", "MCK", "MCO", "MDLZ", "MDR", "MDT",
    "MEA", "MEDI", "MEE", "MEI", "MEL", "MER", "MERQ", "MET", "META", "MF",
    "MFE", "MGI", "MGM", "MGR", "MHC", "MHK", "MHS", "MI", "MII", "MIL",
    "MIR", "MIS", "MJN", "MKC", "MKG", "MKTX", "ML", "MLM", "MLN", "MMC",
    "MMI", "MML", "MMM", "MNC", "MNK", "MNR", "MNST", "MO", "MOH", "MOLX",
    "MON", "MOP", "MOS", "MPC", "MPH", "MPWR", "MRK", "MRN", "MRNA", "MRO",
    "MS", "MSA", "MSCI", "MSFT", "MSI", "MST", "MTB", "MTCH", "MTD", "MTG",
    "MTI", "MTL", "MTW", "MU", "MUR", "MWI", "MWW", "MXIM", "MXS", "MZ",
    "NAB", "NAC", "NAE", "NAL", "NAVI", "NB", "NBL", "NBR", "NCC", "NCLH",
    "NCR", "NDAQ", "NDSN", "NE", "NEC", "NEE", "NEM", "NES", "NEU", "NFB",
    "NFG", "NFLX", "NFX", "NG", "NGH", "NGX", "NI", "NKE", "NKTR", "NLC",
    "NLSN", "NLT", "NLV", "NOC", "NOV", "NOVL", "NOW", "NOXLB", "NRG", "NRT",
    "NSC", "NSI", "NSM", "NT", "NTAP", "NTRS", "NTY", "NUE", "NVDA", "NVLS",
    "NVR", "NWA", "NWL", "NWP", "NWS", "NWSA", "NWT", "NXPI", "NXTL", "NYN",
    "NYT", "NYX", "O", "OAT", "OC", "ODFL", "ODP", "OGN", "OI", "OKE",
    "OLN", "OM", "OMC", "OMX", "ON", "ONE", "ORCL", "ORLY", "ORX", "OT",
    "OTIS", "OVT", "OXY", "PABT", "PAC", "PALM", "PANW", "PAR", "PARA", "PAYC",
    "PAYX", "PBCT", "PBD", "PBG", "PBI", "PBY", "PC", "PCAR", "PCG", "PCH",
    "PCI", "PCL", "PCLB", "PCP", "PCS", "PD", "PDC", "PDCO", "PDG", "PDI",
    "PDQ", "PEG", "PENN", "PEP", "PET", "PETM", "PFE", "PFG", "PG", "PGN",
    "PGR", "PH", "PHB", "PHL", "PHM", "PIN", "PIZ", "PKG", "PLD", "PLL",
    "PLTR", "PM", "PMCS", "PMI", "PNC", "PNR", "PNU", "PNW", "PODD", "POM",
    "POOL", "PPG", "PPL", "PPW", "PRGO", "PRM", "PRU", "PSA", "PSFT", "PSX",
    "PSY", "PT", "PTC", "PTV", "PU", "PUL", "PVH", "PVN", "PVT", "PWER",
    "PWJ", "PWR", "PXD", "PYPL", "PZE", "Q", "QCOM", "QEP", "QLGC", "QRVO",
    "QTRN", "R", "RAD", "RAI", "RAL", "RAM", "RATL", "RBD", "RBK", "RCA",
    "RCL", "RD", "RDC", "RDMN", "RDS", "REE", "REG", "REGN", "REN", "RF",
    "RGI", "RHI", "RHT", "RIG", "RJF", "RL", "RLGY", "RLM", "RM", "RMD",
    "RMG", "RML", "RNB", "ROH", "ROK", "ROL", "ROP", "ROST", "RRC", "RRD",
    "RS", "RSG", "RSH", "RTN", "RTX", "RVB", "RVS", "RVTY", "RYAN", "RYC",
    "RYN", "S", "SA", "SAA", "SAF", "SAI", "SANM", "SAPE", "SB", "SBAC",
    "SBL", "SBNY", "SBUX", "SCG", "SCHW", "SCI", "SCO", "SCV", "SDS", "SE",
    "SEBL", "SED", "SEDG", "SEE", "SEG", "SFA", "SFR", "SFS", "SFX", "SGI",
    "SGL", "SGN", "SHLD", "SHN", "SHW", "SIAL", "SIG", "SIH", "SII", "SITC",
    "SIVB", "SJM", "SK", "SKB", "SKY", "SLB", "SLG", "SLM", "SLR", "SMB",
    "SMCI", "SMS", "SNA", "SNC", "SNDK", "SNI", "SNPS", "SNV", "SO", "SOLSV",
    "SOLV", "SOO", "SOTR", "SOV", "SPC", "SPG", "SPGI", "SPLS", "SPP", "SPXC",
    "SQB", "SQD", "SR", "SRCL", "SRD", "SRE", "SRR", "SRT", "SSP", "STE",
    "STF", "STI", "STJ", "STK", "STLD", "STO", "STR", "STT", "STX", "STY",
    "STZ", "SUB", "SUNEQ", "SUO", "SVU", "SW", "SWK", "SWKS", "SWN", "SWY",
    "SX", "SXCL", "SYF", "SYK", "SYN", "SYY", "T", "TA", "TAP", "TAP-B",
    "TCB", "TCOMA", "TDC", "TDG", "TDM", "TDY", "TE", "TECH", "TEG", "TEL",
    "TEN", "TER", "TEX", "TF", "TFC", "TFD", "TFX", "TG", "TGNA", "TGR",
    "TGT", "THC", "THY", "TIC", "TIE", "TIF", "TIN", "TIS", "TJX", "TKA",
    "TKO", "TLAB", "TMO", "TMUS", "TNB", "TOS", "TOY", "TPL", "TPR", "TRCO",
    "TRGP", "TRIP", "TRMB", "TROW", "TRR", "TRV", "TSCO", "TSG", "TSLA",
    "TSN", "TSS", "TT", "TTD", "TTWO", "TUP", "TWC", "TWTR", "TWX", "TXN",
    "TXO", "TXT", "TYL", "TYM", "U", "UA", "UAL", "UBER", "UC", "UCT",
    "UDR", "UH", "UHS", "UIS", "ULTA", "UMG", "UNH", "UNM", "UNP", "UPJ",
    "UPR", "UPS", "URB", "URBN", "URI", "USB", "USBC", "USH", "USHC", "USS",
    "UST", "USW", "UVN", "V", "VAL", "VAR", "VC", "VFC", "VIAB", "VIAV",
    "VICI", "VLO", "VLTO", "VMC", "VNO", "VNT", "VRSK", "VRSN", "VRTS",
    "VRTX", "VST", "VTR", "VTRS", "VTSS", "VZ", "WAB", "WAI", "WANG", "WAT",
    "WB", "WBA", "WBD", "WCG", "WCI", "WCOM", "WDAY", "WDC", "WEC", "WELL",
    "WEN", "WETT", "WFC", "WFI", "WFM", "WFT", "WH", "WIN", "WLB", "WLL",
    "WLP", "WM", "WMB", "WMT", "WMX", "WOR", "WPM", "WPX", "WRB", "WRC",
    "WSM", "WSN", "WST", "WSW", "WTW", "WU", "WWY", "WY", "WYND", "WYNN",
    "X", "XEC", "XEL", "XL", "XLNX", "XOM", "XRAY", "XTO", "XYL", "XYZ",
    "YHOO", "YNR", "YRCW", "YUM", "ZB", "ZBH", "ZBRA", "ZION", "ZRN", "ZTS"
]

last_dats = [
    "FCX", "FDC", "FDO", "FDP", "FDS", "FDX", "FE", "FFB", "FFIV", "FFS",
    "FG", "FHI", "FHN", "FHP", "FI", "FICO", "FIN", "FIR", "FIS", "FITB",
    "FJ", "FL", "FLA", "FLC", "FLE", "FLIR", "FLM", "FLR", "FLS", "FMC",
    "FMCC", "FMIF", "FMY", "FN", "FNB", "FNMA", "FO", "FOSL", "FOX", "FOXA",
    "FPA", "FPC", "FRC", "FRO", "FRT", "FRX", "FSH", "FSLB", "FSLR", "FST",
    "FTI", "FTL-A", "FTNT", "FTV", "G", "GAS", "GCO", "GCR", "GD", "GDDY",
    "GDT", "GDV", "GDW", "GE", "GEHC", "GEN", "GENZ", "GEV", "GF", "GFS-A",
    "GGP", "GH", "GHB", "GHC", "GI", "GIDL", "GILD", "GIS", "GL", "GLBC",
    "GLD", "GLK", "GLM", "GLW", "GM", "GMCR", "GME", "GN", "GNN", "GNO",
    "GNRC", "GNT", "GNW", "GOOG", "GOOGL", "GOSHA", "GPC", "GPN", "GPS", "GPU",
    "GR", "GRA", "GRL", "GRMN", "GRN", "GS", "GSX", "GT", "GTW", "GTY",
    "GUX", "GWW", "H", "HAL", "HAR", "HAS", "HBAN", "HBI", "HBL", "HBOC",
    "HCA", "HCBK", "HCR", "HD", "HDLM", "HES", "HFC", "HFS", "HIA", "HIG",
    "HII", "HIR", "HJ", "HLT", "HLY", "HM", "HMA", "HMX", "HNG", "HOB",
    "HOG", "HOI", "HOLX", "HON", "HOOD", "HOT", "HP", "HPE", "HPH", "HPQ",
    "HRB", "HRL", "HSH", "HSIC", "HSP", "HST", "HSY", "HT", "HUBB", "HUM",
    "HW", "HWC", "HWM", "HWR", "HYST", "I", "IAC", "IBKR", "IBM", "IC",
    "ICE", "ID", "IDL", "IDXX", "IEX", "IFC", "IFF", "IGT", "IHRT", "IK",
    "IKN", "ILMN", "IMNX", "IMS", "IMSI", "IN", "INA", "INCY", "INFO", "INGR",
    "INTC", "INTU", "INVH", "IP", "IPG", "IPGP", "IQ", "IQV", "IR", "IRM",
    "ISRG", "IT", "ITT", "ITW", "IVZ", "J", "JAVA", "JBHT", "JBL", "JCI",
    "JCP", "JEF", "JERR", "JH", "JHF", "JJN", "JKHY", "JNJ", "JNPR", "JNS",
    "JNY", "JOS", "JOY", "JP", "JPM", "JWN", "JWP", "K", "KATE", "KBH",
    "KCC", "KDP", "KEY", "KEYS", "KG", "KHC", "KIM", "KKR", "KLAC", "KMB",
    "KMG", "KMI", "KMX", "KO", "KODK", "KOP", "KR", "KRB", "KRI", "KSE",
    "KSS", "KSU", "KTY", "KVUE", "KWP", "KYR", "L", "LCE", "LDG", "LDOS",
    "LEG", "LEHMQ", "LEN", "LG", "LGT", "LH", "LHX", "LI", "LIFE", "LII",
    "LIN", "LINB", "LIT", "LJ", "LKQ", "LKS", "LLL", "LLTC", "LLY", "LM",
    "LMT", "LN", "LNC", "LNT", "LO", "LOR", "LOTS", "LOW", "LPT", "LPX",
    "LRCX", "LSI", "LT", "LTC", "LTV", "LU", "LUB", "LULU", "LUMN", "LUV",
    "LVI", "LVLT", "LVS", "LW", "LXK", "LYB", "LYV", "M", "MA", "MAA",
    "MAC", "MAE", "MAG", "MAI", "MAN", "MAR", "MAS", "MAT", "MB", "MBC",
    "MBI", "MCAWA", "MCD", "MCHP", "MCIC", "MCK", "MCO", "MDLZ", "MDR", "MDT",
    "MEA", "MEDI", "MEE", "MEI", "MEL", "MER", "MERQ", "MET", "META", "MF",
    "MFE", "MGI", "MGM", "MGR", "MHC", "MHK", "MHS", "MI", "MII", "MIL",
    "MIR", "MIS", "MJN", "MKC", "MKG", "MKTX", "ML", "MLM", "MLN", "MMC",
    "MMI", "MML", "MMM", "MNC", "MNK", "MNR", "MNST", "MO", "MOH", "MOLX",
    "MON", "MOP", "MOS", "MPC", "MPH", "MPWR", "MRK", "MRN", "MRNA", "MRO",
    "MS", "MSA", "MSCI", "MSFT", "MSI", "MST", "MTB", "MTCH", "MTD", "MTG",
    "MTI", "MTL", "MTW", "MU", "MUR", "MWI", "MWW", "MXIM", "MXS", "MZ",
    "NAB", "NAC", "NAE", "NAL", "NAVI", "NB", "NBL", "NBR", "NCC", "NCLH",
    "NCR", "NDAQ", "NDSN", "NE", "NEC", "NEE", "NEM", "NES", "NEU", "NFB",
    "NFG", "NFLX", "NFX", "NG", "NGH", "NGX", "NI", "NKE", "NKTR", "NLC",
    "NLSN", "NLT", "NLV", "NOC", "NOV", "NOVL", "NOW", "NOXLB", "NRG", "NRT",
    "NSC", "NSI", "NSM", "NT", "NTAP", "NTRS", "NTY", "NUE", "NVDA", "NVLS",
    "NVR", "NWA", "NWL", "NWP", "NWS", "NWSA", "NWT", "NXPI", "NXTL", "NYN",
    "NYT", "NYX", "O", "OAT", "OC", "ODFL", "ODP", "OGN", "OI", "OKE",
    "OLN", "OM", "OMC", "OMX", "ON", "ONE", "ORCL", "ORLY", "ORX", "OT",
    "OTIS", "OVT", "OXY", "PABT", "PAC", "PALM", "PANW", "PAR", "PARA", "PAYC",
    "PAYX", "PBCT", "PBD", "PBG", "PBI", "PBY", "PC", "PCAR", "PCG", "PCH",
    "PCI", "PCL", "PCLB", "PCP", "PCS", "PD", "PDC", "PDCO", "PDG", "PDI",
    "PDQ", "PEG", "PENN", "PEP", "PET", "PETM", "PFE", "PFG", "PG", "PGN",
    "PGR", "PH", "PHB", "PHL", "PHM", "PIN", "PIZ", "PKG", "PLD", "PLL",
    "PLTR", "PM", "PMCS", "PMI", "PNC", "PNR", "PNU", "PNW", "PODD", "POM",
    "POOL", "PPG", "PPL", "PPW", "PRGO", "PRM", "PRU", "PSA", "PSFT", "PSX",
    "PSY", "PT", "PTC", "PTV", "PU", "PUL", "PVH", "PVN", "PVT", "PWER",
    "PWJ", "PWR", "PXD", "PYPL", "PZE", "Q", "QCOM", "QEP", "QLGC", "QRVO",
    "QTRN", "R", "RAD", "RAI", "RAL", "RAM", "RATL", "RBD", "RBK", "RCA",
    "RCL", "RD", "RDC", "RDMN", "RDS", "REE", "REG", "REGN", "REN", "RF",
    "RGI", "RHI", "RHT", "RIG", "RJF", "RL", "RLGY", "RLM", "RM", "RMD",
    "RMG", "RML", "RNB", "ROH", "ROK", "ROL", "ROP", "ROST", "RRC", "RRD",
    "RS", "RSG", "RSH", "RTN", "RTX", "RVB", "RVS", "RVTY", "RYAN", "RYC",
    "RYN", "S", "SA", "SAA", "SAF", "SAI", "SANM", "SAPE", "SB", "SBAC",
    "SBL", "SBNY", "SBUX", "SCG", "SCHW", "SCI", "SCO", "SCV", "SDS", "SE",
    "SEBL", "SED", "SEDG", "SEE", "SEG", "SFA", "SFR", "SFS", "SFX", "SGI",
    "SGL", "SGN", "SHLD", "SHN", "SHW", "SIAL", "SIG", "SIH", "SII", "SITC",
    "SIVB", "SJM", "SK", "SKB", "SKY", "SLB", "SLG", "SLM", "SLR", "SMB",
    "SMCI", "SMS", "SNA", "SNC", "SNDK", "SNI", "SNPS", "SNV", "SO", "SOLSV",
    "SOLV", "SOO", "SOTR", "SOV", "SPC", "SPG", "SPGI", "SPLS", "SPP", "SPXC",
    "SQB", "SQD", "SR", "SRCL", "SRD", "SRE", "SRR", "SRT", "SSP", "STE",
    "STF", "STI", "STJ", "STK", "STLD", "STO", "STR", "STT", "STX", "STY",
    "STZ", "SUB", "SUNEQ", "SUO", "SVU", "SW", "SWK", "SWKS", "SWN", "SWY",
    "SX", "SXCL", "SYF", "SYK", "SYN", "SYY", "T", "TA", "TAP", "TAP-B",
    "TCB", "TCOMA", "TDC", "TDG", "TDM", "TDY", "TE", "TECH", "TEG", "TEL",
    "TEN", "TER", "TEX", "TF", "TFC", "TFD", "TFX", "TG", "TGNA", "TGR",
    "TGT", "THC", "THY", "TIC", "TIE", "TIF", "TIN", "TIS", "TJX", "TKA",
    "TKO", "TLAB", "TMO", "TMUS", "TNB", "TOS", "TOY", "TPL", "TPR", "TRCO",
    "TRGP", "TRIP", "TRMB", "TROW", "TRR", "TRV", "TSCO", "TSG", "TSLA",
    "TSN", "TSS", "TT", "TTD", "TTWO", "TUP", "TWC", "TWTR", "TWX", "TXN",
    "TXO", "TXT", "TYL", "TYM", "U", "UA", "UAL", "UBER", "UC", "UCT",
    "UDR", "UH", "UHS", "UIS", "ULTA", "UMG", "UNH", "UNM", "UNP", "UPJ",
    "UPR", "UPS", "URB", "URBN", "URI", "USB", "USBC", "USH", "USHC", "USS",
    "UST", "USW", "UVN", "V", "VAL", "VAR", "VC", "VFC", "VIAB", "VIAV",
    "VICI", "VLO", "VLTO", "VMC", "VNO", "VNT", "VRSK", "VRSN", "VRTS",
    "VRTX", "VST", "VTR", "VTRS", "VTSS", "VZ", "WAB", "WAI", "WANG", "WAT",
    "WB", "WBA", "WBD", "WCG", "WCI", "WCOM", "WDAY", "WDC", "WEC", "WELL",
    "WEN", "WETT", "WFC", "WFI", "WFM", "WFT", "WH", "WIN", "WLB", "WLL",
    "WLP", "WM", "WMB", "WMT", "WMX", "WOR", "WPM", "WPX", "WRB", "WRC",
    "WSM", "WSN", "WST", "WSW", "WTW", "WU", "WWY", "WY", "WYND", "WYNN",
    "X", "XEC", "XEL", "XL", "XLNX", "XOM", "XRAY", "XTO", "XYL", "XYZ",
    "YHOO", "YNR", "YRCW", "YUM", "ZB", "ZBH", "ZBRA", "ZION", "ZRN", "ZTS"
]
