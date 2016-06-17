from django import forms



class GetCalificate(forms.Form):

	estrellas = forms.MultipleChoiceField(		
        choices= (("4","4"),
        	("5","5"),
        	("3", "3"),
        	("2", "2"),
        	("1", "1"),
        ), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )