from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    language = models.CharField(max_length=10, default='en')  # e.g., 'en' or 'hi'
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200)
    option_four = models.CharField(max_length=200)
    correct_option = models.PositiveSmallIntegerField()  # e.g., 1, 2, 3, or 4

    def __str__(self):
        return f'Quiz for {self.lesson.title}'
