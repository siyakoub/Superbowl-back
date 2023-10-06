import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.odds_service import OddsService

odds_bp = Blueprint("odd", __name__)

