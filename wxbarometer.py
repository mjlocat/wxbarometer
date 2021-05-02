import time
import sys
from datetime import datetime
from bmp280 import BMP280
from smbus import SMBus
from dotenv import dotenv_values
import mysql.connector

config = dotenv_values(".env")
i2c_bus = int(config["I2C_BUS"])
i2c_addr = int(config["SENSOR_ADDR"], 16)
altitude = int(config["ALTITUDE_METERS"])
wait_time = int(config["TIME_BETWEEN_READINGS"])
dbconfig = {
    'user': config['DBUSER'],
    'password': config['DBPASS'],
    'host': config['DBHOST'],
    'database': config['DBDATABASE']
}
cnx = mysql.connector.connect(**dbconfig)
cursor = cnx.cursor()
insert_pressure = "INSERT INTO pressure (pressure, ts) VALUES (%(P)s, %(t)s)"

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
        cursor.execute(insert_pressure, { "P": sea_level_pressure, "t": ts })
        cnx.commit()
        time.sleep(wait_time)
    except KeyboardInterrupt:
        cursor.close()
        cnx.close()
        sys.exit() 
