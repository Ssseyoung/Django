from django.db import models

# Create your models here.
# 게시글
class Board(models.Model):
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    
    def __str__(self):
        return self.title


# 댓글
# - 댓글 내용, 외래키(게시글)
class Comment(models.Model):
    content = models.TextField('댓글 내용')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.board.title} - 댓글(id: {self.id})'
    
    