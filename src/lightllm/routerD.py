
from crewai.flow.flow import Flow, start, listen , router
import random
from pydantic import BaseModel


class ExampleState(BaseModel):
    success_flag  : bool = False


class RouterFlow(Flow[ExampleState]):

    @start()
    def start_method(self):
        
        self.state.success_flag = random.choice([True, False])

    @router(start_method)
    def second_method(self):
        if self.state.success_flag:
            return "success"
        else:
            return "failed"

    @listen("success")
    def third_method(self):
        print("Third method running")

    @listen("failed")
    def fourth_method(self):
        print("Fourth method running")



def kickoff():
    obj = RouterFlow()
    obj.kickoff()
    