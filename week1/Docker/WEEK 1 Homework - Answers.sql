Answers - Homework Week1

 Q3.

SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	COUNT(1)
	
FROM yellow_taxi_data t
WHERE CAST(tpep_pickup_datetime AS DATE) = '2021-01-15'
GROUP BY 1
ORDER BY "day" DESC
LIMIT 100;

Q4.

SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	COUNT(1),
	tip_amount	
		
FROM yellow_taxi_data t

GROUP BY 1,3
ORDER BY tip_amount DESC
LIMIT 100;

Q5.

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

Q6.

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