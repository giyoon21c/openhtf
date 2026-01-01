import openhtf as htf
from openhtf import PhaseNameCase

# console summary
from openhtf.output.callbacks import console_summary

# json output
from openhtf.output.callbacks import json_factory 

@htf.PhaseOptions(name="new_phase_name", phase_name_case=PhaseNameCase.CAMEL)
def example_phase(test):
    return htf.PhaseResult.CONTINUE

def main():
  test = htf.Test(example_phase)

  # add a printed summary at the end of the test
  test.add_output_callbacks(console_summary.ConsoleSummary())

  # add a json output callback
  test.add_output_callbacks(json_factory.OutputToJSON("./test_results.json", indent=2))

  test.execute(lambda: "SN1234")

if __name__ == '__main__':
  main()

