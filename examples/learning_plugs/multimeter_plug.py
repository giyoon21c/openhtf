from openhtf import plugs
import random

class MultimeterPlug(plugs.BasePlug):
  def __init__(self):
    # Simulate connecting to the multimeter
    self.connected = True

  def tearDown(self):
    # Automatically called by OpenHTF after the test to clean up
    self.connected = False

  def measure_voltage(self):
    # Simulate voltage measurement
    return random.uniform(0, 10)

  def measure_current(self):
    # Simulate current measurement
    return random.uniform(0, 2)
