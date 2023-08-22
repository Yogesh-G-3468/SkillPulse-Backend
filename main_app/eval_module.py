import openai
from openai.error import OpenAIError
import re 
import os
from dotenv.main import load_dotenv
import logging
import inspect
from .answers import actual_answers

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs.log"),
    ],)

 # take environment variables from .env.


class Evaluate:

    def __init__(self,subject,avilable_answers) -> None:
        self.subject = subject
        self.avilable_answers = avilable_answers
        self.indi_mark = [0 for i in range(15)]
        logger = logging.getLogger("Evaluate")
        logger.info("Evaluate object created")

    def generate_chat_response(self,prompt):
        load_dotenv()
        openai.api_key = os.getenv('KEY')
        logger = logging.getLogger("generate_chat_response")
        try:
            # Create a completion request with the specified engine, prompt, and max tokens.
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': 'user', 'content': prompt}],
                max_tokens=1024
            )
            logger.info("GPT-3 response generated")
            return response.choices[0].message.content

        except OpenAIError as error:
            # Handle API errors.
            error_message = error.__class__.__name__ + ': ' + str(error)
            print('API Error:', error_message)
            logger.error(error_message)
            return None

        except Exception as e:
            # Handle other exceptions.
            print('Exception:', str(e))
            logger.error(str(e))
            return None


    def generate_prompt(self,questions):
        
        logger = logging.getLogger("generate_prompt")
        n=1
         
        prompt = """task 1 : I will give you many sets of pair of  sentences that must be compared as input, i want you to give me output only in the format I am describing. I dont want anything else as the output.". 

        task 2: I will give you 2 sets of pair of  sentences .I want you to take only the sentence 2 and give me all the tags(single letter concepts) that i am strong at inside the <strong></strong> tag and things i am weak at inside <weak></weak> tag, it must be array of words inside both the tags.i want you to give me output only in the format I am describing. I dont want anything else as the output. I will fill the space in the output where you must insert your output value as "{}".

        task 3: Give me an suggestion on what to learn and how to learn to improve my knowledge based on my answer in sentence 2. give it in <suggest></suggest> tag

        DO'S:
        1)output only in the format i specify
        2)output range from 1 to 10
        DONT'S
        1)Any other text other than the specified output 
        2)No explination and reasoning
        3)no assurance texts like "Understood. Here's the output in the exact format you described, based on the input sentences you provided:"

        sample output  for each sets:
        <rating></rating>
        <strong>[]</strong>
        <weak>[]</weak>
        <suggest>{}</suggest>\n Input : \n"""



        for i in questions[self.subject]:
            if questions[self.subject][i] == "":
                continue
            else:
                q = questions[self.subject][i]
                a = actual_answers[self.subject][i]
                
                para1="\nset "+str(n)+"\n"+"\nsentence 1:"+a+"\n"
                para2="sentence 2:" +q+"\n"
                prompt+=para1+para2+"\n"
                n+=1
        
        logger.info("prompt for the AI generated")
        return prompt


    def extraction(self,input_text):
        logger = logging.getLogger("extraction")
        pattern = r'<rating>(.*?)<\/rating>'
        pattern2= r'<strong>(.*?)<\/strong>'
        pattern3= r'<weak>(.*?)<\/weak>'
        pattern4= r'<suggest>(.*?)<\/suggest>'
        scores=[]
        scores.append(re.findall(pattern, input_text))
        scores.append(re.findall(pattern2, input_text))
        scores.append(re.findall(pattern3, input_text))
        scores.append(re.findall(pattern4, input_text))

        logger.info("scores extracted from the AI generated response")
        return scores
    
    def calculate_percentage(self,scores):

        
        logger = logging.getLogger("calculate_percentage")
        for x in range(len(scores[0])):
            self.indi_mark[int(self.avilable_answers[x])-1] += int(scores[0][x]) 
        

        print("this iss the problem ------->",self.indi_mark)

        if "dbms" in self.subject:
            final_score = {
                "Relational Databases":0,
                "Database Design":0,
                "Transactions and Concurrency":0,
                "Data Storage and Querying":0,
                "Advanced topics":0,
                "totalMarks": 0
            }

            for i in range(len(scores[0])):
                if i < 3:
                    final_score['Joins'] += ((int(scores[0][i])/30)*100)
                elif i >= 3 and i < 6:
                    final_score['Normalization'] += ((int(scores[0][i])/30)*100)
        
        if "os" in self.subject:
            final_score = {
                "Operating System Overview":0,
                "Process Management":0,
                "Storage Management and File System":0,
                "I/O Systems":0,
                "Case Study":0,
                "totalMarks": 0
            }
            
        if "cn" in self.subject:
            final_score = {
                "Introduction and Physical layer":0,
                "Data link layer and LAN":0,
                "Network and Routing":0,
                "Transport layer":0,
                "Application layer":0,
                "totalMarks": 0
            }

            for i in range(len(self.indi_mark)):
                if i < 3:
                    final_score['application level concepts'] += ((int(self.indi_mark[i])/30)*100)
                elif i >= 3 and i < 6:
                    final_score['hardware concepts'] += ((int(self.indi_mark[i])/30)*100)
                elif i >= 6 and i < 9:
                    final_score['generic questions'] += ((int(self.indi_mark[i])/30)*100)
                elif i >= 9 and i < 12:
                    final_score['data transporation'] += ((int(self.indi_mark[i])/30)*100)
                elif i >= 12 and i < 15:
                    final_score['understanding of basic terminologies'] += ((int(self.indi_mark[i])/30)*100)
                else:
                    pass
                
        logger.info("final score calculated")
        return final_score
        
    

    
    def jsonify(self,scores):

        logger = logging.getLogger("jsonify")
        output={}
        
        for i in scores:
            output[self.subject]={}
            for j in range (1,len(i)+1):
                output[self.subject][str(j)]={}
        a=0
        for subscore in zip(scores[0],scores[1],scores[2],scores[3]):
            print("this is subscoree ------>",subscore)
            suggest={"rating":subscore[0],
                     "Strength":subscore[1],
                     "Weak":subscore[2],
                     "Suggestion":subscore[3]}
            output[self.subject][str(self.avilable_answers[a])]=suggest
            a+=1
        
        final_score = self.calculate_percentage(scores)
        output['final_score'] = final_score

        logger.info("jsonified output generated")
        return output
  


