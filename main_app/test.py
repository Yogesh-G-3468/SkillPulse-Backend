import requests

# Define the URL of the server
url = "http://127.0.0.1:8000/api/GetRating/"

# Define the JSON payload
payload = {
    "UserAnswer": [
        {
            "DBMS": [
                {
                    "1": "It is a collection of string in some organized way to facilitate its users to easily delete, manage and upload the files.",
                    "2": "Normalization is used to normalize the tables or combine values that are similar based on the requirement",
                    "3": "the primary key sets the tone for a piece. Just as a melody revolves around its central note, a primary key anchors the musical journey"
                }
            ]
        }
    ]
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response content
print(score:=response.json())

score_val = score['scores']['DBMS']
for x in score_val:
    print("Rating:",score_val[x][0])
    print("Strong:",score_val[x][1])
    print("Weak:",score_val[x][2])
    print("Suggest:",score_val[x][3])

