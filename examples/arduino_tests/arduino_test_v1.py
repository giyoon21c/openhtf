import openhtf as htf

@htf.measures(htf.Measurement("P4_digital")
              .doc("Pin 4 Digital Measurement")
              .equals(False))
def digital_read(test):
    test.measurements.P4_digital = False 

test = htf.Test(digital_read)
test.execute()
