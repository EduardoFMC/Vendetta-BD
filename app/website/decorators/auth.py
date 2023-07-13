from flask import  session, redirect, url_for, flash
from functools import wraps

def is_authenticated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_matricula' not in session:
            flash('Faça o Login(Não autorizado)', category='error')
            return redirect(url_for('profile.login'))

        return f(*args, **kwargs)
    return wrapper

def admin_permission(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session['user_permission']:
            flash('Não autorizado! Apenas administradores', category='error')
            return redirect(url_for('avaliacoes.home'))

        return f(*args, **kwargs)
    return wrapper
    
