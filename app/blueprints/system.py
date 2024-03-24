from flask import Blueprint

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    return "Use post request to /generate_pdf to generate a PDF file", 200


@main_bp.route("/health", methods=["GET"])
def health():
    return "OK", 200
