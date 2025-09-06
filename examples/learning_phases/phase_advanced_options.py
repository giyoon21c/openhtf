import openhtf as htf
import random
import os.path

from openhtf import PhaseNameCase, output
from openhtf.output.callbacks import json_factory
#from openhtf.output.callbacks import json_factory

@htf.PhaseOptions(name="new_phase_name", phase_name_case=PhaseNameCase.CAMEL)
def example_phase(test):
  return htf.PhaseResult.CONTINUE

output_dir = "."

def main():
  test = htf.Test(example_phase)
  # Configure the JSON outputter to save the report to a file.
  #test.add_output(output.json_factory.OutputToJSON("test_report.json"))

  test.add_output_callbacks(
      json_factory.OutputToJSON(
          os.path.join(output_dir, '{dut_id}.hello_world.json'), indent=2
      )
  )
  
  # Execute the test with a serial number
  test.execute(lambda: "SN1234")

if __name__ == '__main__':
    main()