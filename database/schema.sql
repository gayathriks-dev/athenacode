CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    dob DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE record (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    date DATE NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);
