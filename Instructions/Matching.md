# Matching to External Data in OpenRefine

Also see the /Reconciliation subdirectory for more documentation on how one could approach this work.

## Looking up data from a URL

OpenRefine can retrieve data from URLs. This can be used in various ways, including looking up additional information from a remote service based on information in your OpenRefine data.

Typically this is a two step process - firstly a step to retrieve data from a remote service, and secondly to extract the relevant information from the data you have retrieved.

To retrieve data from an external source via the 'Fetch from URL' option:

1. Select the column you wish to match to an external service.
2. From the drop down menu of that column, use the option `Edit column->Add column by fetching URLs`.
3. Use a GREL expression to create a URL for calling the external services.
4. When the query runs, OpenRefine will request each URL and retrieve whatever data is returned. The data retrieved will be stored in a new column.
5. Then use OpenRefine transformations to extract relevant information from the data that has been retrieved. Two specific OpenRefine functions used for this are:
    * parseHtml() (you can also use this for XML.)
    * parseJson()


### Example of Fetch Data via URL Taken from Library Carpentry
Because retrieving data from external URLs takes time, this exercise targets a subset of data.

* Select a column that has ISSN data.
* In the ISSN column use the dropdown menu to choose `Edit column->Add column by fetching URLs`
* Give the column a name e.g. "Journal details"
* In the expression box you need to write some GREL where the output of the expression is a URL which can be used to retrieve data. In this case we are going to use the CrossRef api (read more about the CrossRef service at [http://www.crossref.org](http://www.crossref.org), read more about the API we are going to use at [https://github.com/CrossRef/rest-api-doc/blob/master/rest_api.md)](https://github.com/CrossRef/rest-api-doc/blob/master/rest_api.md)) The syntax for requesting journal information from CrossRef is ```http://api.crossref.org/journals/{ISSN}``` where {ISSN} is replaced with the ISSN of the journal.
* In the expression box type the GREL ```"http://api.crossref.org/journals/"+value```
* Click 'OK'

You should see a message at the top on the OpenRefine screen indicating it is fetching some data, and how far it has got. Wait for this to complete. Fetching data for a single row should take only ten seconds or so, but fetching data for all rows will take longer. You can speed this up by modifying the "Throttle Delay" setting in the 'Add column by fetching URLs' dialog which controls the delay between each URL request made by OpenRefine. This is defaulted to a rather large 5000 milliseconds (5 seconds).

At this point you should have a new cell containing a long text string in a format called 'JSON' (this stands for JavaScript Object Notation, although very rarely spelt out in full).

OpenRefine has a function for extracting data from JSON (sometimes referred to as 'parsing' the JSON). The 'parseJson' function is explained in more detail at [https://github.com/OpenRefine/OpenRefine/wiki/GREL-Other-Functions](https://github.com/OpenRefine/OpenRefine/wiki/GREL-Other-Functions).

* In the new column you've just added use the dropdown menu to access `Edit column->Add column based on this column`
* Add a name for the new column e.g. "Journal Title"
* In the Expression box type the GREL ```value.parseJson().message.title```
* You should see in the Preview the Journal title displays

## Reconciliation services
Reconciliation services allow you to lookup terms from your data in OpenRefine against external services, and use values from the external services in your data.

Reconciliation services can be more sophisticated and often quicker than using the method described above to retrieve data from a URL. However, to use the ‘Reconciliation’ function in OpenRefine requires the external resource to support the necessary service for OpenRefine to work with.

There are a few services where you can find an OpenRefine Reconciliation option available. For example WikiData has a (fledgling) reconciliation service at [https://tools.wmflabs.org/wikidata-reconcile/](https://tools.wmflabs.org/wikidata-reconcile/).

For more information on using Reconciliation services see [https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API](https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API)

### Reconciliation Example Taken from Library Carpentry

In this exercise you are going to use the VIAF Reconciliation service written by [Jeff Chiu](https://twitter.com/absolutelyjeff). Jeff offers two ways of using the reconciliation service - either via a public service he runs at [http://refine.codefork.com/](http://refine.codefork.com/), or by installing and running the service locally using the instructions at [https://github.com/codeforkjeff/refine_viaf](https://github.com/codeforkjeff/refine_viaf).

Once you have chosen which service you are going to use:

* In the Publisher column use the dropdown menu to choose `Reconcile->Start Reconciling`
* Add the details of the service:
    * Click `Add Standard Service...` and in the dialogue that appears enter:
        * "http://refine.codefork.com/reconcile/viaf" 
* You should now see a heading in the list on the left hand side of the Reconciliation dialogue called "VIAF Reconciliation Service"
* Click on this to choose to use this reconciliation service
* In the middle box in the reconciliation dialogue you may get asked what type of 'entity' you want to reconcile to - that is, what type of thing are you looking for. The list will vary depending on what reconciliation service you are using.
    * In this case choose "Corporate Name" (it seems like the VIAF Reconciliation Service is slightly intelligent about this and will only offer options that are relevant)
* In the box on the righthand side of the reconciliation dialogue you can choose if other columns are used to help the reconciliation service make a match - however it is sometimes hard to tell what use (if any) the reconciliation service makes of these additional columns
* At the bottom of the reconciliation dialogue there is the option to "Auto-match candidates with high confidence". This can be a time saver, but in this case you are going to uncheck it, so you can see the results before a match is made
* Now click 'Start Reconciling'

Reconciliation is an operation that can take a little time if you have many values to look up. However, in this case there are only 6 publishers to check, so it should work quite quickly.

Once the reconciliation has completed two Facets should be created automatically:
* Publisher: Judgement
* Publisher: best candidate's score

These are two of several specific reconciliation facets and actions that you can get from the 'Reconcile' menu (from the column drop down menu).

* Close the 'Publisher: best candidate's score' facet, but leave the 'Publisher: Judgement' facet open

If you look at the Publisher column, you should see some cells have found one or more matches - the potential matches are show in a list in each cell. Next to each potential match there is a 'tick' and a 'double tick'. To accept a reconciliation match you can use the 'tick' options in cells. The 'tick' accepts the match for the single cell, the 'double tick' accepts the match for all identical cells.

* Create a text facet on the Publisher column
* Choose 'International Union of Crystallography'

In the Publisher column you should be able to see the various potential matches. Clicking on a match will take you to the VIAF page for that entity.

* Click a 'double tick' in one of the Publisher column cells for the option "International Union of Crystallography"
* This will accept this as a match for all cells - you should see the other options all disappear
* Check the 'Publisher: Judgement' facet. This should now show that 858 items are 'matched' (if this does not update, try refreshing the facets)

We could do these one by one, but if we are confident with matches, there is an option to accept all:

* Remove all filters/facets from the project so all rows display
* In the Publisher column use the dropdown menu to choose 'Reconcile->Actions->Match each cell to its best candidate'

There are two things that reconciliation can do for you. Firstly it gets a standard form of the name or label for the entity. Secondly it gets an ID for the entity - in this case a VIAF id. This is hidden in the default view, but can be extracted:

* In the Publisher column use the dropdown menu to choose 'Edit column->Add column based on this column...'
* Give the column the name 'VIAF ID'
* In the GREL expression box type ```cell.recon.match.id```
* This will create a new column that contains the VIAF ID for the matched entity

## Extensions
The functionality in OpenRefine can be enhanced by ‘extensions’ which can be downloaded and installed to add functionality to your OpenRefine installation.

A list of Extensions (not necessarily complete) is given on the OpenRefine downloads page at [http://openrefine.org/download.html](http://openrefine.org/download.html)

One of these extensions tries to work around the limitation of Reconciliation services described above, by making it possible to use a reconciliation service against ‘linked data’ sources which have SPARQL endpoints. For more information on this see the ‘RDF Extension’ at [http://refine.deri.ie](http://refine.deri.ie). An example of how this works is given in more detail at [http://refine.deri.ie/showcases](http://refine.deri.ie/showcases).

## Using the ‘cross’ function to lookup data in other OpenRefine projects
As well as looking up data in external systems using the methods described above, it is also possible to look up data in other OpenRefine projects on the same computer. This is done using the ‘cross’ function.

The ‘cross’ function takes a value from the OpenRefine project you are working on, and looks for that value in a column in another OpenRefine project. If it finds one or more matching rows in the second OpenRefine project, it returns an array containing the rows that it has matched.

As it returns the whole row for each match, you can use a transformation to extract the values from any of the columns in the second project.
