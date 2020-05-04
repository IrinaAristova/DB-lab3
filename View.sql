CREATE OR REPLACE VIEW CountryMedals  AS
SELECT
    country.country_name,
    olimpiada.olimp_year,
    medal.color             
FROM
         country
    INNER JOIN athlete ON country.country_name = athlete.country_name
    INNER JOIN grantmedal ON athlete.athlete_name = grantmedal.athlete_name
    INNER JOIN olimpiada ON olimpiada.olimp_year = grantmedal.olimpiada_year
    INNER JOIN medal ON medal.color = grantmedal.medal_color;