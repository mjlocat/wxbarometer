import time
import sys
import json
from datetime import datetime
from bmp280 import BMP280
from smbus import SMBus
from dotenv import dotenv_values
import paho.mqtt.client as mqtt

config = dotenv_values(".env")
i2c_bus = int(config["I2C_BUS"])
i2c_addr = int(config["SENSOR_ADDR"], 16)
altitude = int(config["ALTITUDE_METERS"])
wait_time = int(config["TIME_BETWEEN_READINGS"])

client = mqtt.Client(client_id="wx-producer")
client.connect(config["MQTT_HOST"])
client.loop_start()

bus = SMBus(i2c_bus)
bmp280 = BMP280(i2c_addr=i2c_addr, i2c_dev=bus)
bmp280.setup(mode="forced")
while True:
    try:
        ts = datetime.now().timestamp()
        temp = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        altitude = altitude
        sea_level_pressure = pressure + ((pressure * 9.80665 * altitude)/(287 * (273 + temp + (altitude/400))))
        client.publish("wx/barometer", json.dumps({ "P": sea_level_pressure, "t": ts }))
        time.sleep(wait_time)
    except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()
        sys.exit() 
