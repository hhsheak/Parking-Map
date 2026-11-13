CREATE TABLE carpark_information AS
SELECT id, car_park_no, address, x_coord, y_coord
FROM "HDBCarparkInformation";

ALTER TABLE carpark_information
ADD COLUMN geom geometry(Point, 3414);
-- 3414 is the CRS ID for Singapore


UPDATE carpark_information
SET geom = ST_SetSRID(ST_MakePoint(x_coord::double precision, y_coord::double precision), 3414);
