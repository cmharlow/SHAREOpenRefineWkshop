# OpenRefine Project Interface
OpenRefine displays and works with data in a tabular format (i.e. a CSV representation). Each row will usually (_but not always_) represent a 'record' in the data, while each column represents an information or metadata field. The individual data points are in the cells.

## Row/Record Display Limits

OpenRefine only displays a limited number of rows of data at one time. You can adjust the number by using the options in the top left corner of your data table. Navigation through pages of data are on the top right of your data table.

## Working with data in OpenRefine
Most data operation options in OpenRefine are accessed from drop down menus (the upside down triangles) at the top of the columns. When you select an option in a particular column (e.g. to make a change to the data), it will affect all the cells in that column currently selected (we will discuss this more in faceting). If you want to make changes across several columns, you will need to do this one column at a time.

## Rows and Records
OpenRefine has two modes of viewing data 'Rows' and 'Records'. At the moment we are in Rows mode, where each row represents a single record in the data set - in this case, an article. In Records mode, OpenRefine can link together multiple rows as belonging to the same Record. Multi-row records happens by default when a single metadata field (or column) detects multiple values within the selected record or node.

## Sorting data
You can sort data in OpenRefine by clicking on the drop-down menu for the column you want to sort on, and choosing 'Sort'.

Once you have sorted the data, a new 'Sort' drop-down menu will be displayed.

'Sorts' in OpenRefine are temporary - that is, if you remove the 'Sort', the data will go back to its original 'unordered' state. The 'Sort' drop-down menu lets you amend the existing sort (e.g., reverse the sort order), remove existing sorts, and/or make sorts permanent.

## Undo and Redo
OpenRefine lets you undo, and redo, any number of steps you have taken in cleaning the data. This means you can always try out transformations and 'undo' if you need to. The way OpenRefine records the steps you have taken even allows you to take the steps you've carried out on one data set, and apply it to another data set by a simple copy and paste operation.

The 'Undo' and 'Redo' options are accessed via the lefthand panel.

The Undo/Redo panel lists all the steps you've taken so far. To undo steps, simply click on the last step you want to preserve in the list and this will automatically undo all the changes made since that step.

The remaining steps will continue to show in the list but greyed out, and you can reapply them by simply clicking on the last step you want to apply.

However, if you 'undo' a set of steps and then start doing new transformations, the greyed out steps will disappear and you will no longer have the option to 'redo' these steps.

If you wish to save a set of steps to be re-applied later, or to a different project, you can click the 'Extract' button. This gives you the option to select the steps you want to save, and to copy the transformations included in the selected steps in a format called 'JSON'

To apply a set of steps you have copied or saved in this 'JSON' format use the 'Apply' button and paste in the JSON. In this way you can share transformations between projects and each other.

Undo/Redo data is stored with the Project and is saved automatically as you work, so next time you open the project, you can access your full history of steps you have carried out and undo/redo in exactly the same way.
