# drip_garden_autocompounder_v2
V2 of the compounder using selenium / undetected chromedriver


I will be updating this with more complete information, but wanted to get out the ALPHAAAA ALPHA version for those tech savvy and who are up for minor debugging

Install the necessary python packages ( pip install ) google how to do this if you are not sure 
  - selenium
  - getpass
  - undetected chromeriver
  
  
You will need to use / specify a user profile for chrome. I specified this as profile 1, but you can change this path to whatever you want in the code. This is so that this bot can use a defined profile instead of creating a temporary one each time.
This is required because you need to have credentias in MM 

So the first time you run this program, you will need to set up a few things:
  - Use the profile specificed in the program, or change it if you want, and add in your MM credentials and restore your wallet using your seed phrase
  - You will then set a password, and you will want to update the script 'YOUR PASSWORD HERE' with the pasword you choose
  - Another thing you will need to do manually, is the first time you connect to MM with this profile and navigate to the MM tab, you will need to manually click OK on the popup
        (this is a one time thing, so i didn't automate it)

This is all the setup that should be needed.

I will give more detailed instructions, but this should be all that is needed if you are computer savvy to get going.


Note: I used a specific version of chromedriver because this program kept getting blocked by cloudflare antibot detection


This is alpha alpha, so if you have any weird issues, let me know and I can try to help work through them
