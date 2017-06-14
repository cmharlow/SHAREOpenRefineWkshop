# Cleaning and Publishing SHARE Metadata
### Hands on tutorial with OpenRefine

## Required Preparation
This workshop will primarily work with the latest release candidate (2.7rc2) of **OpenRefine**. OpenRefine requires Java and a web browser to run in (**Not Internet Explorer**).

### OpenRefine Installation

If you run into any issues with installation, please get in touch with [me](mailto:cmharlow@stanford.edu) as soon as you are able, and I'll work through these issues with you. I will be available the 2 hours before the workshop to help with installation issues or questions. The zoom information is below:

```
Topic: OpenRefine Installation Help
Time: Jun 15, 2017 10:00 AM - Noon Pacific Time (US and Canada)

Join from PC, Mac, Linux, iOS or Android: https://stanford.zoom.us/j/866812859

Or iPhone one-tap (US Toll):  +16465588656,866812859# or +14086380968,866812859#

Or Telephone:
    Dial: +1 646 558 8656 (US Toll) or +1 408 638 0968 (US Toll)
    +886 277 417 473 (Taiwan Toll)
    +1 855 703 8985 (Canada Toll Free)
    Meeting ID: 866 812 859
    International numbers available: https://stanford.zoom.us/zoomconference?m=zaVwHcZY9refmRy-7rp74gGCBHWoLDlh
```

#### Java Requirements
OpenRefine is built in Java. You will need [Java JRE installed](https://www.java.com/en/download/help/download_options.xml).

### Installing OpenRefine via Installer

1. Go to the [OpenRefine 2.7 beta Download Page](https://github.com/OpenRefine/OpenRefine/releases). Find OpenRefine v2.7 Release Candidate 2 (this should be at the top of the page).
2. Download the OpenRefine file for your operating system and follow the instructions:
    * For Windows:
      * Download `openrefine-win-2.7-rc.2.zip`, unzip, and double-click on `openrefine.exe`.
      * If you’re having issues, try double-clicking on `refine.bat` (in the downloaded and unzipped openrefine folder on your computer) instead.
    * For Mac:
      * Download `openrefine-mac-2.7-rc.2.dmg`, open or double click on the downloaded file, drag icon into the `Applications` folder and double click on it in your Applications list.
      * If you get the error: 'this file is damaged should be moved to trash' (or something similar), do the following:
        * Open System Preferences
        * Open Security & Privacy
        * Go to the General Tab
        * Change the "Allow applications downloaded from:" setting to "Anywhere"
        * You should be able to able to open OpenRefine now.
    * For Linux:
      * Download `openrefine-linux-2.7-rc.2.tar.gz` and unzip the file.
      * Then type `./refine` to start. For Linux only, type `cntl+C` to stop OpenRefine.
3. Once you've tried starting OpenRefine, go to http://127.0.0.1:3333/ and make sure you see the OpenRefine start screen.
4. To quit OpenRefine, close the window that appeared when clicking the starter icon.

### Installation for the Technically-inclined: Compile from Source

(try this if the above fails or you are more technically-inclined)

Alternatively, you can run OpenRefine by downloading or git cloning the source code.

1. Clone or download OpenRefine:
    - To download the source code for 2.7rc2, find the downloads here: https://github.com/OpenRefine/OpenRefine/releases
    - To clone this from GitHub, clone the master branch of this repository: https://github.com/OpenRefine/OpenRefine
2. Move OpenRefine to wherever on your computer you'd like to run it from.
3. Change into that OpenRefine directory in some kind of command line interface or shell (e.g. Terminal on Mac, Command Prompt in Windows,...).
4. In your CLI or shell, first build OpenRefine (you only need to do this once per download):
    - on Windows, type: ```$ refine build```
    - on MacOSX or Unix, type: ```$ ./refine build```
5. Run OpenRefine:
    - On Mac/Linux: ``` $ ./refine ```
    - On Windows: ``` $ refine ```
6. Leave the Command Line Interface running while working with LODRefine. Go to your preferred web browser (**not Internet Explorer**), and navigate to http://127.0.0.1:3333/.
7. When you're done, go back to the Command Line Interface client where LODRefine is running, and type `cntl+C`. This will stop OpenRefine.

---

Questions? Get in touch with [Christina](mailto:cmharlow@stanford.edu).

[Back to the Workshop Agenda](https://github.com/cmh2166/SHAREOpenRefineWkshop/)
