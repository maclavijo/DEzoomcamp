### Answers - Homework Week1

## Q3.Count records - Answer: 53024
# How many taxi trips were there on January 15?
SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	COUNT(1)
	
FROM yellow_taxi_data t

WHERE CAST(tpep_pickup_datetime AS DATE) = '2021-01-15'

GROUP BY 1

ORDER BY "day" DESC

LIMIT 100;

![Answer Q3](/week1/Docker/Week1_Homework_Images/Week1-Q3.JPG)

## Q4. Largest tip for each day - Answer: 2021-01-20
# On which day it was the largest tip in January? (note: it's not a typo, it's "tip", not "trip")

SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	
	COUNT(1),
	
	tip_amount	
	
	
FROM yellow_taxi_data t

GROUP BY 1,3

ORDER BY tip_amount DESC

LIMIT 100;

![Answer Q4](/week1/Docker/Week1_Homework_Images/Week1-Q4.JPG)

## Q5. Most popular destination - Answer: Upper East Side South
# What was the most popular destination for passengers picked up in central park on January 14? Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown"


SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	
	"DOLocationID",
	
	COUNT(1) as "count",
	
	CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
	
	CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_location"
	
	
FROM yellow_taxi_data t 

	JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
	
	JOIN zones zdo ON t."DOLocationID" = zdo."LocationID"


WHERE "PULocationID" = 43 AND

		CAST(tpep_pickup_datetime AS DATE) = '2021-01-14'


GROUP BY 1,2,4,5

ORDER BY "count" DESC

LIMIT 100;

![Answer Q5](/week1/Docker/Week1_Homework_Images/Week1-Q5.JPG)

## Q6.Most expensive route - Answer: Alphabet City/Unknown
# What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)? Enter two zone names separated by a slashFor example:"Jamaica Bay / Clinton East"If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".

SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	
	"DOLocationID",
	
	AVG(total_amount) as "avg",
	
	CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
	
	CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_location"
	
	
FROM yellow_taxi_data t 

	JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
	
	JOIN zones zdo ON t."DOLocationID" = zdo."LocationID"
	

GROUP BY 1,2,4,5

ORDER BY "avg" DESC

LIMIT 100;

![Answer Q6](/week1/Docker/Week1_Homework_Images/Week1-Q6.JPG)
