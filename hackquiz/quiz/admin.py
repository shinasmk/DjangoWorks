from django.contrib import admin
from quiz.models import Category,Questions,Answers


# Register your models here.
class AnswerAdmin(admin.StackedInline):
    model=Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]


admin.site.register(Category)
admin.site.register(Answers)
admin.site.register(Questions,QuestionAdmin)



