# books/forms.py
from django import forms
from .models import Book, Author, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'isbn', 'publication_date', 
                 'description', 'cover_image', 'pages', 'available']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['genres'].widget.attrs.update({'class': 'form-control select2'})
        self.fields['available'].widget.attrs.update({'class': 'form-check-input'})
