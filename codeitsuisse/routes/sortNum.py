import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def sortNumber():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");
    inputValue.sort()
    logging.info("My result :{}".format(inputValue))
    return json.dumps(inputValue);



