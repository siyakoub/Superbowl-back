from app import mysql


class Comment:

    def __init__(self, matchID, commentateur, commentaire, dateHeureComment, commentID=None):
        self.matchID = matchID
        self.commentateur = commentateur
        self.commentaire = commentaire
        self.dateHeureComment = dateHeureComment
        self.commentID = commentID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createComment(%s, %s, %s, %s)",
            (self.matchID, self.commentateur, self.commentateur, self.dateHeureComment)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(id_comment):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from commentaire where commentaireID=%s",
            (id_comment,)
        )
        comment_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if comment_data:
            comment_id = comment_data[0]
            match_id = comment_data[1]
            commentateur = comment_data[2]
            text = comment_data[3]
            dateHeure = comment_data[4]
            return Comment(match_id, commentateur, text, dateHeure, comment_id)
        else:
            return None

    @staticmethod
    def get_all_by_match_id(match_id: int):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from commentaire where confrontationID=%s",
            (match_id,)
        )
        comments_data = cursor.fetchall()
        cursor.close()
        conn.close()
        comments = []
        if comments_data:
            for comment_data in comments_data:
                comment_id = comment_data[0]
                match_id = comment_data[1]
                commentateur = comment_data[2]
                text = comment_data[3]
                dateHeure = comment_data[4]
                comments.append(
                    Comment(match_id, commentateur, text, dateHeure, comment_id)
                )
            return comments
        else:
            return None

    @staticmethod
    def get_all_comment():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from commentaire"
        )
        comments_data = cursor.fetchall()
        comments = []
        cursor.close()
        conn.close()
        if comments_data:
            for comment_data in comments_data:
                comment_id = comment_data[0]
                match_id = comment_data[1]
                commentateur = comment_data[2]
                text = comment_data[3]
                dateHeure = comment_data[4]
                comments.append(
                    Comment(match_id, commentateur, text, dateHeure, comment_id)
                )
            return comments
        else:
            return None

    def update_comment(self, match_id, commentateur, text):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update commentaire set confrontationID=%s, commentateur=%s, texteCommentaire=%s, dateHeureCommentaire= NOW() where commentaireID=%s",
            (match_id, commentateur, text, self.commentID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete_comment(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from Commentaire where commentaireID=%s",
            (self.commentID,)
        )
        conn.commit()
        cursor.close()
        conn.close()


