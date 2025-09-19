import numpy as np

class ManualTester:
   
   def analyze(self, data):
        print("ManualTester-First 5 Execution Times:", data[:5])

class AutomationTester:
   
   def analyze(self, data):
        print("AutomationTester- Faster Execution Time:", np.min(data))

class PerformanceTester:
    
    def analyze(self, data):
          print("PerformanceTester- 95th Percentile Execution Time:", np.percentile(data, 95))

def show_analysis(tester, data):
    tester.analyze(data)

if __name__ == "__main__":
    execution_times = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    
    manualtester = ManualTester()
    automationtester = AutomationTester()
    performancetester = PerformanceTester()

    show_analysis(manualtester, execution_times)
    show_analysis(automationtester, execution_times)
    show_analysis(performancetester, execution_times) 