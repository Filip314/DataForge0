# Dataforge
## What is DataForge?
**DataForge** is a website that acts as a market for closed-source software. Third party developers, individuals or even artists can upload their files or directories on our website and we will make them availible to end-consumers for the price you set.

## Prototype
This is a working protatype that is still missing many of the final intended features. It serves as a demonstration of our website functionality. Because this in not the final version, you can't directly access it by just typing the URL in your browser. More about this in the **Setup** section

## Languages and programmes used:
- **Webnode CMS** - A website editor that made the main framework for our website
- **Python** - The main programming language of the website
- **Flask** - Python-based library that enables the website to run on a local machine acting as a server.
- **SQLite 3** - A Python library for editing `.db` files

 ## Setup
 **!This guide assumes you have a Linux based OS!**
 
 As this is just a prototype, the website doesn't run on the world wide web yet, and it is a bit more complex to get it running. Here is a step-by-step guide:
 - Make sure you have **Python** installed on your PC
 - Install libraries necessery for running the code: `Flask`, `sqlite3` *(should already come preinstalled with Python)*, `render_template`
 - Download the `website` directory from our GitHub
 - Run your computer as a server for the website by typing: `python3 ~/website/app.py` in the terminal. In case your system didn't find the file, look where your computer stored the directory and change the path accordingly.
 - After running `app.py`, there should be the website URL displayed in the terminal. Copy it and run it in your browser.
 - That's it! You should now be able to access the website. Note that as the website is running localy on your PC, you won't be able to access it outside of the same network. Your computer should only provide server service when `app.py` is actively running.

## Navigating the website
DataForge is devided into several categories that you can switch using the top bar. Most categories represent different types of software, e. g. **Documents**, **Images** and **Other software**. You can also navigate to our contact info using the top bar again, in case you had any questions. There is also a waiting list that displays the queue of top 5 applications that are waiting to be approved by our moderator team.

## Contributing
Anyone can post images or directories on our website and choose their price. If you want to add something to sell, please fill the form on our homepage. You will then soon be contacted by our moderator team to discuss adding your application. 
