
import os
import config
from app_factory import create_app


if os.getenv("ENV") == "dev":
    configuration = config.DevConfig
else:
    configuration = config.ProductionConfig

app = create_app(configuration)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 8080)))
