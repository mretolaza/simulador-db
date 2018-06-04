SELECT MAX("TrackId") + 1 FROM "Track";

SELECT MAX("AlbumId") + 1 FROM "Album";

SELECT MAX("InvoiceId") + 1 FROM "Invoice";

SELECT MAX("PlaylistId") + 1 FROM "Playlist";

SELECT MAX("CustomerId") + 1 FROM "Customer";

SELECT MAX("GenreId") + 1 FROM "Genre";

SELECT MAX("ArtistId") + 1 FROM "Artist";

SELECT MAX("InvoiceLineId") + 1 FROM "InvoiceLine";


CREATE SEQUENCE album_id_seq START WITH 348;
ALTER TABLE "Album" ALTER COLUMN "AlbumId"  SET DEFAULT nextval('album_id_seq');

CREATE SEQUENCE track_id_seq START WITH replace_track_id;
ALTER TABLE "Track" ALTER COLUMN "TrackId"  SET DEFAULT nextval('track_id_seq');

CREATE SEQUENCE invoice_id_seq START WITH 413;
ALTER TABLE "Invoice" ALTER COLUMN "InvoiceId"  SET DEFAULT nextval('invoice_id_seq');

CREATE SEQUENCE playlist_id_seq START WITH 19;
ALTER TABLE "Playlist" ALTER COLUMN "PlaylistId"  SET DEFAULT nextval('playlist_id_seq');

CREATE SEQUENCE customer_id_seq START WITH 60;
ALTER TABLE "Customer" ALTER COLUMN "CustomerId"  SET DEFAULT nextval('customer_id_seq');

CREATE SEQUENCE genre_id_seq START WITH 26;
ALTER TABLE "Genre" ALTER COLUMN "GenreId"  SET DEFAULT nextval('genre_id_seq');

CREATE SEQUENCE artist_id_seq START WITH 276;
ALTER TABLE "Artist" ALTER COLUMN "ArtistId"  SET DEFAULT nextval('artist_id_seq');

CREATE SEQUENCE invoice_line_id_seq START WITH 2241;
ALTER TABLE "InvoiceLine" ALTER COLUMN "InvoiceLineId"  SET DEFAULT nextval('invoice_line_id_seq');