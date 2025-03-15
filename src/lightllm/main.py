from crewai.flow.flow import Flow,start,listen
import time


class SimpleFlow(Flow):

    @start()
    def function1(self):
        print("Function 1 started")
        time.sleep(3)
    @listen(function1)
    def function2(self):
        print("Function 2 started")
        time.sleep(2)
    
    @listen(function2)
    def function3(self):
        print("Function 3 started")


def kickoff():
    obj = SimpleFlow()
    obj.kickoff()

