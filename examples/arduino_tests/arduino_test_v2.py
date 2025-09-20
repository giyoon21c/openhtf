import openhtf as htf

from openhtf.output.callbacks import console_summary
from openhtf.output.callbacks import json_factory

@htf.measures(htf.Measurement("P4_digital")
              .doc("Pin 4 Digital Measurement")
              .equals(True))
@htf.measures(htf.Measurement("P5_digital")
              .doc("Pin 5 Digital Measurement")
              .equals(True))
@htf.measures(htf.Measurement("P6_digital")
              .doc("Pin 6 Digital Measurement")
              .equals(False))


def digital_read(test):
  test.measurements.P4_digital = False 
  #test.measurements.P4_digital = True 
  test.measurements.P5_digital = True 
  test.measurements.P6_digital = False 

# beginning of the test
test = htf.Test(digital_read)
test.add_output_callbacks(console_summary.ConsoleSummary())

test.execute()
