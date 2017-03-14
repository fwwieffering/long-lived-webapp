from flask import Flask, Response
import logging
import atexit
import time
import json

app = Flask(__name__)
logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.INFO)
#--------------------------------------- exit handling ----------------------------
@atexit.register
def exit_handler():
    logger.info("Received exit command. Sleeping 60 seconds")
    time.sleep(60)

@app.route('/', methods=['GET'])
def up():
    return rjson({'status': 'happy'})


def rjson(blob, statcode=200):
    return Response(json.dumps(blob), mimetype='application/json',
                    status=statcode)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
