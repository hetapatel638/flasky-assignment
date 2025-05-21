from flask import Blueprint
from ..models import Permission
from . import views  # noqa: F401
from . import errors  # noqa: F401

main = Blueprint('main', __name__)

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)