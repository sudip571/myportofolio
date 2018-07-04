from flask import Blueprint

porto=Blueprint('porto',__name__)

from . import views
