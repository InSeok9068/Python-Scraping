CREATE TABLE scraping (
	id BIGINT(7) NOT NULL AUTO_INCREMENT, 
	title VARCHAR(200), 
	content VARCHAR(10000),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (id)
	);  

ALTER DATABASE scraping CHARACTER SET = UTF8MB4 COLLATE = UTF8MB4_UNICODE_CI;

ALTER TABLE pages CONVERT TO CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI;

ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI;

ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI;

-- CREATE TABLE 'wikipedia'.'pages' (
-- 	'id' INT NOT NULL AUTO_INCREMENT,
-- 	'url' VARCHAR(255) NOT NULL,
-- 	'created' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- 	PRIMARY KEY ('id')
-- );

-- CREATE TABLE 'wikipedia'.'links'(
-- 	'id' NOT NULL AUTO_INCREMENT,
-- 	'fromPageId' INT NULL,
-- 	'toPageId' INT NULL,
-- 	'created' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- 	PRIMARY KEY ('id')
-- );

CREATE TABLE wikipedia_pages (
	id INT NOT NULL AUTO_INCREMENT,
	url VARCHAR(255) NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE wikipedia_links(
	id INT NOT NULL AUTO_INCREMENT,
	fromPageId INT NULL,
	toPageId INT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
)
