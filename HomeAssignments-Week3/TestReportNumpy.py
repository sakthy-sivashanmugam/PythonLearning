import numpy as np

class TestReport:
   def __init__(self,execution_times=None):
       if execution_times is None:
           self.execution_times = np.array([])
       else:
           self.execution_times = np.array(execution_times)

   def average_time(self):
        return np.mean(self.execution_times)
   
   def max_time(self):
        return np.max(self.execution_times)
   
   
class RegressionReport(TestReport):
   
    def slow_tests(self,threshold):
        slow= self.execution_times[self.execution_times > threshold]
        return slow
      
if __name__ == "__main__":
    execution_times = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7, 0.8, 0.9, 1.0])
    report = RegressionReport(execution_times)
    print("Average Execution Time:", report.average_time())

    print("Max Execution Time:", report.max_time())

    threshold = 0.5
    print(f"Tests taking more than {threshold} seconds:", report.slow_tests(threshold))