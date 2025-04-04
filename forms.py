import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

# Load Data
train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        validators=[DataRequired()]
    )
    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info"
    )
    submit = SubmitField("Predict")

    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        self.airline.choices = [(val, val) for val in X_data.airline.unique()]
        self.source.choices = [(val, val) for val in X_data.source.unique()]
        self.destination.choices = [(val, val) for val in X_data.destination.unique()]
        self.additional_info.choices = [(val, val) for val in X_data.additional_info.unique()]
