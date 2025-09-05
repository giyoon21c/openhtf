import openhtf as htf


def phase_resistance_test(test):
  #test.measurements.resistance=10.5
  test.measurements.resistance=1

def main():
  min_resistance = 5
  max_resistance = 17

  measurement = htf.Measurement('resistance').in_range(min_resistance, max_resistance)
  configured_phase = htf.measures(measurement)(phase_resistance_test)

  test = htf.Test([configured_phase]) 
  test.execute(lambda: "SN1234")

if __name__ == "__main__":
  main()