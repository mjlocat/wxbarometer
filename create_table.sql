CREATE TABLE pressure (
  id BIGINT NOT NULL AUTO_INCREMENT,
  pressure FLOAT NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);
