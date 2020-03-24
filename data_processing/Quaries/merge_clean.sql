-- Table: public.merge_clean

-- DROP TABLE public.merge_clean;

CREATE TABLE public.merge_clean
(
    "Unnamed: 0" bigint,
    reportedcity text COLLATE pg_catalog."default",
    dateofloss text COLLATE pg_catalog."default",
    elevationdifference double precision,
    floodzone text COLLATE pg_catalog."default",
    latitude double precision,
    longitude double precision,
    numberoffloorsintheinsuredbuilding double precision,
    occupancytype double precision,
    originalconstructiondate text COLLATE pg_catalog."default",
    amountpaidonbuildingclaim double precision,
    state text COLLATE pg_catalog."default",
    reportedzipcode double precision,
    stns bigint,
    obs double precision,
    pred double precision,
    stn_lat double precision,
    stn_lon double precision,
    new_date_column text COLLATE pg_catalog."default",
    geometry text COLLATE pg_catalog."default",
    rolling_2days_obs double precision,
    rolling_7days_obs double precision
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.merge_clean
    OWNER to postgres;
    
    
--join table
-- SELECT "Unnamed: 0" from merge_clean
SELECT * FROM 
(SELECT "Unnamed: 0", reportedcity FROM merge_clean) as reportedcity
JOIN
(SELECT "Unnamed: 0", dateofloss FROM merge_clean) as dateofloss
ON reportedcity."Unnamed: 0" = dateofloss."Unnamed: 0"
