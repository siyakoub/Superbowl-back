use superBowlBdd;
DELIMITER $$
drop trigger if exists before_insert_user;
CREATE TRIGGER before_insert_user
BEFORE INSERT ON Utilisateur
FOR EACH ROW
BEGIN
    DECLARE email_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO email_count FROM Utilisateur WHERE adresseEmail = NEW.adresseEmail;

    IF email_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Adresse e-mail déjà existante';
    END IF;
END$$

DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createUser;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(100),
    IN p_prenom VARCHAR(100),
    IN p_adressEmail VARCHAR(254),  -- Ajout de la virgule ici
    IN p_password VARCHAR(254)
)
BEGIN
    if ( select exists (select 1 from Utilisateur where adresseEmail = p_adressEmail) ) THEN

        select 'Adresse e-mail déjà existante!!';

    ELSE

        insert into Utilisateur
        (
            nom,
            prenom,
            adresseEmail,
            motDePasse,
            dateInscription,
            actif
        )
        values
        (
            p_name,
            p_prenom,
            p_adressEmail,
            p_password,
            now(),
            1
        );

    END IF;
END$$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createAdmin;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createAdmin`(
    IN p_login VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_nom VARCHAR(100),
    IN p_prenom VARCHAR(100)
)
BEGIN
    if ( select exists (select 1 from administrateur where login = p_login) ) THEN

        select 'Administrateur déjà existante!!';

    ELSE

        insert into administrateur
        (
            login,
            pass,
            nom,
            prenom,
            actif
        )
        values
        (
            p_login,
            p_password,
            p_nom,
            p_prenom,
            1
        );

    END IF;
END$$
DELIMITER ;

DELIMITER $$
drop trigger if exists before_insert_admin;
CREATE TRIGGER before_insert_admin
BEFORE INSERT ON Administrateur
FOR EACH ROW
BEGIN
    DECLARE login_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO login_count FROM administrateur WHERE login = NEW.login;

    IF login_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Administrateur déjà existante';
    END IF;
END$$

DELIMITER ;


DELIMITER $$
drop trigger if exists before_insert_equipe;
CREATE TRIGGER before_insert_equipe
BEFORE INSERT ON equipe
FOR EACH ROW
BEGIN
    DECLARE name_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO name_count FROM equipe WHERE nomEquipe = NEW.nomEquipe;

    IF name_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Equipe déjà existante';
    END IF;
END$$

DELIMITER ;


DELIMITER $$
drop procedure if exists sp_createEquipe;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createEquipe`(
    IN p_nomEquipe VARCHAR(100),
    IN p_paysOrigine VARCHAR(50)
)
BEGIN
    if ( select exists (select 1 from equipe where nomEquipe = p_nomEquipe) ) THEN

        select 'Equipe déjà existante!!';

    ELSE

        insert into equipe
        (
            nomEquipe,
            paysOrigine
        )
        values
        (
            p_nomEquipe,
            p_paysOrigine
        );

    END IF;
END$$
DELIMITER ;


DELIMITER $$
drop trigger if exists before_insert_joueur;
CREATE TRIGGER before_insert_joueur
BEFORE INSERT ON joueur
FOR EACH ROW
BEGIN
    DECLARE name_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO name_count FROM joueur WHERE nomJoueur = NEW.nomJoueur AND equipeID = NEW.equipeID;

    IF name_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Joueur déjà existante dans l\'equipe';
    END IF;
END$$

DELIMITER ;


DELIMITER $$
drop procedure if exists sp_createJoueur;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createJoueur`(
    IN p_nomJoueur VARCHAR(50),
    IN p_prenomJoueur VARCHAR(50),
    IN p_numberJoueur int,
    IN p_equipeID int
)
BEGIN
    if ( select exists (select 1 from joueur where nomJoueur = p_nomJoueur AND equipeID = p_equipeID) ) THEN

        select 'Joueur déjà existant dans l\'équipe!!';

    ELSE

        insert into joueur
        (
            nomJoueur,
            prenomJoueur,
            numeroJoueur,
            equipeID
        )
        values
        (
            p_nomJoueur,
            p_prenomJoueur,
            p_numberJoueur,
            p_equipeID
        );

    END IF;
END$$
DELIMITER ;

DELIMITER $$
drop trigger if exists before_insert_cote;
CREATE TRIGGER before_insert_cote
BEFORE INSERT ON cote
FOR EACH ROW
BEGIN
    DECLARE teamID_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO teamID_count FROM cote WHERE coteVictoire = NEW.coteVictoire;

    IF teamID_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Une équipe ne peut pas avoir plusieurs côtes';
    END IF;
END$$

DELIMITER ;


DELIMITER $$
drop procedure if exists sp_createCote;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createCote`(
    IN p_coteVictoire float,
    IN p_equipeID int
)
BEGIN
    if ( select exists (select 1 from cote where coteVictoire = p_coteVictoire AND equipeID = p_equipeID) ) THEN

        select 'Cote déja attribué...';

    ELSE

        insert into cote
        (
            coteVictoire,
            equipeID
        )
        values
        (
            p_coteVictoire,
            p_equipeID
        );

    END IF;
END$$
DELIMITER ;
