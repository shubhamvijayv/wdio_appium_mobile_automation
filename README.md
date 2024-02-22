# Setup for this project using linux system:

**1. we need to have Node JS installed on our local machine. This is a prerequisite for working with Appium.**

**2. Below is the command to install nodejs**

            sudo apt-get update

            sudo apt-get install nodejs

**3. Once the installation is complete, open the terminal and type the command**

            "node -v" and press enter.

**It should show the latest version of Node, confirming that node has been installed successfully on your local machine.**

**4. Next, type the command**

                npm -v

**it should show the latest version of npm installed on your machine. npm comes bundled with node and should get installed automatically with Node JS.**

**5. complition of all node setup we can install appium in our local machine.Open the terminal and type the given below command:**

            npm install -g appium

**6. To verify that the Appium was successfully installed lets check its version by typing the given below the command:**

            appium -v

## Appium Driver Installation:

**7. To install an Appium Driver, we need to run the given below command:**

*uiautomator2 driver only use for android device.*

             appium driver install uiautomator2

*xcuitest driver only use for ios device.*

             appium driver install xcuitest

**8. Appium has provided us with the following command that lists all the drivers available for download and also shows the driver that is currently installed/not installed on your local machine-**

            appium driver list

**9. Updating Appium Driver**

**Appium provides the command to check if any driver update is available. Running the following command will let you know if any driver update is available -**

            appium driver list --updates

**10. How to update individual driver using linux terminal we can update given below the command:**

            appium driver update <driver name>

## Appium-Doctor

**11. appium-doctor helps in checking that Appium and its respective dependencies has been installed correctly on the machine to start with mobile automation for Android and iOS.**

**12. For automating an Android Mobile application we need to have Android Studio installed on our machine.**

**13. To install appium-doctor run the given below command:**

              npm install -g appium-doctor


**14. we can check version of appium-doctor given below command:**

              appium-doctor --version

**15. Verify Appium Android setup using appium-doctor:**

*The following command will check the Android Setup with Appium and provide us with detailed log.*

              appium-doctor --android


__Checks like NodeJS was installed, ANDROID_HOME and JAVA_HOME environment variables are set correctly,
etc are verified and detailed logs are provided.__

__If any configuration is missing it will be provided in the logs and accordingly needs to be
fixed for Appium to be set up correctly.__

*ANDROID_HOME and JAVA_HOME and ADB set is given below:*

__1. Firstly, we can open ~/.bashrc file using given below the command:__

                          gedit ~/.bashrc

__2. after that we can set ANDROID_HOME and JAVA_HOME and ADB in ~/.bashrc file like given below:__

                               export ANDROID_HOME='/home/arcgate/Android/Sdk'

                               export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"

                               export ADB="/home/arcgate/Android/Sdk/platform-tools/adb"


__3. ANDROID_HOME and JAVA_HOME and ADB is successfully set we can press save button on ~/.bashrc file after that we can close ~/.bashrc file.__

__4. then we can run on terminal given below the command:__

                               source ~/.bashrc

__5. then we can run given below command for succesfully set on bashrc file__

                              appium-doctor --android


***If all the checks pass and there are no fix required, your Android Appium setup is configured correctly.***

**16. Verify Appium iOS setup using appium-doctor:**

***Before running Appium doctor check for iOS setup, make sure you have installed carthage package. carthage package install given below the command***

               npm install -g carthage

***To verify the Appium iOS setup, given below the command:***

               appium-doctor --ios

***If there are no mandatory fixes required as per the logs, you have configured Appium iOS successfully on your local machine.***


**17. we can inspect the element from android or ios mobile then we can use Appium Inspector.**
        
__Appium Inspector easily gives locator from use for automate our project.__

**18. given below the link for install appium inspector easily:**

          "https://github.com/appium/appium-inspector/releases"


**19. for android mobile testing, we can install android studio.**

__given below the link install for android studio in our machine__

           "https://www.google.com/aclk?sa=l&ai=DChcSEwie9uyT8s-EAxW1pWYCHYk4D8YYABAAGgJzbQ&ase=2&gclid=CjwKCAiA0PuuBhBsEiwAS7fsNYgBcQC1tueO08R3jyRwv2sTuh-rgd9V40A4YCRiu44F-QdUvv5rNhoCmPIQAvD_BwE&sig=AOD64_1hD0cORG5Pi2-jjws9jVQMIXW00A&q&nis=4&adurl&ved=2ahUKEwiu8OaT8s-EAxWMwjgGHcxcBuUQ0Qx6BAgNEAE"

**20. for ios mobile testing, we can use Xcode.**

**21. we can easily use appium in our local machine then install jdk (java)**

__given below the command:__

            sudo apt install default-jdk

**22. how to check java version in our local machine**

            java --version

**23. all configuration in our local machine we can move in our project then firstly we install python in our local machine**

## Required thing only for our project

**24. check python version given below the command:**

             python -V

**25. successfully installed python in our local machine. we can create virtual environment in our project**

__given below the command:__

             python -m venv venv

**26. successfully create virtaul environment in project. we can activate the virtualenv given below the command:**

             source venv/bin/activate

**27. successfully activate the virtualenv after that we can install requirenments.txt file in env environment.**

__given below command install requirenments.txt file in env environment:__

             pip install -r requirenments.txt


**28. then run test-suite properly we can use one by one given below the 2 command:**


            pytest tests/test_login.py -s -v --device android --device_name ready_to_use --alluredir=./allure-results

            pytest tests/test_signup.py -s -v --device android --device_name ready_to_use --alluredir=./allure-results
