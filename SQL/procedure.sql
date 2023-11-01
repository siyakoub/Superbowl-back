use superBowlBdd;
-- Changement de délimiteur pour pouvoir créer des procédures et des déclencheurs
DELIMITER $$

-- Supprimez le déclencheur s'il existe déjà
DROP TRIGGER IF EXISTS before_insert_user;

-- Créez le déclencheur before_insert_user
CREATE TRIGGER before_insert_user
BEFORE INSERT ON Utilisateur
FOR EACH ROW
BEGIN
    DECLARE email_count INT;

    -- Vérifiez si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO email_count FROM Utilisateur WHERE adresseEmail = NEW.adresseEmail;

    IF email_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Adresse e-mail déjà existante';
    END IF;
END $$

-- Rétablissez le délimiteur par défaut
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
END $$
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
END $$
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
END $$

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
END $$

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
END $$
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
END $$

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
END $$
DELIMITER ;

DELIMITER $$
drop trigger if exists before_insert_cote;
CREATE TRIGGER before_insert_cote
BEFORE INSERT ON cote
FOR EACH ROW
BEGIN
    DECLARE teamID_count INT;

    -- Vérifier si l'adresse e-mail existe déjà
    SELECT COUNT(*) INTO teamID_count FROM cote WHERE equipeID = NEW.equipeID;

    IF teamID_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Une équipe ne peut pas avoir plusieurs côtes';
    END IF;
END $$

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
END $$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createMatch;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createMatch`(
    IN p_teamDomicileID int,
    IN p_teamExterieurID int,
    IN p_dateHeureDebut datetime,
    IN p_dateHeureFin datetime,
    IN p_statut varchar(10)
)
BEGIN
    if ( select exists (select 1 from confrontation where equipeDomicileID = p_teamDomicileID AND equipeExterieurID = p_teamExterieurID AND dateHeureDebut = p_dateHeureDebut AND dateHeureFin = p_dateHeureFin) ) THEN

        select 'Match déjà enregistré...';

    ELSE

        insert into confrontation
        (
            equipeDomicileID,
            equipeExterieurID,
            dateHeureDebut,
            dateHeureFin,
            statut
        )
        values
        (
            p_teamDomicileID,
            p_teamExterieurID,
            p_dateHeureDebut,
            p_dateHeureFin,
            p_statut
        );

    END IF;
END $$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createComment;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createComment`(
    IN p_confrontation_id int,
    IN p_commentateur varchar(100),
    IN p_text_comment Text,
    IN p_dateHeureComment datetime
)
BEGIN
    if ( select exists (select 1 from commentaire where confrontationID = p_confrontation_id AND texteCommentaire = p_text_comment) ) THEN

        select 'Commentaire déjà enregistré...';

    ELSE

        insert into confrontation
        (
            confrontationID,
            commentateur,
            texteCommentaire,
            dateHeureCommentaire
        )
        values
        (
            p_confrontation_id,
            p_commentateur,
            p_text_comment,
            p_dateHeureComment
        );

    END IF;
END $$
DELIMITER ;


DELIMITER $$
drop procedure if exists sp_createBet;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createBet`(
    IN p_userID int,
    IN p_confrontation_id int,
    IN p_equipeID int,
    IN p_montantMiser Decimal(10,2),
    IN p_montantGagnePerdu Decimal(10,2)
)
BEGIN

    insert into Pari
    (
        userID,
        confrontationID,
        equipeID,
        montantMise,
        montantGagnePerdu
    )
    values
    (
        p_userID,
        p_confrontation_id,
        p_equipeID,
        p_montantMiser,
        p_montantGagnePerdu
    );

END $$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createEvent;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createEvent`(
    IN p_description text,
    IN p_type varchar(50),
    IN p_confrontation_id int
)
BEGIN
    if ( select exists (select 1 from Evenement where descriptionEvenement = p_description AND confrontationID = p_confrontation_id) ) THEN

        select 'Evenement déjà enregistré...';

    ELSE

        insert into Evenement
        (
            descriptionEvenement,
            dateHeureEvenement,
            typeEvenement,
            confrontationID
        )
        values
        (
            p_description,
            NOW(),
            p_type,
            p_confrontation_id
        );

    END IF;
END $$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createHistoriqueMise;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createHistoriqueMise`(
    IN p_userID int,
    IN p_confrontationID int,
    IN p_montantMiser decimal(10,2),
    IN p_resultat varchar(6)
)
BEGIN

    insert into HistoriqueMises
    (
        userID,
        confrontationID,
        montantMise,
        resultat
    )
    values
    (
        p_userID,
        p_confrontationID,
        p_montantMiser,
        p_resultat
    );

END $$
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createSession;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createSession`(
    IN p_email varchar(254),
    IN p_token varchar(254),
    IN p_dateHeureDebut datetime,
    IN p_dateHeureFin datetime
)
BEGIN

    insert into session
    (
        email,
        token,
        dateHeureDebut,
        dateHeureFin
    )
    values
    (
        p_email,
        p_token,
        p_dateHeureDebut,
        p_dateHeureFin
    );

END $$
DELIMITER ;




DELIMITER $$
drop event if exists UpdateMatchBeginStatusEvent;
CREATE EVENT UpdateMatchBeginStatusEvent
ON SCHEDULE EVERY 5 MINUTE
DO
BEGIN
    UPDATE Confrontation
    SET statut = 'EnCours'
    WHERE dateHeureDebut <= NOW();
END;

$$

DELIMITER ;

DELIMITER $$
drop event if exists UpdateMatchEndStatusEvent;
CREATE EVENT UpdateMatchEndStatusEvent
ON SCHEDULE EVERY 5 MINUTE
DO
BEGIN
    UPDATE Confrontation
    SET statut = 'Termine', dateHeureFin=NOW()
    WHERE dateHeureFin <= NOW();
END;

$$

DELIMITER ;

