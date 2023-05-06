#Creation of tables
CREATE TABLE clients(ID INT PRIMARY KEY AUTO_INCREMENT, 
					 NAME VARCHAR(50) NOT NULL,
                     HOST CHAR(15) NOT NULL,
                     PORT INT NOT NULL
                     );
                     
CREATE TABLE personnel(ID INT PRIMARY KEY AUTO_INCREMENT, 
					 NAME VARCHAR(50) NOT NULL,
					 SURNAME VARCHAR(50) NOT NULL,
                     SSN VARCHAR(15) NOT NULL
                     );
                     
CREATE TABLE messages(ID INT PRIMARY KEY AUTO_INCREMENT, 
					 CLIENT_ID INT NOT NULL,
					 PAYLOAD VARCHAR(50) NOT NULL,
                     FOREIGN KEY (CLIENT_ID) REFERENCES clients(ID)
                     );
                    
#To add data to the table                    
INSERT INTO clients(NAME,HOST,PORT) VALUES ("Client #1"," 127.0.0.1", 5001);	
INSERT INTO clients(NAME,HOST,PORT) VALUES ("Client #2"," 127.0.0.1", 5002);

#The same procedure was applied for the other tables.
INSERT INTO personnel(NAME,SURNAME,SSN) VALUES ("Isaac"," Newton", 12345678900);
INSERT INTO personnel(NAME,SURNAME,SSN) VALUES ("Albert"," Einstein", 98765432100);

