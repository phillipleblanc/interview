from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)


@app.route("/health")
def health():
    return "ok"


@app.route("/data", methods=["POST"])
def post_data():
    json_data = json.loads(request.data)
    if len(json_data) > 0:
        for record in json_data:
            data.add_data_record(record)
    return "ok"


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data.get_data_records())


@app.route("/clear", methods=["POST"])
def clear():
    data.clear_records()
    return "ok"


if __name__ == "__main__":
    port = 5000
    print(f"data-ingestor listening on port: {port}")
    app.run("0.0.0.0", port)
