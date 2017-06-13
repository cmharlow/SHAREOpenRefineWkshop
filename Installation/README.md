# Cleaning and Publishing SHARE Metadata
### Hands on tutorial with OpenRefine

## Required Preparation
This workshop will primarily work with the latest release candidate (2.7rc2) of **OpenRefine**. OpenRefine requires Java and a web browser to run in (**Not Internet Explorer**).

### OpenRefine Installation

If you run into any issues with installation, please get in touch with [me](mailto:cmharlow@stanford.edu) as soon as you are able, and I'll work through these issues with you. As a back-up (if you cannot install OpenRefine locally), sign up for a 1 month trial of a hosted version of OpenRefine described below.

#### Java Requirements
OpenRefine is built in Java. You will need [Java JRE installed](https://www.java.com/en/download/help/download_options.xml).

### Installing OpenRefine via Installer

1. Go to the [OpenRefine 2.7 beta Download Page](https://github.com/OpenRefine/OpenRefine/releases). Find OpenRefine v2.7 Release Candidate 2 (this should be at the top of the page).
2. Download the OpenRefine file for your operating system and follow the instructions:
  a. For Windows:
    * Download `openrefine-win-2.7-rc.2.zip`, unzip, and double-click on `openrefine.exe`.
    * If you’re having issues, try double-clicking on `refine.bat` (in the downloaded and unzipped openrefine folder on your computer) instead.
  b. For Mac:
    * Download `openrefine-mac-2.7-rc.2.dmg`, open, drag icon into the `Applications` folder and double click on it.
    * If you get the error: 'this file is damaged should be moved to trash' (or something similar), do the following:
      * Open System Preferences
      * Open Security & Privacy
      * Go to the General Tab
      * Change the "Allow applications downloaded from:" setting to "Anywhere"
      * You should be able to able to open OpenRefine now.
  c. For Linux:
    * Download `openrefine-linux-2.7-rc.2.tar.gz` and unzip the file.
    * Then type `./refine` to start. For Linux only, type `cntl+C` to stop OpenRefine.
3. Once you've tried starting OpenRefine, go to http://127.0.0.1:3333/ and make sure you see the OpenRefine start screen.
4. To quit OpenRefine, close the window that appeared when clicking the starter icon.

### Back-ups OpenRefine Installation Options

Try these if the above fails:

#### Hosted Version of OpenRefine (RefinePro)
RefinePro is a company that runs cloud-hosted instances of OpenRefine.

If you want to try a cloud-based version or if you cannot get the instructions above to work, you can try a free month trial to RefinePro. Follow these steps:

1. Go to [the RefinePro site](https://app.refinepro.com/register/) and register (you will need to provide a name and email address).
2. On that registration page, for the 'Community' portion, do not choose anything.
3. When done, enter. You'll get a free month trial.
3. Respond to the email confirmation. This should take you back to the RefinePro login.
4. Logging in takes you to your dashboard. Choose to start an instance - this will create an OpenRefine instance.
5. Once an instance available on your dashboard, click on 'Start'. Once it is starting, click on 'Access this RefinePro instance', a link that appears once your OpenRefine instance is running. (this make take a few minutes to start up)
6. This should take you to OpenRefine.

#### For the Technically-inclined: Compile from Source

Alternatively, you can run OpenRefine by downloading or git cloning the source code.

1. Clone or download OpenRefine:
  a. To download the source code for 2.7rc2, find the downloads here: https://github.com/OpenRefine/OpenRefine/releases
  b. To clone this from GitHub, clone the master branch of this repository: https://github.com/OpenRefine/OpenRefine
2. Move OpenRefine to wherever on your computer you'd like to run it from.
3. Change into that OpenRefine directory in some kind of command line interface or shell (e.g. Terminal on Mac, Command Prompt in Windows,...).
4. In your CLI or shell, first build OpenRefine (you only need to do this once per download):
  a. on Windows, type: ```$ refine build```
  b. on MacOSX or Unix, type: ```$ ./refine build```
5. Run OpenRefine:
  a. On Mac/Linux: ``` $ ./refine ```
    b. On Windows: ``` $ refine ```
6. Leave the Command Line Interface running while working with LODRefine. Go to your preferred web browser (**not Internet Explorer**), and navigate to http://127.0.0.1:3333/.
7. When you're done, go back to the Command Line Interface client where LODRefine is running, and type `cntl+C`. This will stop OpenRefine.

---

Questions? Get in touch with [Christina](mailto:cmharlow@stanford.edu).

[Back to the Workshop Agenda](https://github.com/cmh2166/SHAREOpenRefineWkshop/)
