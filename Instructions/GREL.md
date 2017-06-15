# Transforming Data in OpenRefine with GREL (Google Refine Expression Language)

###Introducing Transformations

'Transformations' in OpenRefine are ways of manipulating data in columns going beyond facets & filters. Transformations are predominately written in 'GREL', or the Google Refine Expression Language (harkening back to the original name of OpenRefine). To some extent GREL expressions are similar to Python string methods and/or Excel formula.

Full documentation for the GREL is available at [https://github.com/OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language](https://github.com/OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language).

### Common GREL Transformations
Some transformations are used regularly and are accessible directly through menu options, without having to type them directly. Examples of these are below, thanks to Library Carpentry for gathering them.

Common Transformation  | Action | GREL expression
--------------------| ------------- | -------------
To Uppercase| Converts the current value to uppercase | ```value.toUppercase()```
To Lowercase| Converts the current value to lowercase | ```value.toLowercase()```
To Titlecase| Converts the current value to titlecase (i.e. each word starts with an uppercase character and all other characters are converted to lowercase) | ```value.toTitlecase()```
Trim leading and trailing whitespace | Removes any 'whitespace' characters (e.g. spaces, tabs) from the start or end of the current value | ```value.trim()```

### Writing GREL Transformations
To start writing transformations:

1. Select the column on which you wish to perform a transformation
2. Choose 'Edit cells->Transform…'
3. In the screen that displays, the 'Expression' is where you write the GREL transformation. It also gives a preview of the transformation on 10 rows of your data.

The transformation you type into the 'Expression' box has to be a valid GREL expression. The simplest expression is simply the word 'value' by itself - which simply means the value that is currently in the column - that is: make no change.

GREL functions are written by giving a value of some kind (a text string, a date, a number etc.) to a GREL function. Some GREL functions take additional parameters or options which control how the function works. GREL supports two types of syntax:

* value.function(options)
* function(value, options)

Either is valid, and which is used is completely down to personal preference. In these notes the first syntax is used.

We will try:
- `value.toUppercase()`
- `value.substring(0, value.indexOf('.'))`
- `if(value.contains('.'), value.substring(0, value.indexOf('.')), value)`
- `value.md5()`
- `value.unicode()`
- `value.replace(/^\d{4}$/, 'Year : ' + value)`

### Creating a New Column via a GREL transformations

You can also add a new column based on the output of a GREL transformation:

1. Select the source column on which you wish to perform a transformation for the values of the new column
2. Choose 'Edit columns->Add column based on this column...'
3. In the screen that displays, the 'Expression' is where you write the GREL transformation. It also gives a preview of the transformation on 10 rows of your data.
4. Give your new column a name.
