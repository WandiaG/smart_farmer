from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    member_code = IntegerField('Member Code', validators=[DataRequired(), Length(min=1, max=10)] )
    submit = SubmitField('Search')

