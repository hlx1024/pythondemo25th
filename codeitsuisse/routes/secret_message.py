import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def encrypt():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
    	result.append(encry(test_case["n"],test_case["text"]))
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def encry(n,text):
	p_text = ""
	for ch in text:
		if ch.isalnum:
			p_text += ch.upper()

	start = 0
	list_of_substrings = []
	for i in range(n):
		length = len(p_text) // n
		remainder = len(p_text) % n

		if i < remainder:
			length += 1

		substring = p_text[start: start + length]
		list_of_substrings.append(substring)
		start += length
	result = ""
	for i in range(len(p_text)):
		str_index_in_list = i%n
		str_index = i // n
		result += list_of_substrings[str_index_in_list][str_index]
	return result