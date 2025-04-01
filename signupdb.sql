create database signupdb;
use signupdb;

select * from society_ppf;


create table society_ppf(
SocietyMembershipID int NOT NULL PRIMARY key auto_increment,
SocietyName varchar (150)
);


create table sign_up_ppf(
MemberID int not null primary key auto_increment,
firstname varchar(100),
lastname varchar(100),
email varchar(100) not null,
SocietyMembershipID int,
foreign key (SocietyMembershipID) references society_ppf(SocietyMembershipID)
);


insert into society_ppf(SocietyName)
values("Eat and Retreat Society"),
("Sci-fi gee Society"),
("The clue seekers Society"),
("Law Society"),
("Foreign Exchange Society")
;

SELECT * FROM society_ppf;

DELIMITER // 
CREATE PROCEDURE AddMember (
    IN firstname varchar(100),
    IN lastname varchar(100),
    IN email varchar(100),
)


-- DELI-- MITER //

-- CREATE PROCEDURE AddMemberBySociety(
--     IN p_fi-- rstname VARCHAR(50),
--     IN p_lastname VARCHAR(50),
--     IN p_email VARCHAR(100),
--     IN p_SocietyName VARCHAR(100)
-- )
-- BEGIN
--     DECLARE v_SocietyMembershipID INT;

--     SELECT id INTO v_SocietyMembershipID FROM society_ppf WHERE name = p_SocietyName LIMIT 1;

--     
--     IF v_SocietyMem-- bershipID IS NULL THEN
--         SIGNAL SQLSTATE '45000'
--         SET MESSAGE_TEXT = 'Error: Society does not exist.';
--     END IF;

--     INSERT INTO sign_up_ppf (firstname, lastname, email, SocietyName)
--     VALUES (p_firstname, p_lastname, p_email, p_SocietyName );

--     SELECT 
--         CONCAT('Success: ', p_firstname, ' ', p_lastname, 
--                ' added to "', p_SocietyName, '" (Society ID: ', v_SocietyMembershipID, ').') 
     --    AS Confirmation;
-- END //

-- DELIMITER ;

-- CALL AddMemberBySociety('Ross', 'Geller', 'ross@gmail.co', 'The Clue Seeker Society');

DELIMITER //

CREATE PROCEDURE AddMemberOfUniSociety(
    IN p_firstname VARCHAR(100),
    IN p_lastname VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_SocietyName VARCHAR(150)
)
BEGIN
    DECLARE v_SocietyMembershipID INT;

    -- Fetch Society ID
    SELECT SocietyMembershipID INTO v_SocietyMembershipID 
    FROM society_ppf 
    WHERE SocietyName = p_SocietyName 
    LIMIT 1;

    -- Check if Society exists
    IF v_SocietyMembershipID IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Society does not exist.';
    END IF;

    -- Insert into sign_up_ppf with the correct Society ID
    INSERT INTO sign_up_ppf (firstname, lastname, email, SocietyMembershipID)
    VALUES (p_firstname, p_lastname, p_email, v_SocietyMembershipID);

    -- Confirmation Message
    SELECT CONCAT(
        'Success: ', p_firstname, ' ', p_lastname, 
        ' added to "', p_SocietyName, 
        '" (Society ID: ', v_SocietyMembershipID, ').'
    ) AS Confirmation;
END //

CALL AddMemberOfUniSociety('Ross', 'Geller', 'gh@hj.com', 'Eat and Retreat Society');