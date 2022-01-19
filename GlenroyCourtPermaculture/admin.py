from django.contrib import admin
from GlenroyCourtPermaculture.models import Post
from GlenroyCourtPermaculture.models import Comment
from django_summernote.admin import SummernoteModelAdmin
from django import forms

admin.site.register(Post)
admin.site.register(Comment)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].required = True

    def clean(self):
        title = self.cleaned_data['title']
        if not title.istitle():
            raise forms.ValidationError({'title': "Not a proper titlecased string"})    

    class Meta:
        model = Post
        fields = '__all__'

