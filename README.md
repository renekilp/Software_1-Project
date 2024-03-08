LENTOPELIPROJEKTI - METROPOLIAN TIETO- JA VIESTINTÄTEKNIIKAN OHJELMISTO 1-KURSSI

Tämä on Metropolian Tieto- ja Viestintätekniikan Ohjelmisto 1-kurssin lentopeliprojektin repository, joka on toteutettu kurssin loppuprojektina. 
Projektin tarkoituksena oli kehittää yksinkertainen lentopeli, jossa käytetään python ohjelmointikieltä sekä yhdistetään tietokantoja.


-------------------------------------------------------------------------------------------------------------------------------------------------
Toiminta ohjeet pelin ajamiseen (ns. tyhjältä pöydältä)

- Mariadb:n ja HeidiSql:n lataaminen. 
- Luo uusi istunto HeidiSql:ssä. Käytä kohdissa 'Käyttäjä' ja 'Salasana' molemmissa tekstiä 'root'. Sekä aseta kohtaan 'Portti' luku: 3306.
- Alustavasti tarvitaan flight_game tietokanta, jonka luontiskripti löytyy Metropolian Moodlesta. Luontiskripti on lisätty myös tähän repositoryyn (flight_game_luontiskripti.sql)  
- Lataa IDE libraryt; colorama ja art - (esim. terminaalissa aja komennot: pip install colorama, pip install art)
- Aja KYSYMYSTAULUNLUONTI.py tiedosto vain KERRAN, jotta saadaan tarvittava taulu valmiiseen flight_game tietokantaan.
-------------------------------------------------------------------------------------------------------------------------------------------------

