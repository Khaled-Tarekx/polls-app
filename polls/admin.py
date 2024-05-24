from django.contrib import admin
from .models import Article, Membership, Publication, Puplisher, Question, Choice, Person, Group


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# class ArticleInline(admin.TabularInline):
#     model = Article
#     extra = 1



# class PuplicationAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['title']}),
#     ]
#     inlines = [ArticleInline]
#     search_fields = ['title']




admin.site.register(Question, QuestionAdmin)
# admin.site.register(Publication, PuplicationAdmin)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Publication)
admin.site.register(Puplisher)
admin.site.register(Article)