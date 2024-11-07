from traticker.app import db


class Setting(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)
    discord_webhook_url = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

