# notion-tools
Scripts to help with Notion

All Scripts require python >= 3.6 and the requests module.
You may need to install it with pip install requests.

Then copy config.py.example to config.py and edit it.
Insert the ID of your Tasks Database,
You get the secret when you create a notion integration. Please do so and add it as well.


## add_tasks.py
Script to add Tasks to Thomas Frank's Notes System in Notion.
You can directly pass a Task to the command line using:
./add_task.py -t "My fancy Task"
This is useful e.g. for Apple  Shortcuts

Or use -i to paste multiline tasks, or -f to specify a file.
For Files and Paste, you will need Markdown syntax, which means every line starting with - is threaded as task.
 So, you can directly use your meeting notes to extract the tasks you wrote down.
 
## get_all.py
Get all Tasks, only for API Debug.
