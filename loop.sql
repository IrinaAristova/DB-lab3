DECLARE
    start_year INT NOT NULL DEFAULT 2012;
    cnt INT NOT NULL DEFAULT 5;
BEGIN

    DELETE FROM Cities WHERE Olimpiada_olimp_year >= start_year;
    DELETE FROM Olimpiada WHERE olimp_year >= start_year;  
    
    FOR i in 1..cnt LOOP
        INSERT INTO Olimpiada (olimp_year) values (start_year + (i-1)*4);
        INSERT INTO Cities (city_name, Olimpiada_olimp_year) values ('city_name' || i, start_year + (i-1)*4);
    END LOOP;
END;
