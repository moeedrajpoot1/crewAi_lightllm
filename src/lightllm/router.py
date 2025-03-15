from crewai.flow.flow import Flow, start, listen , router
import random

class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Assalamo-Alaikum")

    @router(greeting)
    def select_city(self):
        cities = ["karachi" , "lahore" , "multan"]
        select_city = random.choice(cities)
        print(f"Selecting city: {select_city}")

        self.state['select_city']= select_city
        if self.state['select_city'] == "karachi":
            return "karachi"
        if self.state['select_city']== "lahore":
            return "lahore"
        if self.state['select_city']== "multan":
            return "multan"
    @listen("karachi")
    def f1(self):
        print(f"write some fun fact about { self.state['select_city']}")
        

    @listen("lahore")
    def f2(self):
        print(f"write some fun fact about { self.state['select_city']}")
        return f"write some fun fact about { self.state['select_city']}"
    
    @listen("multan")
    def f3(self):
        print(f"write some fun fact about { self.state['select_city']}")
        return f"write some fun fact about { self.state['select_city']}"








def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot():
    obj = RouteFlow()
    obj.plot()