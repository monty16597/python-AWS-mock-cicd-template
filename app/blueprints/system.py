from flask import Blueprint

system_bp = Blueprint("system", __name__)


@system_bp.route("/", methods=["GET"])
def index():
    return "Use post request to /generate_pdf to generate a PDF file", 200


@system_bp.route("/health", methods=["GET"])
def health():
    return "OK", 200
