drop database if exists superBowlBdd;
create database superBowlBdd;
use superBowlBdd;
drop table if exists Utilisateur;
-- Création de la table Utilisateur
CREATE TABLE Utilisateur (
    userID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    adresseEmail VARCHAR(254) NOT NULL,
    motDePasse VARCHAR(254) NOT NULL, -- Assurez-vous de stocker les mots de passe de manière sécurisée (hachage)
    dateInscription DATETIME NOT NULL,
    actif int not null
);
drop table if exists Equipe;
-- Création de la table Équipe
CREATE TABLE Equipe (
    equipeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nomEquipe VARCHAR(100) NOT NULL,
    paysOrigine VARCHAR(50) NOT NULL
);
drop table if exists Joueur;
-- Création de la table Joueur
CREATE TABLE Joueur (
    joueurID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nomJoueur VARCHAR(50) NOT NULL,
    prenomJoueur VARCHAR(50) NOT NULL,
    numeroJoueur INT NOT NULL,
    equipeID INT NOT NULL,
    FOREIGN KEY (EquipeID) REFERENCES Equipe(equipeID)
);
drop table if exists Confrontation;
-- Création de la table Confrontation(Match)
CREATE TABLE Confrontation (
    confrontationID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    equipeDomicileID INT NOT NULL,
    equipeExterieurID INT NOT NULL,
    dateHeureDebut DATETIME NOT NULL,
    dateHeureFin DATETIME NOT NULL,
    statut ENUM('Termine', 'AVenir', 'EnCours') NOT NULL,
    FOREIGN KEY (equipeDomicileID) REFERENCES Equipe(equipeID),
    FOREIGN KEY (equipeExterieurID) REFERENCES Equipe(equipeID)
);
drop table if exists Cote;
-- Création de la table Cote
CREATE TABLE Cote (
    coteID float NOT NULL AUTO_INCREMENT PRIMARY KEY,
    equipeID INT NOT NULL,
    coteVictoire DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (equipeID) REFERENCES Equipe(equipeID)
);
drop table if exists Pari;
-- Création de la table Pari
CREATE TABLE Pari (
    pariID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userID INT NOT NULL,
    confrontationID INT NOT NULL,
    equipeID INT NOT NULL,
    montantMise DECIMAL(10,2) NOT NULL,
    montantGagnePerdu DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (userID) REFERENCES Utilisateur(userID),
    FOREIGN KEY (confrontationID) REFERENCES Confrontation(confrontationID),
    FOREIGN KEY (equipeID) REFERENCES Equipe(equipeID)
);
drop table if exists Commentaire;
-- Création de la table Commentaire
CREATE TABLE Commentaire (
    commentaireID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    confrontationID INT NOT NULL,
    commentateur VARCHAR(100) NOT NULL,
    texteCommentaire TEXT,
    dateHeureCommentaire DATETIME NOT NULL,
    FOREIGN KEY (confrontationID) REFERENCES Confrontation(confrontationID)
);
drop table if exists HistoriqueMises;
-- Création de la table HistoriqueMises
CREATE TABLE HistoriqueMises (
    historiqueID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userID INT NOT NULL,
    confrontationID INT NOT NULL,
    montantMise DECIMAL(10,2) NOT NULL,
    resultat ENUM('Gagne', 'Perdu') NOT NULL,
    FOREIGN KEY (userID) REFERENCES Utilisateur(userID),
    FOREIGN KEY (confrontationID) REFERENCES Confrontation(confrontationID)
);
drop table if exists Evenement;
-- Création de la table Evenement
CREATE TABLE Evenement (
    eventID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descriptionEvenement TEXT,
    dateHeureEvenement DATETIME NOT NULL,
    typeEvenement VARCHAR(50) NOT NULL,
    confrontationID INT NOT NULL,
    FOREIGN KEY (confrontationID) REFERENCES Confrontation(confrontationID)
);
drop table if exists Administrateur;
-- Création de la table Administrateur
CREATE TABLE Administrateur(
    administrateurID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    pass varchar(100) NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    actif int not null
);

-- Création de la table session
-- Ajoutez un index à la colonne "adresseEmail" de la table "Utilisateur"
ALTER TABLE Utilisateur
ADD INDEX idx_adresseEmail (adresseEmail);

drop table if exists session;
-- Créez la table "session" avec la clé étrangère vers la colonne "adresseEmail" de la table "Utilisateur"
CREATE TABLE session (
    sessionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(254) NOT NULL,
    token VARCHAR(254) NOT NULL,
    dateHeureDebut DATETIME NOT NULL,
    dateHeureFin DATETIME,
    FOREIGN KEY (email) REFERENCES Utilisateur (adresseEmail)
);

