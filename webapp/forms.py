from django import forms
from .models import Order, SolarPanel, SolarInverter, Customer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'panels_ordered', 'inverters_ordered']
        widgets = {
            'panels_ordered': forms.CheckboxSelectMultiple(),
            'inverters_ordered': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['panels_ordered'].queryset = SolarPanel.objects.all()
        self.fields['inverters_ordered'].queryset = SolarInverter.objects.all()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']