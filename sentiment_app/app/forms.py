from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class AnalyzeForm(FlaskForm):
    text = TextAreaField(
        "Enter your sentence",
        validators=[DataRequired(), Length(min=1, max=500)]
    )
    submit = SubmitField("Analyze")
