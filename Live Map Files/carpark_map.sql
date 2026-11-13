CREATE OR REPLACE VIEW carpark_map AS
SELECT ci.car_park_no, ci.address, ci.x_coord, ci.y_coord, ci.geom,
	   cs.lot_type, cs.lots_available, cs.total_lots, cs.last_update,
	   CASE WHEN lots_available = 0 THEN 'None'
			WHEN total_lots - lots_available < 10 THEN '<10'
			WHEN total_lots - lots_available < 50 THEN '<50'
			WHEN total_lots - lots_available < 100 THEN '<100'
			ELSE 'Available'
	   END AS parking_status
FROM carpark_status AS cs
LEFT JOIN carpark_information AS ci
ON cs.carpark_number = ci.car_park_no;