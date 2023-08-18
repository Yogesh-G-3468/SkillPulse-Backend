import openai
from openai.error import OpenAIError
import re 
import os
from dotenv.main import load_dotenv
import logging
import inspect

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

 # take environment variables from .env.


class Evaluate:

    def __init__(self,subject,avilable_answers) -> None:
        self.subject = subject
        self.avilable_answers = avilable_answers
        self.indi_mark = [0 for i in range(15)]
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        logger.info("Evaluate object created")

    def generate_chat_response(self,prompt):
        load_dotenv()
        openai.api_key = os.getenv('KEY')
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
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
        
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        n=1
        actual_answers ={
            "dbms":
        {
            "1": "Database is a collection of data in some organized way to facilitate its users to easily access, manage and upload the data.",
            "2": "Normalization is the process of analyzing the relational schemas which are based on their respective functional dependencies and the primary keys in order to fulfill certain properties.",
            "3": "A primary key is a special field or set of fields that uniquely identify each record in a table. It ensures that each row in the table has a distinct identity and no two rows can have the same primary key value. The primary key is used to establish relationships between tables, enforce data integrity, and provide a quick way to locate specific records.",
            "4": "In database design, denormalization involves intentionally introducing redundancy into a table structure. This can improve query performance but may lead to data integrity challenges.",
            "5": "A foreign key is a field in one table that refers to the primary key in another table. It establishes a link between the data in two tables, enabling the creation of relationships.",
        },

            "cn": 
        {
            "1": "DNS stands for Domain Name System, and it is a fundamental technology used to translate human-readable domain names into IP addresses. It is used in daily life for efficient browsing, caching, and load balancing.",
            "2": "A firewall is a network security device or software that acts as a barrier between a trusted internal network and untrusted external networks. Its primary purpose is to monitor, filter, and control network traffic based on security rules.",
            "3": "The internet and the web are not the same thing. The internet is a global network of computers, while the web is a way of accessing information on the internet.",
            "4": "Network topology refers to the physical or logical arrangement of devices within a network. Common topologies used in college labs include the star topology.",
            "5": "A proxy server is an intermediate server that sits between a client device and a destination server. It provides anonymity and privacy by acting as a gateway and forwarding requests.",
            "6": "Yes, most routers contain a switch inside them. The switch connects different ports on the router to allow devices on the same network to communicate.",
            "7": "Peer-to-peer is a networking model where each computer acts as both a client and a server. BitTorrent is a P2P file-sharing system that allows users to share files directly.",
            "8": "Load balancing distributes traffic across multiple servers to improve performance and reliability.",
            "9": "Yes, data can be shared between systems without the web. Peer-to-peer file sharing, direct file sharing, and shared network file sharing are some ways to do it.",
            "10": "User Datagram Protocol (UDP) is a transport protocol used for sending data between devices. UDP improves online gaming performance due to its low latency, faster data transmission, and reduced congestion.",
            "11": "Data in different OSI layers is referred to as bit, frame, packet, and segment.",
            "12": "Caching involves storing copies of web resources locally to reduce the need for fetching from the original server and improve page load times.",
            "13": "Bandwidth refers to the maximum data transmission over a network connection. Higher bandwidth does not guarantee faster data speed.",
            "14": "\"Ping\" is a network utility to test the reachability of a host and measure round-trip time. Lower ping is preferred for better speed.",
            "15": "The OSI model is a reference model and is not implemented in real life. It is used as a reference for building other models."
        }
}


        
        
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
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
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

        
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        for x in range(len(scores[0])):
            self.indi_mark[int(self.avilable_answers[x])-1] += int(scores[0][x]) 
        

        print("this iss the problem ------->",self.indi_mark)

        if self.subject == "dbms":
            final_score = {
                "Joins":0,
                "Normalization":0,
            }

            for i in range(len(scores[0])):
                if i < 3:
                    final_score['Joins'] += ((int(scores[0][i])/30)*100)
                elif i >= 3 and i < 6:
                    final_score['Normalization'] += ((int(scores[0][i])/30)*100)
        
        if self.subject == "cn":
            final_score = {
                "application level concepts":0,
                "hardware concepts":0,
                "generic questions":0,
                "data transporation":0,
                "understanding of basic terminologies":0,
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

        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
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
  


