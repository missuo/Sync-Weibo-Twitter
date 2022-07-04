# Sync Weibo To Twitter
An automatic real-time Weibo Twitter synchronization tool

## Features
- Real-time Weibo Twitter synchronization
- No need to update cookies
- There is no charge, except for the server
- Images will not sync

## Usage
1. You should first register an `IFTTT` account.

2. You need to create a new application, `Webhooks` to `Twitter`. 

![4c98f38d73b3b27c2fd3a](https://telegraph.eowo.us/file/4c98f38d73b3b27c2fd3a.png)

3. You need to write down the KEY of `Webhooks` and authorize your `Twitter`.

4. Git Clone this project to your server.

5. Change the `config.json` file. Modify the third line of your `Weibo ID`.

~~~json
"user_id_list": [
        "123456"
    ],
~~~

6. Change the `ifttt.py` file. Modify the line 72-74.
~~~
	path = './weibo/YOURWEIBONAME/YOURWEIBOID.json' # Weibo Crawler JSON File
	event_name = 'XXX' # Webhooks Event Name
	key = 'XXX' # Webhooks Key
~~~

7. Installing the Python environment
~~~shell
pip3 install -r requirements.txt
~~~

8. Run the `ifttt.py` file. Add to Corntab.
~~~shell
python3 ifttt.py
~~~

## Reference Articles
[微博 API 失效后 IFTTT 同步微博到 Day One 方法](https://sspai.com/post/67334)

## Open Source Projects Used
[dataabc/weibo-crawler](https://github.com/dataabc/weibo-crawler)

## License
MIT License