
from flask import Blueprint, current_app, request
from models.request import WebRequestSchema
from marshmallow import ValidationError


total_sales_value_bp = Blueprint("total_sales_value", __name__)


@total_sales_value_bp.route("/v1/total_sales_value/<store_id>")
def total_sales_value(store_id):
    app = current_app
    request_data = {
        "store_id": store_id,
        "date": request.args.get("date")
    }
    app.logger.debug("Unvalidated Request:" + str(request_data))

    try:
        valid_req = WebRequestSchema().load(request_data)
    except ValidationError as request_err:
        app.logger.error("Unvalidated request: " + str(request_err.messages))
        return request_err.messages, 400

    return WebRequestSchema().dump(valid_req)
    # return str(valid_req.store_id) + " on " + valid_req.date.strftime("%Y-%m-%d")
