import os
from flask import Blueprint, request, jsonify
from reportlab.pdfgen import canvas
from ..controllers import upload_pdf_file, generate_presigned_url

main_bp = Blueprint("pdf", __name__)


@main_bp.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    if request.method == "POST":
        # Get data from the POST request
        data = request.get_json()

        # Extract first name and last name from the received data
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")

        # Create a PDF file
        pdf_filename = f"{first_name}_{last_name}_info.pdf"
        pdf = canvas.Canvas(pdf_filename)

        pdf.drawString(100, 750, "First Name:")
        pdf.drawString(200, 750, first_name)
        pdf.drawString(100, 730, "Last Name:")
        pdf.drawString(200, 730, last_name)

        pdf.save()

        # Upload the generated PDF to S3
        try:
            upload_pdf_file(pdf_filename)
        except Exception as e:
            return jsonify({"error": f"Failed to uploading file: {e}"}), 500

        os.remove(pdf_filename)

        # Generate a presigned URL for the uploaded file
        try:
            download_url = generate_presigned_url(pdf_filename)
        except Exception as e:
            return jsonify({"error": f"Failed to generate public URL: {e}"}), 500

        return (
            jsonify(
                {
                    "message": "PDF created and uploaded to cloud successfully!",
                    "download_url": download_url,
                }
            ),
            200,
        )

    return jsonify({"error": "Invalid request method"}), 405
