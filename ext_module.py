import logging
import logging_module as lm
import json
import requests
from threading import Thread

log = lm.get_logger(__name__)


class External():
    def __init__(self, ext_url, imei_map):
        self.ext_url = ext_url
        self.imei_map = imei_map


    def __can_send_out(self, device_id):
        res = self.imei_map.get(device_id) is not None
        log.info('Position for device id %s can be sent: %r', device_id, res)
        return res


    def __create_gps_event_string(self, position):
        device_id = position.get('deviceId')
        imei_no = str(self.imei_map.get(device_id))
        latitude = str(position['latitude'])
        longitude = str(position['longitude'])
        speed = str(position['speed'])
        time = str(position['fixTime'])
        gps_event = {
            'imei_no': imei_no,
            'lattitude': latitude,
            'longitude': longitude,
            'lattitude_direction': 'N',
            'longitude_direction': 'E',
            'speed': speed,
            'digital_port1': '0',
            'digital_port2': '0',
            'digital_port3': '0',
            'digital_port4': '0',
            'analog_port1': '0',
            'analog_port2': '0',
            'angle': '0',
            'satellite': '0',
            'time': time,
            'battery_voltage': '20',
            'gps_validity': 'A'
        }
        return json.dumps(gps_event)

    def __send_data(self, position):
        message = self.__create_gps_event_string(position)
        resp = requests.post(self.ext_url, data=message)
        log.info('response: %s | request: %s', resp.text, message)


    def process_position(self, device_id, position):
        if self.__can_send_out(device_id):
            Thread(target=self.__send_data, args=(position,)).start()

