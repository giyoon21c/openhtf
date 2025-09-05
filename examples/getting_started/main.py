import openhtf as htf

@htf.measures(
    htf.Measurement("greeting_message").with_validator(
      lambda msg: "Hello" in msg
    )
)

@htf.PhaseOptions(timeout_s=5)
def hello_world_with_measurement(test):
  #message = "Hello world!"
  message = "xello world!"
  print(message)
  test.measurements.greeting_message = message

#def hello_world(test):
#  print("hello openHTF")
#  return htf.PhaseResult.CONTINUE

def main():
  test = htf.Test(hello_world_with_measurement)
  test.execute(lambda: "SN1234")

if __name__ == "__main__":
  main()