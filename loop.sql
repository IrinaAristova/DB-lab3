DECLARE
    start_year INT NOT NULL DEFAULT 2020;
    cnt INT NOT NULL DEFAULT 5;
BEGIN
 
    FOR i in 1..cnt LOOP
        INSERT INTO Cities (Olimpiada.olimp_year) values (start_year + (i-1)*4);
        INSERT INTO Cities (city_name) values ("city_name" || i, start_year + (i-1)*4);
    END LOOP;
END;
