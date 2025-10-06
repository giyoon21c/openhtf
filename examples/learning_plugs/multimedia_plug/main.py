import openhtf as htf
from multimeter_plug import MultimeterPlug

@htf.plug(multimeter=MultimeterPlug)
def phase_test(test, multimeter):
  # Use the plug to measure voltage and current
  voltage = multimeter.measure_voltage()
  current = multimeter.measure_current()

def main():
  test = htf.Test(phase_test)
  test.execute(lambda: "SN1234")

if __name__ == "__main__":
  main()
