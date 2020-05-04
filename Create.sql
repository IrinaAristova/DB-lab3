CREATE TABLE athlete (
    athlete_name  VARCHAR2(50) NOT NULL,
    gender        VARCHAR2(10),
    country_name  VARCHAR2(50) NOT NULL
);

ALTER TABLE athlete ADD CONSTRAINT athlete_pk PRIMARY KEY ( athlete_name );

CREATE TABLE category (
    sportcategory_category_name  VARCHAR2(50) NOT NULL,
    disciplina_disc_name         VARCHAR2(50) NOT NULL
);

ALTER TABLE category ADD CONSTRAINT category_pk PRIMARY KEY ( sportcategory_category_name,
                                                              disciplina_disc_name );

CREATE TABLE cities (
    city_name             VARCHAR2(50) NOT NULL,
    olimpiada_olimp_year  INTEGER NOT NULL
);

CREATE UNIQUE INDEX cities__idx ON
    cities (
        olimpiada_olimp_year
    ASC );

ALTER TABLE cities ADD CONSTRAINT cities_pk PRIMARY KEY ( city_name );

CREATE TABLE country (
    country_name VARCHAR2(50) NOT NULL
);

ALTER TABLE country ADD CONSTRAINT country_pk PRIMARY KEY ( country_name );

CREATE TABLE disciplina (
    disc_name VARCHAR2(50) NOT NULL
);

ALTER TABLE disciplina ADD CONSTRAINT disciplina_pk PRIMARY KEY ( disc_name );

CREATE TABLE event (
    event_name VARCHAR2(50) NOT NULL
);

ALTER TABLE event ADD CONSTRAINT event_pk PRIMARY KEY ( event_name );

CREATE TABLE grantmedal (
    disciplina_name  VARCHAR2(50) NOT NULL,
    event_name       VARCHAR2(50) NOT NULL,
    athlete_name     VARCHAR2(50) NOT NULL,
    olimpiada_year   INTEGER NOT NULL,
    medal_color      VARCHAR2(15) NOT NULL
);

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_pk PRIMARY KEY ( disciplina_name,
                                               event_name,
                                               athlete_name,
                                               olimpiada_year,
                                               medal_color );

CREATE TABLE medal (
    color VARCHAR2(15) NOT NULL
);

ALTER TABLE medal ADD CONSTRAINT medal_pk PRIMARY KEY ( color );

CREATE TABLE olimpiada (
    olimp_year INTEGER NOT NULL
);

ALTER TABLE olimpiada ADD CONSTRAINT olimpiada_pk PRIMARY KEY ( olimp_year );

CREATE TABLE sportcategory (
    category_name VARCHAR2(50) NOT NULL
);

ALTER TABLE sportcategory ADD CONSTRAINT sportcategory_pk PRIMARY KEY ( category_name );

ALTER TABLE athlete
    ADD CONSTRAINT athlete_country_fk FOREIGN KEY ( country_name )
        REFERENCES country ( country_name );

ALTER TABLE category
    ADD CONSTRAINT category_disciplina_fk FOREIGN KEY ( disciplina_disc_name )
        REFERENCES disciplina ( disc_name );

ALTER TABLE category
    ADD CONSTRAINT category_sportcategory_fk FOREIGN KEY ( sportcategory_category_name )
        REFERENCES sportcategory ( category_name );

ALTER TABLE cities
    ADD CONSTRAINT cities_olimpiada_fk FOREIGN KEY ( olimpiada_olimp_year )
        REFERENCES olimpiada ( olimp_year );

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_athlete_fk FOREIGN KEY ( athlete_name )
        REFERENCES athlete ( athlete_name );

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_disciplina_fk FOREIGN KEY ( disciplina_name )
        REFERENCES disciplina ( disc_name );

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_event_fk FOREIGN KEY ( event_name )
        REFERENCES event ( event_name );

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_medal_fk FOREIGN KEY ( medal_color )
        REFERENCES medal ( color );

ALTER TABLE grantmedal
    ADD CONSTRAINT grantmedal_olimpiada_fk FOREIGN KEY ( olimpiada_year )
        REFERENCES olimpiada ( olimp_year );