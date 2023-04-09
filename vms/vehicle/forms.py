from django import forms


from vehicle.models import Vehicles


class VehicleForm(forms.ModelForm):
    class Meta():
        model=Vehicles
        fields=[
            "vehicle_name",
            "vehicle_number",
            "vehicle_model",
            "owner",
            "km_driven",
            "date_of_purchase",
            "fuel_type"
        ]

        widgets={
            "date_of_purchase":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "fuel_type":forms.Select(attrs={"class":"form-select"})
        }