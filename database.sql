--- db is named 'picklogger'

CREATE TABLE "brands" (
	"id" SERIAL PRIMARY KEY,
	"brand" VARCHAR(30) NOT NULL,
	"img_url" VARCHAR(255) NOT NULL
);

INSERT INTO "brands" ("brand", "img_url")
VALUES ('Abus', '../../images/Abus_Lock.jpg'), ('American', '../../images/American_Lock.jpg'), ('Brinks', '../../images/Brinks_Lock.jpg'), ('Commando', '../../images/Commando_Lock.jpg'), ('Kwikset', '../../images/Kwikset_Lock.jpg'), ('Master', '../../images/Master_Lock.jpg'), ('Sargent', '../../images/Sarget_Lock.jpg'), ('Schlage', '../../images/Schlage_Lock.jpg'), ('Tru-Bolt', '../../images/Tru-Bolt_Lock.jpg'), ('Weiser', '../../images/Weiser_Lock.jpg'), ('Yale', '../../images/Yale_Lock.jpg'), ('Other', '../../images/Other_Lock.jpg'), ('Unknown', '../../images/Other_Lock.jpg');