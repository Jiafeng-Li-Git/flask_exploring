
from flask import Blueprint, current_app, request


total_sales_value_bp = Blueprint("total_sales_value", __name__)


@total_sales_value_bp.route("/v1/total_sales_value/<store_id>")
def total_sales_value(store_id):
    app = current_app
    request_data = {
        "store_id": store_id,
        "date": request.args.get("date")
    }
    app.logger.debug("Unvalidated Request:" + str(request_data))
    return request_data["store_id"] + " on " + request_data["date"]
