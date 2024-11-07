from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
    flash,
)
from flask_login import (
    login_required,
    logout_user,
    login_user

)

from traticker.app import login_manager
from traticker.models.user import User
from traticker.utils.discord import send_discord_webhook

router = Blueprint("user", __name__, url_prefix="/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@router.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            send_discord_webhook(f"{user.username} がログインしました。")
            return redirect(url_for("domain.domain_list"))
        if user is None:
            send_discord_webhook(f"未知のユーザー名: {username}でログインを試みました")
            flash("ログインに失敗しました。ユーザー名が間違っています。")
        else:
            send_discord_webhook(f"{user.username} がログインに失敗しました。")
            flash("ログインに失敗しました。パスワードが間違っています。")

    return render_template("user/login.html")


