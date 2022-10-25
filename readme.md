# VidGen

VidGen is a fun tool written with python that uses OpenAI to generate video scripts. 
It then fetches images from Google Images and other stock video sites and uses Google Cloud TTS to make *interesting* videos!

Try it out yourself!

# Installation

Python to be installed: https://www.python.org/downloads/
Visual Studio Code: https://code.visualstudio.com/download

## MacOS:

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

## Windows:

python3 -m venv env

env\Scripts\activate

pip install -r requirements.txt

## API Keys you will need

Review example_env_file for all the API keys you will need

# OPENAI

Get API keys from: https://beta.openai.com/account/api-keys

Free trial users: 20 requests/minute and 400 requests per hour.

# PEXELS

Get API keys from: https://www.pexels.com/api/new/

By default, the API is rate-limited to 200 requests per hour and 20,000 requests per month.

# STORYBLOCKS

It's not free. 35$ per month.

# Google Cloud TTS

Visit https://console.cloud.google.com/ to get API keys.

1. Create new project
2. Go to project dashboard
3. Go to project settings
4. Go to service accounts
5. Click "Create new service account"
6. Give a name to your account and click "Create"
7. Click on service account name that you just created.
8. Go to "Keys"
9. Click on "Add Key" and "Create New Key"
10. Select "JSON" from popup and click "Create"
11. This will download a json file in your computer. Copy the path of this file and paste it in .env file.

## How To Generate A Video

1. If you are on a Mac you can double click on VidGen.command
2. If you are not on a mac, cd to the repo directory in your terminal and run "python gui.py"
3. After some set up (that you can monitor in terminal) a GUI will pop up.
4. Mix and match your video options
5. Once you are happy, hit Generate Resources
6. After the resources are done generating, review the generated files (script, images, etc)
7. If it all looks good, hit Create Movie to actually render the .mp4 file
8. Optional: For a more realistic voice experiment with using the google TTS options

python3 gui.py (on Mac)
python gui.py (on Windows)