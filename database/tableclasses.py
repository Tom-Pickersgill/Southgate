def FPL_data_table():
    return """
    FirstName TEXT,
    Surname TEXT NOT NULL,
    PositionsList TEXT,
    Team TEXT,
    Cost INTEGER,
    PointsLastRound INTEGER,
    TotalPoints INTEGER,
    AveragePoints INTEGER,
    AveragePointsPerDollar INTEGER,
    TotalPointsPerDollar REAL,
    GameweekWeighting REAL,
    TransfersOut INTEGER,
    YellowCards INTEGER,
    GoalsConceded INTEGER,
    GoalsConcededPoints INTEGER,
    Saves INTEGER,
    SavesPoints INTEGER,
    GoalsScored INTEGER,
    GoalsScoredPoints INTEGER,
    ValueSeason REAL,
    TransfersOutRound INTEGER,
    PriceRise INTEGER,
    PriceFallRound INTEGER,
    LastSeasonPoints INTEGER,
    PriceFall INTEGER,
    ValueForm REAL,
    PenaltiesMissed INTEGER,
    Form INTEGER,
    Bonus INTEGER,
    FanRating INTEGER,
    CleanSheets INTEGER,
    CleanSheetPoints INTEGER,
    Assists INTEGER,
    SelectedByPercent REAL,
    TransfersIn INTEGER,
    OwnGoals INTEGER,
    EAIndex INTEGER,
    PenaltiesSaved INTEGER,
    DreamteamCount INTEGER,
    MinutesPlayed INTEGER,
    TransfersInRound INTEGER,
    PriceRiseRound INTEGER,
    RedCards INTEGER,
    BPS INTEGER,
    NextFixture1 INTEGER,
    NextFixture2 TEXT,
    NextFixture3 TEXT,
    NextFixture4 TEXT,
    NextFixture5 TEXT,
    ICTIndex REAL,
    Year INTEGER,
    Week INTEGER,
    Timeline TEXT NOT NULL,
    PRIMARY KEY (FirstName, Surname, Timeline)
    """
    