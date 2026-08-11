# criar formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from newsite.models import Usuario
from flask_wtf.file import MultipleFileField


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators= [DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário inexistente, crie uma conta')




class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('nome do usuário', validators= [DataRequired()])
    senha = PasswordField('Senha', validators= [DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('confirmação de senha', validators= [DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('e-mail já cadastrado, faça login para continuar')
        
class FormFoto(FlaskForm):
    foto = MultipleFileField('foto', validators=[DataRequired()])
    botao_confirmacao = SubmitField('enviar')