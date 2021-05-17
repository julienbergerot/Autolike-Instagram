# Autolike
This simple project is an Instagram autoliker. It will go through your feed and like all the posts you did not already liked. Follow the procedure to make it work.

# Installation
All of this work has been done on Chrome but is easly ajustable to other browsers such as Firefox or Explorer.

You need to install a few things :
* selenium
* a web driver (unique for each browser), and can be download following this [page](https://selenium-python.readthedocs.io/installation.html)

After the web driver is downloaded, you need to add it to your path. For example, create a folder `C://WebDriver/bin`, put your *chromedriver.exe* in it and add this folder to your path.
Reboot your computer and this step should be done. You can check if this has been done correctly by doing the following in the command line. Something shoudl show up.
```bash
chromedriver
```

# Configure your account
To remember who you are, you need to specify your Chrome account. Open Chrome, type *chrome://version* in the search bar. Find the variable Profile Path. It should look like *C://Users/{username}/AppData/Local/Google/Chrome/User Data/Default*. Copy this value in the options.py file, where it is said to.

Open a new command line, and run :
```bash
python configure_browser.py
```
A page should open. Accept the cookies and log into your instagram account. This permits the program to load the connected page the following times.
Comme back to you command line and enter to save this.

# Configure the pattern recognition
Run the jupyter notebook called *Find your pattern*. There is also a result in the `data` folder, but it may not work on your computer. Do not forget to change the options.py file as requested in the notebook.

# Run the autoliker
All the calibration are done for my computer so it may not work correctly on yours. You may need to adapt the options.py file, the *mouse_to_browser* function.
To run the program, simply :
```bash
python autolike.py
```
Until it found 10 already liked pictures, it will keep on liking. You can add a limit of likes by adding a number as argument in the command line.
```bash
python autolike.py {max_number_of_likes}
```

# Autofollow part

This part find all your followers and followees. It simply store their username in a file, according to their category. If they are ghosts (follow but do not like), if you did not follow them back or if they did not follow you back.
This will be store in a daily folder when you run 
```bash
python storeData.py
```

As for the pattern recognition, an another pattern is required to unfollow people. Just follow the *ipynb* file, and all is explained. You might also need to find the SEARCH,ENTER and CONFIRM position (the *mouse.py* file is here to help).

Once this is done, you can run 
```bash
python find.py
```

***Becareful, this is a project done for fun but you may get banned from Instagram if you use it too much !***