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
            dateInscription
        )
        values
        (
            p_name,
            p_prenom,
            p_adressEmail,
            p_password,
            now()
        );

    END IF;
END$$
DELIMITER ;

