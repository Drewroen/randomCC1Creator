This repo allows you to download all CC1 dat files from Gliderbot, and also create a random level set based on the downloaded DAT files. It's intended for a potential competitive Chip's Challenge tournament.

Still WIP, likely a couple issues.

Features:
* Pulls from GliderBot, if files are already downloaded, it doesn't try again
* Creates a random set of levels, with the first level being a basic free win level to allow for easy loading
* Sets the password of all levels to `AAAA`

To download all GliderBot level sets:
* ``` pip install -r requirements.txt ```
* ``` python .\cc1DatDownloader.py ```

To create a random DAT:
* ``` python .\cc1DatCreator.py ```
