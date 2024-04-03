CREATE TABLE Taxi (
    taxi_id INT PRIMARY KEY,
    pickup_point TEXT DEFAULT '[1]',
    drop_point TEXT DEFAULT '[1]',
    pickup_time TEXT DEFAULT '[1]',
    drop_time TEXT DEFAULT '[1]',
    total_pay INT
);

CREATE TABLE Booking (
    booking_id INT PRIMARY KEY,
    taxi_id INT,
    customer_id VARCHAR(10) DEFAULT '0',
    pickup_point VARCHAR(1) DEFAULT '0',
    drop_point VARCHAR(1) DEFAULT '0',
    pickup_time INT,
    drop_time INT,
    pay INT
);
