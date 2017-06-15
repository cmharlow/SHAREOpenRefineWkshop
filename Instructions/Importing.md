# Importing Data into OpenRefine

## What Data Can I Import?
You can upload or import files in a variety of formats, including:

* TSV (tab-separated values)
* CSV (comma-separated values)
* Excel
* JSON (javascript object notation)
* XML
* Google Spreadsheet

You can also upload or import files from a number of sources, including:

- files from your local computer/machine
- specify a URL from which OpenRefine will retrieve structured data
- Copy & Paste data
- Retrieve data from your Google Drive Account (requires authentication)

## Create & Import Data into OpenRefine Project

### Start OpenRefine

To start, open/begin running OpenRefine by double clicking on the application wherever you installed it.

*NOTE: If OpenRefine does not open in a browser window, open your browser and type the address <http://127.0.0.1:3333/> to take you to the OpenRefine interface.*

### Create You OpenRefine Project

OpenRefine Projects store together your data and your history of work on that data.

![Create a Project Screen](Images/StartProject.png "Create a Project Screen")

1. Click on the "Create Project" tab.
2. Next you need to decide what data to import into your Project.

*Common question: Can I use OpenRefine to create data from scratch? The answer is no: OpenRefine is really built just to work with existing data, not to create data.*

*Common error: Do not use the `Open Project` tab to create a Project. Open Project is only for importing existing OpenRefine projects.*

### Load Data:

The options for importing data into your project include:

- `This Computer`: i.e. load a file from your Computer's file system.
- `Web Addresses (URLs)`: i.e. load structured data available via a URL
- `Clipboard`: i.e. copy and paste data into a text box that OpenRefine will then parse as structured data
- `Google Data`: Retrieve data from a Google Spreadsheet in your Google Drive Account (this requires authentication)

Depending on your interest, try one of the following:

#### SHARE API for Normalized Data

1. Click on `Web Addresses (URLs)`.
2. Enter `https://share.osf.io/api/v2/normalizeddata/` then click `Next >>`.
3. A blob of JSON should appear. Use the `Parse Data As` options as the bottom to select `JSON Files`.
4. In the now structured JSON preview, choose which node you want to evaluate as your "record" by clicking on it.
5. Review the preview of data in tabular format. If okay, give the project a name in the top right corner, then click `Create Project >>`. If not okay, click `<< Start Over` in the top left corner and re-select your data and data parsing options.

#### OAI-PMH Feed via URL

1. Click on `Web Addresses (URLs)`.
2. Enter `http://scholarworks.boisestate.edu/do/oai/?verb=ListRecords&metadataPrefix=oai_dc` then click `Next >>`.
3. A blob of XML should appear. Use the `Parse Data As` options as the bottom to select `XML Files`.
4. In the now structured XML preview, choose which node you want to evaluate as your "record" by clicking on it.
5. Review the preview of data in tabular format. If okay, give the project a name in the top right corner, then click `Create Project >>`. If not okay, click `<< Start Over` in the top left corner and re-select your data and data parsing options.

#### Sample SHARE JSON File or OAI-PMH XML File from GitHub

1. Click on `Web Addresses (URLs)`.
2. Enter `https://raw.githubusercontent.com/cmh2166/SHAREOpenRefineWkshop/master/Data/sampleData.json` for the sample JSON. If you want the sample XML, enter `https://raw.githubusercontent.com/cmh2166/SHAREOpenRefineWkshop/master/Data/samplemetadata.oai.dc.xml`. Then click `Next >>`.
3. A blob of XML should appear. Use the `Parse Data As` options as the bottom to select `XML Files`.
4. In the now structured XML preview, choose which node you want to evaluate as your "record" by clicking on it.
5. Review the preview of data in tabular format. If okay, give the project a name in the top right corner, then click `Create Project >>`. If not okay, click `<< Start Over` in the top left corner and re-select your data and data parsing options.

#### Sample File from your Computer or from Google Drive

1. Click on `This Computer` or `Google Drive`.
2. If necessary, authenticate, then locate the file which you have downloaded that you would like to use.
2. Click 'Next'.
2. Ensure the data looks correct. use the `Parse Data As` options to correct.
5. Review the preview of data in tabular format. If okay, give the project a name in the top right corner, then click `Create Project >>`. If not okay, click `<< Start Over` in the top left corner and re-select your data and data parsing options.

## Other Notes
* Pay Attention to the Parse Data options. These can help with number conversions or removing blank rows, as well as encoding issues.
* Think about what you want to do with this data before choosing the tabular representation. Almost always you want to use CSV/TSV if you're hoping to export the data back out for re-ingest in your local repository system.
* Projects created and available to your OpenRefine installation will appear in the OpenRefine homepage under `Open Project`.
* Upper file size limits... ~20k "simple" rows, depending on your computing power.
