import openhtf as htf
import random
import time
from datetime import datetime

"""
OpenHTF is designed to separate test logic from reporting. The best way to
print durations is to add a callback that runs after the test finishes. The
test_record contains a list of phases, each with a start_time_millis and
end_time_millis.

"""

def print_phase_durations(record):
  for phase in record.phases:
    duration_s = (phase.end_time_millis - phase.start_time_millis) / 1000.0
    print(f"Phase '{phase.name}' took {duration_s:.3f} seconds.")


@htf.PhaseOptions(timeout_s=11)
def phase_pass(test):
  current_datetime = datetime.now()
  current_timestamp = current_datetime.timestamp()
  print(f'time start: {current_timestamp} {current_datetime}') 
  time.sleep(10)

  current_datetime = datetime.now()
  current_timestamp = current_datetime.timestamp()
  print(f'time end: {current_timestamp} {current_datetime}') 
 
  return htf.PhaseResult.CONTINUE


@htf.PhaseOptions(repeat_limit=5) # Retries up to 3 times in case of failure
def phase_retry(test):

  choice = random.choice([True, False])
  print(choice)
  if choice:
    return htf.PhaseResult.CONTINUE
  else:
    return htf.PhaseResult.REPEAT


def main():
  test = htf.Test(phase_pass, phase_retry)

  # add Output callback (cleanest way) here!
  test.add_output_callbacks(print_phase_durations)

  test.execute(lambda: "SN1234")

if __name__ == '__main__':
    main()
