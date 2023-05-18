
CREATE TABLE if not exists animals (
    id serial primary key,
    fact text,
    animal text,

    UNIQUE(fact, animal)
);


INSERT INTO animals (fact, animal) SELECT fact, 'bird' as animal FROM birds;

INSERT INTO animals (fact, animal) SELECT fact, 'cat' as animal FROM cats;

INSERT INTO animals (fact, animal) SELECT fact, 'dog' as animal FROM dogs;

INSERT INTO animals (fact, animal) SELECT fact, 'fox' as animal FROM foxes;

INSERT INTO animals (fact, animal) SELECT fact, 'kangaroo' as animal FROM kangaroos;
