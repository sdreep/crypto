SELECT
    to_char(timestmp,'yyyyMMddHH') as hours
FROM
    quotes
GROUP BY 1;

SELECT * from




SELECT
left(replace(replace(timestmp, '-',''), 'T',''), 10) as  hours,
avg(bid) as avgbid

FROM quotes
WHERE instrument= 'EUR_USD'
GRoup by hours, bid
LIMIT 100;

select * from cadjpy
limit 100;


INSERT INTO cadjpy(ntimestp)
VALUES
    (left(replace(replace(ntimestp, '-',''), 'T',''), 10));
SELECT
distinct(left(replace(replace(timestmp, '-',''), 'T',''), 10)) as  hours,
avg(bid) as avgbid
FROM eurusd
GROUP BY hours
limit 1000;


create table eurusd;


--COUNT_QUOTES_BY_INSTRUMENTS-----------------------------------------------


select distinct instrument, count(tick_id) as count
from quotes
group by instrument
order by count
desc
;

--CREATE_TABLE_FOR_INSTRUMENT-----------------------------------------------
----------------------------------------------------------------------------
drop table eurusd;

CREATE TABLE eurusd(
    tick_id     bigint PRIMARY KEY,
    time        text NOT NULL,
    bid         numeric NOT NULL,
    ask         numeric NOT NULL
);

--hour-aggregation----------------------------------
CREATE TABLE eurusd_HOUR(
    time        text NOT NULL PRIMARY KEY,
    bid         numeric NOT NULL,
    ask         numeric NOT NULL
);




--INSERT_INTO_TABLE_FOR_INSTRUMENT------------------------------------------
----------------------------------------------------------------------------
INSERT INTO eurusd(tick_id, time, bid, ask)
SELECT
tick_id,
left(replace(replace(timestmp, '-',''), 'T',''), 10) as  hours,
bid,
ask
FROM quotes
WHERE instrument= 'EUR_USD';

--hour_aggregation-------------------------------------------

drop table eurusd_HOUR;

INSERT INTO eurusd_HOUR(time, bid, ask)
select distinct on (time) time, bid, ask from eurusd
group by 1, time, bid, ask;


--AVERAGE_HOUR_BID-------------------------------------------
----------------------------------------------------------------------------
select distinct on (time) time, bid, ask from eurusd
group by 1, time, bid, ask
limit 1000;

----------------------------------------------------------------------------
----------------------------------------------------------------------------


SELECT *
   FROM   dblink('dbname=ttrss','SELECT content FROM ttrss_entries')



select count(distinct(time)) from eurusd_HOUR;

select time, bid, ask
from eurusd
group by tick_id, bid
;


VALUES ('tick_id', left(replace(replace(timestmp, '-',''), 'T',''), 10), 'bid', 'ask')
FROM quotes WHERE instrument= 'EUR_USD'
);

SELECT
tick_id,
left(replace(replace(timestmp, '-',''), 'T',''), 10) as  hours,
bid,
ask
FROM quotes
WHERE instrument= 'EUR_USD'
;

SELECT hours, avgbid FROM
(SELECT
left(replace(replace(timestmp, '-',''), 'T',''), 10) as  hours,
avg(bid) as avgbid
FROM quotes
WHERE instrument= 'EUR_USD'
GRoup by hours, bid
LIMIT 100)
AS EURUSD
Group by EURUSD, hours, avgbid
limit 100
;



SELECT
instrument,
left(replace(replace(timestmp, '-',''), 'T',''), 10) as  hours,
avg(bid)
FROM quotes
GRoup by instrument, timestmp
ORDER BY hours
DESC
LIMIT 100;



replace(replace(timestmp, '-',''), 'T','')

left(timestmp, 2)

replace(timestmp, 'T','')
convert string to time stamp

SELECT
regexp_replace(timestmp,'[^a-zA-Z0-9]', ' ', 'g'), timestmp
FROM quotes;

regexp_replace(lower(trim(both from timestmp)), '[^0-9]', '', 'g')

to_date(timestmp, yyyyMMddHH)


date_part('hour', timestamp 'timestmp')