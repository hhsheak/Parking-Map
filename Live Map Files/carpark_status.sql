CREATE TABLE carpark_status (
	lot_type TEXT,
	lots_available INT,
	total_lots INT,
	carpark_number TEXT UNIQUE,
	last_update TIMESTAMP);
