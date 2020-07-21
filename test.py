from datetime import datetime
import pytz




#print(pytz.all_timezones)

def convert_time_zone_to_ist(dt_str):
    input_format = '%Y-%m-%dT%H:%M:%S.000%z'
    output_format = '%Y-%m-%d %H:%M:%S'
    req_tz = 'Asia/Calcutta'
    dt = datetime.strptime(str, input_format)
    local_dt = dt.astimezone(pytz.timezone(req_tz))
    local_dt_str = local_dt.strftime(output_format)
    print(dt_str , ' ', dt, ' ', local_dt, ' ', local_dt_str)
    return local_dt_str

input = [
    '2020-07-21T01:06:52.000+0000',
    '2020-07-21T02:06:57.000+0530',
    '2020-07-21T01:06:52.000+0000',
    '2020-07-21T01:59:38.000+0000',
    '2020-07-21T02:06:57.000+0000',
    '2020-07-21T02:07:18.000+0000',
    '2020-07-21T01:59:38.000+0000',
    '2020-07-21T02:05:44.000+0000',
    '2020-07-21T02:07:18.000+0000',
    '2020-07-21T02:07:51.000+0000',
    '2020-07-21T02:07:08.000+0000',
    '2020-07-21T02:05:44.000+0000',
    '2020-07-21T01:31:03.000+0000',
    '2020-07-21T00:21:01.000+0000',
    '2020-07-21T02:07:51.000+0000',
    '2020-07-21T02:04:52.000+0000',
    '2020-07-21T02:07:08.000+0000',
    '2020-07-21T01:31:03.000+0000',
    '2020-07-21T02:06:46.000+0000',
    '2020-07-21T00:21:01.000+0000',
    '2020-07-21T02:06:46.000+0000',
    '2020-07-21T02:04:52.000+0000',
    '2020-07-21T01:17:34.000+0000',
    '2020-07-21T01:17:34.000+0000',
    '2020-07-20T20:41:47.000+0000',
    '2020-07-21T02:05:41.000+0000',
    '2020-07-20T20:41:47.000+0000',
    '2020-07-21T01:51:24.000+0000',
    '2020-07-21T02:05:41.000+0000',
    '2020-07-20T17:37:06.000+0000',
    '2020-07-21T01:51:24.000+0000',
    '2020-07-20T21:35:02.000+0000',
    '2020-07-20T17:37:06.000+0000',
    '2020-07-21T02:05:07.000+0000',
    '2020-07-20T21:35:02.000+0000',
    '2020-07-21T01:48:33.000+0000',
    '2020-07-21T02:05:07.000+0000',
    '2020-07-21T02:07:18.000+0000',
    '2020-07-21T02:05:10.000+0000',
    '2020-07-21T01:48:33.000+0000',
    '2020-07-21T02:07:18.000+0000',
    '2020-07-21T02:05:10.000+0000'
]

for str in input:
    convert_time_zone_to_ist(str)