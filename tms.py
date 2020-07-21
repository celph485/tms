import json
import os
import requests
import threading
import time
import logging
import logging_module as lm
from flask import Flask
from config_module import Config
from ext_module import External

app = Flask(__name__)
app.config.from_object(Config())
logging.basicConfig(level=logging.INFO, handlers=[lm.get_file_handler(), lm.get_console_handler()])

data_store = {
    'device_position_map' : {},
    'session_id' : 'asdad-adas'
}

ext = External(app.config['EXT_URL'], app.config['IMEI_MAP'])


def update_session_id(force=True):
    if force is True or data_store['session_id'] is None: 
        app.logger.info('Trying to accquiring new session')
        token_res = requests.get(app.config['TOKEN_URL'])
        app.logger.info('response status: %s',token_res.status_code)
        data_store['session_id'] = token_res.cookies['JSESSIONID']
        app.logger.info('New session accquired successfully.')


def get_device_position_map():
    app.logger.info('Record updation started')
    update_session_id(False)
    req_cookies = dict(JSESSIONID=data_store['session_id'])
    app.logger.info('Calling traccar server for latest positions')
    pos_res = requests.get(app.config['POSITION_URL'], cookies=req_cookies)
    app.logger.info('Position response status: %s',pos_res.status_code)
    if pos_res.status_code == 401:
        app.logger.info('Current session has expired, terminating record updation process.')
        update_session_id(True)
    else:
        positions = json.loads(pos_res.text)
        if positions is not None:
            app.logger.info('Received %d positions from traccar server.', len(positions))
            for position in positions:
                device_id = position.get('deviceId')
                if device_id is not None:
                    data_store['device_position_map'].update({device_id: position})
                    ext.process_position(device_id, position)
            app.logger.info('Record updation process is completed successfully.')
        else:
            app.logger.info('No positions recived, terminating record updation process.')


@app.before_first_request
def update_map():
    app.logger.info('Traccar Middleware Service')
    update_session_id(True)
    def run_job():
        while True:
            update_frequency = app.config['DATA_REFRESH_FRQUENCY']
            get_device_position_map()
            app.logger.info('Record updation process will start after %d seconds.', update_frequency)
            time.sleep(update_frequency)
    thread = threading.Thread(target=run_job)
    thread.start()

@app.route('/')
def hello_world():
    return 'Hello World...'


