import openhtf as htf

min_resistance = 5
max_resistance = 17

@htf.measures(
  htf.Measurement('resistance').in_range(min_resistance, max_resistance)
)
def phase_resistance_test(test):
  #test.measurements.resistance=10.5
  test.measurements.resistance=10.5

def main():

  #measurement = htf.Measurement('resistance').in_range(min_resistance, max_resistance)
  #configured_phase = htf.measures(measurement)(phase_resistance_test)
  #test = htf.Test([configured_phase]) 

  test = htf.Test(phase_resistance_test)
  test.execute(lambda: "SN1234")

if __name__ == "__main__":
  main()