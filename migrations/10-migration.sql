--
-- PostgreSQL database dump
--

-- Dumped from database version 13.9 (Debian 13.9-0+deb11u1)
-- Dumped by pg_dump version 13.9 (Debian 13.9-0+deb11u1)

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
-- Name: birds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.birds (
    id smallint NOT NULL,
    fact text
);

--
-- Name: birds_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.birds_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



--
-- Name: birds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.birds_id_seq OWNED BY public.birds.id;


--
-- Name: cats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cats (
    id smallint NOT NULL,
    fact text
);



--
-- Name: cats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cats_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



--
-- Name: cats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cats_id_seq OWNED BY public.cats.id;


--
-- Name: dogs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dogs (
    id smallint NOT NULL,
    fact text
);



--
-- Name: dogs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dogs_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



--
-- Name: dogs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dogs_id_seq OWNED BY public.dogs.id;


--
-- Name: foxes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foxes (
    id smallint NOT NULL,
    fact text
);



--
-- Name: foxes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foxes_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



--
-- Name: foxes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foxes_id_seq OWNED BY public.foxes.id;


--
-- Name: kangaroos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kangaroos (
    id smallint NOT NULL,
    fact text
);



--
-- Name: kangaroos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kangaroos_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



--
-- Name: kangaroos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kangaroos_id_seq OWNED BY public.kangaroos.id;


--
-- Name: birds id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.birds ALTER COLUMN id SET DEFAULT nextval('public.birds_id_seq'::regclass);


--
-- Name: cats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cats ALTER COLUMN id SET DEFAULT nextval('public.cats_id_seq'::regclass);


--
-- Name: dogs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dogs ALTER COLUMN id SET DEFAULT nextval('public.dogs_id_seq'::regclass);


--
-- Name: foxes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foxes ALTER COLUMN id SET DEFAULT nextval('public.foxes_id_seq'::regclass);


--
-- Name: kangaroos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kangaroos ALTER COLUMN id SET DEFAULT nextval('public.kangaroos_id_seq'::regclass);


--
-- Data for Name: birds; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.birds (id, fact) FROM stdin;
1	Many birds, such as starlings, sing notes too high for humans to hear.
2	Birds don't fall off of a branch when they sleep because their toes automatically clench around the twig they are standing on. Because the grabbing action is done by tendons rather than muscles, the birds can sleep without danger of falling.
3	In the continental U.S. alone, between 1.4 billion and 3.7 billion birds are killed by cats annually.
4	The type of diet a bird eats in the wild is directly related to the shape of a bird's beak.
5	Scientists believe that birds evolved from theropod dinosaurs.
6	More than 150 kinds of birds have become extinct since 1600, though many more may have died out that scientists don't know about. It wasn't just European explorers that killed bird species. Archeology shows that when people first arrived in ancient times in Hawaii and on islands in the South Pacific and Caribbean, they killed many birds Europeans had never seen before.
7	The earliest known bird is the Archaeopteryx. It lived during the Jurassic period 150 million years ago. Because it did not have the basic features of flight, scientists are uncertain if it could fly.
8	The Ostrich is the largest bird in the world. It also lays the largest eggs and has the fastest maximum running speed (97 kph).
9	The biggest bird that ever existed on Earth is the flightless elephant bird, which is now extinct. It weighed about 1000 lb. (450 kg.). Seven ostrich eggs would fit inside one elephant bird's egg. Elephant birds died out 400 years ago, but people still find pieces of their tough-shelled eggs.
10	The unique black and white coloring of penguins works as camouflage.
11	Birds sense winter is coming by 1) changes in hormones that cause them to put on fat, 2) the changing length of the day, and 3) sensing small changes in air pressure, which is important in predicting weather changes.
12	Flamingos pair for a lifetime. Some stay with their mates for 50 years or more.
\.


--
-- Data for Name: cats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cats (id, fact) FROM stdin;
1	When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.
2	Hearing is the strongest of cat's senses: They can hear sounds as high as 64 kHz compared with humans, who can hear only as high as 20 kHz.
3	Cat people are more open to new experiences than typical 'dog people.'
4	Approximately 24 cat skins can make a coat.
5	Cats make about 100 different sounds. Dogs make only about 10.
6	Cats have an extra organ that allows them to taste scents on the air, which is why your cat stares at you with her mouth open from time to time.
7	Evidence suggests domesticated cats have been around since 3600 B.C., 2,000 years before Egypt's pharaohs.
8	Cat owners are 17% more likely to have a graduate degree.
10	A cat called the Turkish Van does not have the fur insulation problem and LOVES water.
11	A cat ran for mayor of Mexico City in 2013.
12	A house cat is faster than Usain Bolt.
13	Among many other diseases, cats can suffer from anorexia, senility, feline AIDS and acne.
14	Calico cats are almost always female.
15	While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.
16	Cats can move their ears 180 degrees.
17	Cats are very soft.
\.


--
-- Data for Name: dogs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dogs (id, fact) FROM stdin;
1	A dog's nose print is unique, much like a person's fingerprint.
2	Rin Tin Tin, the famous German Shepherd, was nominated for an Academy Award.
3	Did you know tripping over your dog is the second most likely way to get injured around hounds? Bites are the most common.
4	In the Harry Potter series, Hagrid's dog, Fang, was a Neapolitan Mastiff- a breed that almost became extinct after WWII.
5	All dogs dream, but puppies and senior dogs dream more frequently than adult dogs.
6	33 percent of dog owners admit to talking to their dog over the telephone, often leaving them messages on the answering machine.
7	Dog body odor is often called 'Frito Feet,' referring to bacteria collected on dogs' paws that often smell like the popular salty snack.
8	Spaying or neutering your dog can help prevent certain types of cancer.
9	The Basenji is not technically 'barkless,' as many people think. They can yodel.
10	Dogs can smell disease.
11	When dogs kick backward after they go to the bathroom it's not to cover it up, but to mark their territory, using the scent glands in their feet.
12	As per the Guinness Book of World Records, the world's smallest dog, a Yorkshire Terrier from Great Britian, weighed a teeny-tiny 4 ounces at age two.
13	Basset Hounds have the longest ears out of any other dog breed. Many measure between 7 and 10 inches long.
14	Human blood pressure goes down when petting a dog. And so does the dog's.
15	A dog's unique smell is secreted in its glands.
16	The seeds of apples and pears should be kept away from dogs. Their composition includes arsenic, which could kill your dog.
17	The idea that a dog's saliva has healing powers has been around at least since the ancient Greeks and Romans, whose physicians believed it to be an antidote for poisoning.
18	According to legend, the dog rescued on Noah's Ark was the Afghan Hound.
19	Dogs and humans have the same type of slow wave sleep (SWS) and rapid eye movement (REM) and during this REM stage dogs can dream. The twitching and paw movements that occur during their sleep are signs that your pet is dreaming
20	Big happy 'helicopter' tail wagging is one sign of a really nice dog
\.


--
-- Data for Name: foxes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.foxes (id, fact) FROM stdin;
1	Grey foxes can retract their claws like cats do.
2	A male is called a 'dog fox' while a female is called a 'vixen'
3	Even if you encounter a wild fox, they probably won't eat you. Their omnivorous diet mainly consists of small rodents, small mammals, vegetation and birds.
4	Speaking of whiskers, they have some on their legs. This helps them with their bearings, especially when it's dark outside.
5	Foxes dig underground dens where they take care of their kits and hide from predators
6	Foxes are generally solitary animals; unlike wolves, they hunt on their own rather than in packs
7	Foxes have whiskers on their legs and face, which help them to navigate
8	Besides whiskers on their legs, foxes also use Earth's magnetic field to hunt their prey. Foxes leap up and pounce on their prey. They can leap in any direction, but they're more likely to jump towards the northeast, where 72 of their attacks were successful.
9	Foxes have excellent hearing. Red foxes can reportedly hear a watch ticking 40 yards away!
10	Some foxes can hear objects that are 40 yards (36.5 meters) away.
11	What does the fox say? There are at least 40 different voices the fox can uses, but the most common is their scream.
12	Most foxes are like medium-sized dogs, with the biggest foxes weighing 24 pounds (11 kilograms) and measuring 34 inches (86 cm) without its tail.
\.


--
-- Data for Name: kangaroos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kangaroos (id, fact) FROM stdin;
3	Like all marsupials, kangaroos are born extremely early; the equivalent of the seventh week of pregnancy for humans. They travel from the birth canal as little more than an embryo by blindly propelling through the mother's fur to the safety of the pouch, where they will spend several months developing before finally leaving to explore the world.
4	On land kangaroos only ever move their hind legs together, however in water they kick each leg independently to swim.
5	There are more kangaroos than humans in Australia. They are the national symbol of Australia and appear on postage stamps, coins, and aeroplanes.
7	In one leap they can jump 3m high and 7.6m long.
8	Kangaroos have very powerful legs and can be dangerous at times.
9	Kangaroos are marsupial animals that are found in Australia as well as New Guinea.
10	There are four different kangaroo species, the red kangaroo, eastern grey kangaroo, western grey kangaroo and antilopine kangaroo.
12	Female kangaroos can determine the gender of their offspring. They can even delay gestation when environmental factors are likely to diminish the chance of young surviving.
\.


--
-- Name: birds_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.birds_id_seq', 33, true);


--
-- Name: cats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cats_id_seq', 17, true);


--
-- Name: dogs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dogs_id_seq', 20, true);


--
-- Name: foxes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foxes_id_seq', 12, true);


--
-- Name: kangaroos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kangaroos_id_seq', 13, true);


--
-- Name: birds birds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.birds
    ADD CONSTRAINT birds_pkey PRIMARY KEY (id);


--
-- Name: cats cats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cats
    ADD CONSTRAINT cats_pkey PRIMARY KEY (id);


--
-- Name: dogs dogs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dogs
    ADD CONSTRAINT dogs_pkey PRIMARY KEY (id);


--
-- Name: foxes foxes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foxes
    ADD CONSTRAINT foxes_pkey PRIMARY KEY (id);


--
-- Name: kangaroos kangaroos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kangaroos
    ADD CONSTRAINT kangaroos_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--
