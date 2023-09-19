import argparse
import json
import numpy as np
import time

parser = argparse.ArgumentParser(
            prog='Weather station random events generation',
            description='Generates weather station random events',
            epilog='Usage:')

parser.add_argument('--name', dest='name', required=True, help='Name of the weather station')
parser.add_argument('--lat', type=float, dest='lat', required=True, help='Latitude of the weather station')
parser.add_argument('--long', type=float, dest='lng', required=True, help='Longitude of the weather station')
parser.add_argument('--wait', type=float, dest='wait', required=True, help='Seconds to wait until the next measurement is generated')
parser.add_argument('--output_dir', dest='output_dir', required=True, help='Directory in which the measurements are generated')


args = parser.parse_args()

rng = np.random.default_rng()

while True:
    temp = float(rng.integers(20, high=25) + round(rng.random(), 1))
    humidity = float(rng.integers(60, high=75))
    pressure = float(rng.integers(1010, high=1020))
    timestamp = time.time()

    data = {'name': args.name, 'lat': args.lat, 'long': args.lng, 'temperature': temp, 'relative_humidity': humidity, 'pressure': pressure}
    print(data)
    with open('{output_dir}/measurement_{location}_{timestamp}.json'.format(output_dir=args.output_dir, location=args.name, timestamp=timestamp), 'w') as f:
        f.write(json.dumps(data))

    time.sleep(args.wait)
