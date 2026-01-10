# main_test.py

from openhtf.output.callbacks import console_summary
import openhtf as htf


@htf.measures(
    htf.Measurement("resistor_val")
    .doc("Computed resistor value")
)
def resistor_test(test):
  #test.measurements.resistor_val = 100
  test.measurements["resistor_val"] = 10

def main():
  test = htf.Test(resistor_test)
  test.add_output_callbacks(console_summary.ConsoleSummary())
  test.execute()

if __name__ == "__main__":
  main()
