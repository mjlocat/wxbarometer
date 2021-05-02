# wxbarometer

This python script interfaces with the [Bosch BMP280](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp280/) pressure sensor over the i2c bus and writes the pressure readings to a database. It leverages the python [BMP280](https://github.com/pimoroni/bmp280-python) library to read data from the sensor. It then converts the pressure reading to the sea level adjusted pressure using [this algorithm](https://gist.github.com/cubapp/23dd4e91814a995b8ff06f406679abcf) before storing the results.

## Installation

1. Install the supporting libraries `sudo pip3 install -r requirements.txt`
1. Copy the sample environment file `cp env.sample .env`
1. Edit the .env file following the instructions in the file
1. Create the pressure table in your database from `create_table.sql`
1. Install the checkrunning.sh script in your crontab: `* * * * * source ~/.bashrc && cd ~/wxbarometer && ./checkrunning.sh 2>&1 > /dev/null`

