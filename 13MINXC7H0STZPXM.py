import amino
from requests import delete
from concurrent.futures import ThreadPoolExecutor
print("""\033[38;5;147m
Script by deluvsushi
Github : https://github.com/deluvsushi
╱╭╮╭━━━┳━╮╭━┳━━┳━╮╱╭┳━╮╭━┳━━━┳━━━┳╮╱╭┳━━━┳━━━┳━━━━┳━━━━┳━━━┳━╮╭━┳━╮╭━╮
╭╯┃┃╭━╮┃┃╰╯┃┣┫┣┫┃╰╮┃┣╮╰╯╭┫╭━╮┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╭╮╭╮┣━━╮━┃╭━╮┣╮╰╯╭┫┃╰╯┃┃
╰╮┃╰╯╭╯┃╭╮╭╮┃┃┃┃╭╮╰╯┃╰╮╭╯┃┃╱╰┻╯╭╯┃╰━╯┃┃┃┃┃╰━━╋╯┃┃╰╯╱╭╯╭┫╰━╯┃╰╮╭╯┃╭╮╭╮┃
╱┃┃╭╮╰╮┃┃┃┃┃┃┃┃┃┃╰╮┃┃╭╯╰╮┃┃╱╭╮╱┃╭┫╭━╮┃┃┃┃┣━━╮┃╱┃┃╱╱╭╯╭╯┃╭━━╯╭╯╰╮┃┃┃┃┃┃
╭╯╰┫╰━╯┃┃┃┃┃┣┫┣┫┃╱┃┃┣╯╭╮╰┫╰━╯┃╱┃┃┃┃╱┃┃╰━╯┃╰━╯┃╱┃┃╱╭╯━╰━┫┃╱╱╭╯╭╮╰┫┃┃┃┃┃
╰━━┻━━━┻╯╰╯╰┻━━┻╯╱╰━┻━╯╰━┻━━━╯╱╰╯╰╯╱╰┻━━━┻━━━╯╱╰╯╱╰━━━━┻╯╱╱╰━╯╰━┻╯╰╯╰╯
""")
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
	print(f"-- {x}:{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
chats = sub_client.get_chat_threads(size=100)
for z, title in enumerate(chats.title, 1):
	print(f"-- {z}:{title}")
chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]

def remove_co_host(user_id: str, nickname: str):
	response = delete(
		f"{client.api}/x{com_id}/s/chat/thread/{chat_id}/co-host/{user_id}",
		headers=client.headers).json()["api:message"]
	print(f"-- Co-Host Invite {nickname}::: {response}")
	
while True:
	with ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(0, 25000, 1500):
			try:
				online_users = sub_client.get_online_users(
					start=i, size=100).profile
				for user_id, nickname in zip(
						online_users.userId, online_users.nickname):
					[executor.submit(remove_co_host, user_id, nickname)
					 for _ in range(3)]
			except Exception as e:
				print(e)
