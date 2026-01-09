import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement("voltage")
    .in_range(maximum=10)
    .with_units(units.VOLT)
)
def phase_voltage(test):
    test.measurements.voltage = 5.3

@htf.measures(
    htf.Measurement("memory")
    .equals(8)
    .with_units(units.GIGABYTE)
)
def phase_memory(test):
    test.measurements.memory = 8

def main():
    test = htf.Test(phase_voltage, phase_memory)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()

