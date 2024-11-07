from traticker.app import app
from traticker.views.user import (
    router as user_router
)

routers = [
    user_router
]
for router in routers:
    app.register_blueprint(router)

