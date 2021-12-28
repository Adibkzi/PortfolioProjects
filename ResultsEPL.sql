-- how many times does Man city won BY 3 Points in ascending form
select *
from ResultsEPL
where HomeTeam like '%Man City%'
and FTHG > 3
order by Season asc

-- Show how many time G Scott  ref Arsenal Home games 
select Season,DateTime,HomeTeam,FTHG,Referee
from ResultsEPL
where HomeTeam like 'Arsenal' and Referee like '%G Scott%'
order by Season  DESC

-- WRITE HOMETEAM IN UPPERCASE
SELECT UPPER(HOMETEAM) AS HOMETEAM, LOWER(AWAYTEAM) AS awayteam
from ResultsEPL

--- UPDATE A TABLE IN RESULTSEPL TO SHOW WATFORD SEASON FOR 2018-19 
UPDATE ResultsEPL
set HomeTeam = 'Watford FC'
WHERE Season = '2018-19' 
SELECT * FROM ResultsEPL
