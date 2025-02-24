--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8 (Homebrew)
-- Dumped by pg_dump version 15.8 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: additionalimage; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.additionalimage (
    artwork_id integer NOT NULL,
    image_url character varying NOT NULL
);


ALTER TABLE public.additionalimage OWNER TO nickgolebiewski;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO nickgolebiewski;

--
-- Name: artist; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.artist (
    id integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    artist_name character varying,
    short_bio character varying(200) NOT NULL,
    long_bio character varying,
    image_url character varying,
    birth_country character varying,
    birth_year integer,
    death_year integer
);


ALTER TABLE public.artist OWNER TO nickgolebiewski;

--
-- Name: artist_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.artist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.artist_id_seq OWNER TO nickgolebiewski;

--
-- Name: artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.artist_id_seq OWNED BY public.artist.id;


--
-- Name: artwork; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.artwork (
    id integer NOT NULL,
    artist_id integer NOT NULL,
    title character varying NOT NULL,
    size character varying NOT NULL,
    year integer,
    end_year integer,
    image_url character varying,
    hi_res_url character varying,
    description character varying,
    keywords character varying,
    department_id integer,
    series_id integer,
    date_added character varying,
    price double precision,
    sold boolean NOT NULL
);


ALTER TABLE public.artwork OWNER TO nickgolebiewski;

--
-- Name: artwork_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.artwork_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.artwork_id_seq OWNER TO nickgolebiewski;

--
-- Name: artwork_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.artwork_id_seq OWNED BY public.artwork.id;


--
-- Name: artworks_mediums; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.artworks_mediums (
    artwork_id integer NOT NULL,
    medium_id integer NOT NULL
);


ALTER TABLE public.artworks_mediums OWNER TO nickgolebiewski;

--
-- Name: artworksmediumslink; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.artworksmediumslink (
    artwork_id integer NOT NULL,
    medium_id integer NOT NULL
);


ALTER TABLE public.artworksmediumslink OWNER TO nickgolebiewski;

--
-- Name: department; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.department (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying(300),
    web boolean,
    "order" integer
);


ALTER TABLE public.department OWNER TO nickgolebiewski;

--
-- Name: department_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.department_id_seq OWNER TO nickgolebiewski;

--
-- Name: department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.department_id_seq OWNED BY public.department.id;


--
-- Name: medium; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.medium (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.medium OWNER TO nickgolebiewski;

--
-- Name: medium_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.medium_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medium_id_seq OWNER TO nickgolebiewski;

--
-- Name: medium_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.medium_id_seq OWNED BY public.medium.id;


--
-- Name: organization; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.organization (
    id integer NOT NULL,
    name character varying NOT NULL,
    address_1 character varying,
    address_2 character varying,
    city character varying NOT NULL,
    state character varying NOT NULL,
    country character varying,
    phone character varying,
    email character varying,
    type character varying NOT NULL
);


ALTER TABLE public.organization OWNER TO nickgolebiewski;

--
-- Name: organization_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organization_id_seq OWNER TO nickgolebiewski;

--
-- Name: organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.organization_id_seq OWNED BY public.organization.id;


--
-- Name: person; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.person (
    id integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    email character varying,
    phone integer,
    org_id integer,
    note character varying,
    type character varying NOT NULL
);


ALTER TABLE public.person OWNER TO nickgolebiewski;

--
-- Name: person_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.person_id_seq OWNER TO nickgolebiewski;

--
-- Name: person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.person_id_seq OWNED BY public.person.id;


--
-- Name: series; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.series (
    id integer NOT NULL,
    artist_id integer NOT NULL,
    name character varying NOT NULL,
    description character varying(300),
    web boolean,
    "order" integer
);


ALTER TABLE public.series OWNER TO nickgolebiewski;

--
-- Name: series_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.series_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.series_id_seq OWNER TO nickgolebiewski;

--
-- Name: series_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.series_id_seq OWNED BY public.series.id;


--
-- Name: soldartwork; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public.soldartwork (
    id integer NOT NULL,
    artwork_id integer NOT NULL,
    person_id integer NOT NULL,
    org_id integer,
    price double precision,
    date_sold character varying,
    "timestamp" character varying
);


ALTER TABLE public.soldartwork OWNER TO nickgolebiewski;

--
-- Name: soldartwork_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.soldartwork_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.soldartwork_id_seq OWNER TO nickgolebiewski;

--
-- Name: soldartwork_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.soldartwork_id_seq OWNED BY public.soldartwork.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: nickgolebiewski
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    email character varying NOT NULL,
    admin boolean
);


ALTER TABLE public."user" OWNER TO nickgolebiewski;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: nickgolebiewski
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO nickgolebiewski;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nickgolebiewski
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: artist id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artist ALTER COLUMN id SET DEFAULT nextval('public.artist_id_seq'::regclass);


--
-- Name: artwork id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artwork ALTER COLUMN id SET DEFAULT nextval('public.artwork_id_seq'::regclass);


--
-- Name: department id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.department ALTER COLUMN id SET DEFAULT nextval('public.department_id_seq'::regclass);


--
-- Name: medium id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.medium ALTER COLUMN id SET DEFAULT nextval('public.medium_id_seq'::regclass);


--
-- Name: organization id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.organization ALTER COLUMN id SET DEFAULT nextval('public.organization_id_seq'::regclass);


--
-- Name: person id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.person ALTER COLUMN id SET DEFAULT nextval('public.person_id_seq'::regclass);


--
-- Name: series id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.series ALTER COLUMN id SET DEFAULT nextval('public.series_id_seq'::regclass);


--
-- Name: soldartwork id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.soldartwork ALTER COLUMN id SET DEFAULT nextval('public.soldartwork_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: additionalimage; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.additionalimage (artwork_id, image_url) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.alembic_version (version_num) FROM stdin;
3d9aaae0c87b
\.


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.artist (id, first_name, last_name, artist_name, short_bio, long_bio, image_url, birth_country, birth_year, death_year) FROM stdin;
\.


--
-- Data for Name: artwork; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.artwork (id, artist_id, title, size, year, end_year, image_url, hi_res_url, description, keywords, department_id, series_id, date_added, price, sold) FROM stdin;
\.


--
-- Data for Name: artworks_mediums; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.artworks_mediums (artwork_id, medium_id) FROM stdin;
\.


--
-- Data for Name: artworksmediumslink; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.artworksmediumslink (artwork_id, medium_id) FROM stdin;
\.


--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.department (id, name, description, web, "order") FROM stdin;
\.


--
-- Data for Name: medium; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.medium (id, name) FROM stdin;
\.


--
-- Data for Name: organization; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.organization (id, name, address_1, address_2, city, state, country, phone, email, type) FROM stdin;
\.


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.person (id, first_name, last_name, email, phone, org_id, note, type) FROM stdin;
\.


--
-- Data for Name: series; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.series (id, artist_id, name, description, web, "order") FROM stdin;
\.


--
-- Data for Name: soldartwork; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public.soldartwork (id, artwork_id, person_id, org_id, price, date_sold, "timestamp") FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: nickgolebiewski
--

COPY public."user" (id, username, password, email, admin) FROM stdin;
\.


--
-- Name: artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.artist_id_seq', 1, false);


--
-- Name: artwork_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.artwork_id_seq', 1, false);


--
-- Name: department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.department_id_seq', 1, false);


--
-- Name: medium_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.medium_id_seq', 1, false);


--
-- Name: organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.organization_id_seq', 1, false);


--
-- Name: person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.person_id_seq', 1, false);


--
-- Name: series_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.series_id_seq', 1, false);


--
-- Name: soldartwork_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.soldartwork_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nickgolebiewski
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


--
-- Name: additionalimage additionalimage_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.additionalimage
    ADD CONSTRAINT additionalimage_pkey PRIMARY KEY (artwork_id, image_url);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: artist artist_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (id);


--
-- Name: artwork artwork_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artwork
    ADD CONSTRAINT artwork_pkey PRIMARY KEY (id);


--
-- Name: artworks_mediums artworks_mediums_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworks_mediums
    ADD CONSTRAINT artworks_mediums_pkey PRIMARY KEY (artwork_id, medium_id);


--
-- Name: artworksmediumslink artworksmediumslink_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworksmediumslink
    ADD CONSTRAINT artworksmediumslink_pkey PRIMARY KEY (artwork_id, medium_id);


--
-- Name: department department_name_key; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_name_key UNIQUE (name);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id);


--
-- Name: medium medium_name_key; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.medium
    ADD CONSTRAINT medium_name_key UNIQUE (name);


--
-- Name: medium medium_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.medium
    ADD CONSTRAINT medium_pkey PRIMARY KEY (id);


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (id);


--
-- Name: person person_email_key; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_email_key UNIQUE (email);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: series series_name_key; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_name_key UNIQUE (name);


--
-- Name: series series_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_pkey PRIMARY KEY (id);


--
-- Name: soldartwork soldartwork_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.soldartwork
    ADD CONSTRAINT soldartwork_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: additionalimage additionalimage_artwork_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.additionalimage
    ADD CONSTRAINT additionalimage_artwork_id_fkey FOREIGN KEY (artwork_id) REFERENCES public.artwork(id);


--
-- Name: artwork artwork_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artwork
    ADD CONSTRAINT artwork_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(id);


--
-- Name: artwork artwork_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artwork
    ADD CONSTRAINT artwork_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(id);


--
-- Name: artwork artwork_series_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artwork
    ADD CONSTRAINT artwork_series_id_fkey FOREIGN KEY (series_id) REFERENCES public.series(id);


--
-- Name: artworks_mediums artworks_mediums_artwork_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworks_mediums
    ADD CONSTRAINT artworks_mediums_artwork_id_fkey FOREIGN KEY (artwork_id) REFERENCES public.artwork(id);


--
-- Name: artworks_mediums artworks_mediums_medium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworks_mediums
    ADD CONSTRAINT artworks_mediums_medium_id_fkey FOREIGN KEY (medium_id) REFERENCES public.medium(id);


--
-- Name: artworksmediumslink artworksmediumslink_artwork_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworksmediumslink
    ADD CONSTRAINT artworksmediumslink_artwork_id_fkey FOREIGN KEY (artwork_id) REFERENCES public.artwork(id);


--
-- Name: artworksmediumslink artworksmediumslink_medium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.artworksmediumslink
    ADD CONSTRAINT artworksmediumslink_medium_id_fkey FOREIGN KEY (medium_id) REFERENCES public.medium(id);


--
-- Name: person person_org_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_org_id_fkey FOREIGN KEY (org_id) REFERENCES public.organization(id);


--
-- Name: series series_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(id);


--
-- Name: soldartwork soldartwork_artwork_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.soldartwork
    ADD CONSTRAINT soldartwork_artwork_id_fkey FOREIGN KEY (artwork_id) REFERENCES public.artwork(id);


--
-- Name: soldartwork soldartwork_org_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.soldartwork
    ADD CONSTRAINT soldartwork_org_id_fkey FOREIGN KEY (org_id) REFERENCES public.organization(id);


--
-- Name: soldartwork soldartwork_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nickgolebiewski
--

ALTER TABLE ONLY public.soldartwork
    ADD CONSTRAINT soldartwork_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);


--
-- PostgreSQL database dump complete
--

