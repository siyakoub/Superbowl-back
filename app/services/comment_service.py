from app.models.comment import Comment


class CommentService:

    @staticmethod
    def get_comment_by_id_service(comment_id):
        return Comment.get_by_id(comment_id)

    @staticmethod
    def get_all_comment_by_match_id_service(match_id):
        return Comment.get_all_by_match_id(match_id)

    @staticmethod
    def get_all_comment_service():
        return Comment.get_all_comment()

    @staticmethod
    def create_comment_service(match_id, commentateur, text, dateHeure):
        comment = Comment(match_id, commentateur, text, dateHeure)
        comment.save()

    @staticmethod
    def update_comment_service(commentID, new_match_id, new_commentateur, new_text):
        comment = Comment.get_by_id(commentID)
        if comment:
            comment.update_comment(new_match_id, new_commentateur, new_text)
        else:
            pass

    @staticmethod
    def delete_comment_service(commentID):
        comment = Comment.get_by_id(commentID)
        if comment:
            comment.delete_comment()
        else:
            pass
        