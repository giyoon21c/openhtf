import openhtf as htf
from openhtf.util import units
import random
import time

import os.path
from openhtf import PhaseNameCase, output
from openhtf.output.callbacks import json_factory

output_dir = "."


@htf.measures(
  htf.Measurement("voltage_over_time")
  .with_dimensions(units.SECOND, units.VOLT) # Input axes: time, voltage
  .with_units(units.OHM)  # Output unit: resistance in ohms
)
def phase_voltage_measurement(test):
  for t in range(10):
    timestamp = t
    voltage = round(random.uniform(3.3, 3.5), 2)
    current = round(random.uniform(0.3, 0.5), 2)
    print(f'{voltage} {current}')
    test.measurements.voltage_over_time[timestamp, voltage] = current
    time.sleep(0.1)

def main():
  test = htf.Test(phase_voltage_measurement)

  # adds json output
  test.add_output_callbacks(
      json_factory.OutputToJSON(
          os.path.join(output_dir, '{dut_id}.multi-dimensional.json'), indent=2
      )
  )
  
  test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()


