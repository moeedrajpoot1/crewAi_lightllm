from crewai.flow.flow import Flow, start, listen

from litellm import completion
import time


API_KEY = 'AIzaSyAOB_3aOGS7atDLQTwMBbR-hh9xdd4GFK8'

class cityFunFact(Flow):
     @start()
     def generate_random_city_name(self):
          result=completion(
               model = "gemini/gemini-1.5-pro",
               api_key = API_KEY,
               messages= [{"content":"any one famous animal name","role":"user"}]
          )
          city_name = result["choices"][0]["message"]["content"]
          print(city_name)
          return city_name
        
     @listen(generate_random_city_name)
     def generate_fun_fact(self,city_name):
          
          result=completion(
               model = "gemini/gemini-2.0-flash-exp",
               api_key = API_KEY,
               messages= [{"content":f"write some fun fact about{city_name} city ","role":"user"}]
          )
          fun_fact = result["choices"][0]["message"]["content"]
          print(fun_fact)
          self.state['fun_fact']= fun_fact
     

     @listen(generate_fun_fact)
     def save_fun_fact(self):
          with open ('fun_fact.md','w') as file :
               file.write(self.state["fun_fact"])
               return self.state["fun_fact"]
          
          
     

def kickoff():
     obj = cityFunFact()
     result = obj.kickoff()
     print(result)
