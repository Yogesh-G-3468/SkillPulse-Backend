import openai
from openai.error import OpenAIError
import re 


class AIresponse:
    def generate_chat_response(self,prompt):

        openai.api_key = 'your api'
        try:
            # Create a completion request with the specified engine, prompt, and max tokens.
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': 'user', 'content': prompt}],
                max_tokens=1024
            )
            return response.choices[0].message.content

        except OpenAIError as error:
            # Handle API errors.
            error_message = error.__class__.__name__ + ': ' + str(error)
            print('API Error:', error_message)
            return None

        except Exception as e:
            # Handle other exceptions.
            print('Exception:', str(e))
            return None


    def generate_prompt(self,subject, questions):
        
        n=1
        actual_answers ={
                        "DBMS": [
                            {
                              1:"Database is a collection of data in some organized way to facilitate its users to easily access, manage and upload the data.",
                              2:"Normalization is the process of analyzing the relational schemas which are based on their respective functional dependencies and the primary keys in order to fulfill certain properties."
                
                              }
                          ]
                        }

        
        
        prompt = """task 1 : I will give you 2 sets of pair of  sentences that must be compared as input, i want you to give me output only in the format I am describing. I dont want anything else as the output.". 

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



        for i in questions[subject][0]:
            q = questions[subject][0][i]
            a= actual_answers[subject][0][i]
            
            para1="\nset "+str(n)+"\n"+"\nsentence 1:"+a+"\n"
            para2="sentence 2:" +q+"\n"
            prompt+=para1+para2+"\n"
            n+=1
        
        return prompt


    def extraction(self,input_text):

        pattern = r'<rating>(.*?)<\/rating>'
        pattern2= r'<strong>(.*?)<\/strong>'
        pattern3= r'<weak>(.*?)<\/weak>'
        pattern4= r'<suggest>(.*?)<\/suggest>'
        scores=[]
        scores.append(re.findall(pattern, input_text))
        scores.append(re.findall(pattern2, input_text))
        scores.append(re.findall(pattern3, input_text))
        scores.append(re.findall(pattern4, input_text))
        return scores
    
    def jsonify(self,scores):
      output={}
      
      for i in scores:
          output["DBMS"]={}
          for j in range (1,len(i)+1):
            output["DBMS"][j]={}
      a=1
      for subscore in zip(scores[0],scores[1],scores[2],scores[3]):
        output["DBMS"][a]=list(subscore)
        a+=1
      return output
                






if __name__ == '__main__':
# Example usage.
    user_prompt = {
          "DBMS": [
            {
              1:"It is a collection of string in some organized way to facilitate its users to easily delete, manage and upload the files.",
              2:"Normalization is used to normalize the tables or combine values that are similar based on the requirement"
                
              }
          ]
    }

    ai = AIresponse()

    prompt=ai.generate_prompt("DBMS",user_prompt)
    scores=ai.extraction(ai.generate_chat_response(prompt))
    print(ai.jsonify(scores))

#print(prompt)
# print(x:=generate_chat_response(prompt))
# input_text = x

# pattern = r'<rating>(.*?)<\/rating>'
# pattern2= r'<strong>(.*?)<\/strong>'
# pattern3= r'<weak>(.*?)<\/weak>'
# pattern4= r'<suggest>(.*?)<\/suggest>'
# matches = re.findall(pattern, input_text)
# matches2 = re.findall(pattern2, input_text)
# matches3 = re.findall(pattern3, input_text)
# matches4 = re.findall(pattern4, input_text)


# print(matches)
# print(matches2)
# print(matches3)
# print(matches4)
  


