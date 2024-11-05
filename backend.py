import requests
api_key = "wkQhVfpxgjqeagWqQxSCFLUK4KL4gYBvNB8ftphu59410f9a"
url = "https://teachgpt.ssis.nu/api/v1/chat/completions"
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {api_key}",
}
payload = {
"model": "Meta-Llama-3.1-70B",
"messages": [
{
"role": "system",
"content": "You are a helpful assistant."
},
{
"role": "user",
"content": "Hello!"
}
]
}
response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
    print("Success:")
    print(response.json())
else:
    print("Error:")
    print(response.text)