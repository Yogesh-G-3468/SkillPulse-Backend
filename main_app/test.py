import requests

# Define the URL of the server
url = "http://127.0.0.1:8000/api/GetRating/"
url2 = "http://127.0.0.1:8000/api/greeting/"

# Define the JSON payload

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token 269faeaf2fa196a32300844362abf4d8d53a5fd2"
  }

payload = {
  "UserAnswer": 
    {
      "DBMS": 
        {
          "1": "It is a collection of data in some structured manner to enable users to easily access, manage, and store information.",
          "2": "Normalization is employed to standardize database tables or merge values that exhibit similarities based on specified criteria.",
          "3": "The primary key serves as the anchor for a composition. Just as a song revolves around its central theme, a primary key secures the database journey.",
          "4": "Indexes are data structures used to optimize data retrieval speed in a table, working akin to book indexes.",
          "5": "A foreign key is a field that refers to the primary key in another table, creating links between related data.",
          "6":"Leave me alone i dono anything"
        }
    }
}

# Send the POST request
# response = requests.post(url, json=payload)

# # Print the response content
# print(score:=response.json())

# score_val = score['scores']['DBMS']
# for x in score_val:
#     print("Rating:",score_val[x][0])
#     print("Strong:",score_val[x][1])
#     print("Weak:",score_val[x][2])
#     print("Suggest:",score_val[x][3])
# print(score['final_score'])

response = requests.get(url2,headers=headers)

print(response.json())
