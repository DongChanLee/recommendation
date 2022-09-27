CREATE TABLE melon_artists (
	id			text	PRIMARY KEY,
	name        text	not null,
	headtext	text	not null,
	cdate		date	not null,
	mdate		date	not null default now()
);