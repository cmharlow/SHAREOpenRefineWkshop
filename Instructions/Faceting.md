# Faceting & Filtering Your Data

## What Are Facets?

Facets are one of the most useful features of OpenRefine for both data state assessment as well as data normalization.

`Facets` group all the values that appear in a column, and then allow you to filter the data by these values as well as edit values across many records at the same time. It acts like a facet you would see in your discovery layer, but with editing and filtering capabilities.

We are primarily interested in `Text facets`. This simply groups all the text values in a column and lists each value with the number of records it appears in. The facet information appears in the left hand panel in the OpenRefine interface.

## Creating a Text Facet

To create a Text Facet for a column:

1. Click on the drop down menu at the top of the column
2. choose `Facet -> Text Facet`.

The facet will then appear in the left hand panel. The facet consists of a list of values used in the data. You can filter the data displayed by clicking on one of these headings.

You can include multiple values from the facet in a filter at one time by using the `Include` option which appears when you put your mouse over a value in the Facet.

You can also `invert` the filter to show all records which do not match your selected values. This option appears at the top of the Facet panel when you select a value from the facet to apply as a filter.

## Creating a Text Filters

You can also apply `Text Filters` which looks for a particular piece of text appearing in a column. Text filters are applied by:

1. Click the drop down menu at the top of the column you want to filter
2. Choose 'Text filter'.
3. In the left-hand area, a filter box appears. Type in the text you want to use in the Filter to display only rows which contain that text in the selected column.

You can also use regular expressions in the filter.

## Working with Faceted & Filtered Data
It is very important to note that when you have faceted or filtered the data displayed in OpenRefine, any operations you carry out will apply only to the rows that match the filter - that is the data currently being displayed.

## More on Facets
As well as 'Text facets' Refine also supports a range of other types of facet. These include:

* Numeric facets
* Timeline facets (for dates)
* Custom facets
* Scatterplot facets

**Numeric and Timeline facets** display graphs instead of lists of values. The graph includes 'drag and drop' controls you can use to set a start and end range to filter the data displayed.

**Scatterplot facets** are less commonly used - for further information on these see the tutorial at [http://enipedia.tudelft.nl/wiki/OpenRefine_Tutorial#Exploring_the_data_with_scatter_plots](http://enipedia.tudelft.nl/wiki/OpenRefine_Tutorial#Exploring_the_data_with_scatter_plots)

**Custom facets** are a range of different types of facets, and also allow you write your own custom facets. Some of the default custom facets are:

* `Word facet` - this breaks down text into words and counts the number of records each word appears in
* `Duplicates facet` - this results in a binary facet of 'true' or 'false'. Rows appear in the 'true' facet if the value in the selected column is an exact match for a value in the same column in another row
* `Text length facet` - creates a numeric facet based on the length (number of characters) of the text in each row for the selected column. This can be useful for spotting incorrect or unusual data in a field where specific lengths are expected (e.g. if the values are expected to be years, any row with a text length more than 4 for that column is likely to be incorrect)
* `Facet by blank` - a binary facet of 'true' or 'false'. Rows appear in the 'true' facet if they have no data present in that column. This is useful when looking for rows missing key data.

## Editing Data in a Facet
If you create a text facet you can edit the values in the facet to change the value for several records at the same time. To do this, simply mouse-over the value you want to edit and click the 'edit' option that appears.

## Clustering Data in a Facet
The Cluster function groups together values in a column that are 'similar' according to a range of string matching algorithms and enables you to merge those values together.

To use the 'Cluster' function:
- Click on the 'Edit Cells' menu option in the relevant column
- Choose 'Cluster and edit...'

Alternatively, on a Facet in your left-hand working area, click on 'Cluster' in the top right corner of your facet.

Clustering allows use of a number of preselected string matching algorithms. For more information on the methods used to create Clusters see [https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth](https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth)

For each cluster you have the option of 'merging' the values together - that is replace with a single consistent value. By default OpenRefine uses the most common value in the cluster as the new value, but you can select one of the other values by clicking the value itself, or you can simply type the desired value into the 'New Cell Value' box.
