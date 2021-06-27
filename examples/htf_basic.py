import openhtf as htf


#
# use of validator
# 
@htf.measures(htf.Measurement("P4_digital")
              .doc("Pin 4 Digital Measurement")
              .equals(True))
def digital_read(test):
  #test.measurements.P4_digital = False
  test.measurements.P4_digital = True 

if __name__ == "__main__":
  test = htf.Test(digital_read)
  test.execute()

