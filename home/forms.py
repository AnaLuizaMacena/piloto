# forms.py
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome completo'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )


class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do produto'})
    )
    preco = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço','data-mask':'#.##0,00', 'data-mask-reserve': 'true'})
        )
    
