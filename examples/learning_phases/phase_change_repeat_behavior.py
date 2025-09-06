import openhtf as htf
import random

@htf.PhaseOptions(force_repeat=True, repeat_limit=3)
def repeat_phase(test):
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(repeat_on_timeout=True)
def timeout_phase(test):
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(stop_on_measurement_fail=True)
def random_fail_phase(test):
    if random.choice([True, False]):
        return htf.PhaseResult.CONTINUE
    else:
        return htf.PhaseResult.STOP

# This test won't be run if random_fail_phase is FAIL.
def always_true_phase(test):
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(repeat_phase, timeout_phase, random_fail_phase, always_true_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
