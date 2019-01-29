"""
Created by 简单7月 on 2019/1/28
"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

from app.models.Base import db
from app.models.User import User
from app.validate.auth import UserRegisterForm, UserLoginForm
from . import web

__author__ = '简单7月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    用户注册
    :return:
    """
    # 验证
    form = UserRegisterForm(request.form)
    # POST方式提交并验证
    if request.method == "POST" and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))

    # 返回视图文件，templates/auth/register.html
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    """
    用户登录
    :return:
    """
    form = UserLoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            remember = False
            print(request.form)
            print(request.form.get('remember'))
            if request.args.get('remember'):
                remember = True
            login_user(user, remember=remember)

            next = request.args.get('next')
            if not next or not next.starswitch('/'):
                next = url_for('web.index')

            return redirect(next)
        else:
            flash("账户名或密码错误", category='login_error')
    return render_template('auth/login.html', form=form)
