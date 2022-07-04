'''
Author: Vincent Young
Date: 2022-07-04 01:02:39
LastEditors: Vincent Young
LastEditTime: 2022-07-04 18:43:44
FilePath: /Sync-Weibo-Twitter/ifttt.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
#!/usr/bin/env python3

import datetime
import weibo
import requests
import json
import os

class Ifttt(object):
	
	def __init__(self, path, event_name, key):
		self.path = path
		self.event_name = event_name
		self.key = key
		self.text = []
		self.image = []
		self.num = 0
		self.id = []
		
	# Parsing JSON file
	def parse_post_info(self, path):
		with open(path, 'r', encoding='UTF-8') as f:
			json_data = json.loads(f.read())
			for post in json_data['weibo']:
				self.num += 1
				self.text.append(post['text'])
				self.id.append(post['id'])
			print("JSON File Weibo Numbers: ", self.num)
			# print(self.text)
			# print(self.id)
	

	# Send to IFTTT
	def send_notice(self):
		url = f"https://maker.ifttt.com/trigger/{self.event_name}/with/key/{self.key}"
		for num in range(0, self.num):
			with open("./ifttt_record.txt","r", encoding='UTF-8') as ifttt_record_file:
				send_ids = ifttt_record_file.readlines()
				for send_id in send_ids:
					# print(send_id.)
					if str(self.id[num]) == send_id.strip().replace("\n",""):
						print("This Weibo has been send to IFTTT")
						return
				payload = {"value1": self.text[num]}
				headers = {"Content-Type": "application/json"}
				response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
				# print(payload)
				# Log the request
				with open("./ifttt_record.txt","a") as ifttt_record_file:
					ifttt_record_file.write(str(self.id[num]) + "\n")
					print("Send to IFTTT: ", self.text[num])
					ifttt_record_file.close()
				ifttt_record_file.close()


def main():
	starttime = datetime.datetime.now()
	# Run Weibo Crawler
	config = weibo.get_config()
	wb = weibo.Weibo(config)
	wb.start() 
	path = './weibo/YOURWEIBONAME/YOURWEIBOID.json' # Weibo Crawler JSON File
	event_name = 'XXX' # Webhooks Event Name
	key = 'XXX' # Webhooks Key
	ifttt = Ifttt(path, event_name, key)
	ifttt.parse_post_info(path)
	ifttt.send_notice()
	os.remove(path) 
	endtime = datetime.datetime.now()
	print("Total Running Time: ", endtime - starttime)
	
if __name__ == '__main__':
	main()