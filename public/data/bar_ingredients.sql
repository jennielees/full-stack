drop table if exists ingredients;

create table ingredients (
    id int primary_key not null,
    name text not null,
    price int,
    stock int
);

insert into ingredients values
    (1, 'glug of rum', 4, 3),
    (2, 'slug of whisky', 3, 4),
    (3, 'splash of gin', 3, 7),
    (4, 'olive on a stick', 2, 5),
    (5, 'salt-dusted rim', 1, 20),
    (6, 'rasher of bacon', 3, 8);