# Munging Data in OpenRefine

## Joining & Splitting Cells

A common workflow with multi-valued cells is to:

- split multi-valued cells into individual cells based off of a delimiter ;
- modify/refine/clean individual cells ;
- join multi-valued cells back together using a delimiter.

Let's go through joining & splitting cells right now, and modifying will come up soon after.

### Joining Cells

* Click the dropdown menu at the top of a column which contains cells you would like to join
* Choose `Edit cells->Join multi-valued cells`
* In the prompt type the "\|" (pipe) symbol as your delimiter to use to join the values together.
* Click 'OK' to join that Column's cells together for each "Record"

### Splitting Cells

To split multi-valued cells into their own cells within the same "Records", we can use a 'Split multi-valued cells' function:

* Click the dropdown menu at the top of a column with multi-valued cells
* Choose `Edit cells->Split multi-valued cells`
* In the prompt type the "\|" (pipe) symbol or whatever is the delimiter, then click 'OK'
* Click the 'Records' option to change to Records mode

### Reviewing Rows vs Records

Use the 'Rows' and 'Records' view options in the top left corner of your data table to observe if the numbers of Rows and Records are equal (or not).

### Moving Columns Around

For multi-row records (what you will have if you imported heavily-nested data), you will want to make sure that a unique record identifier is the first column of your OpenRefine Data Table. This will help make sure that multi-row records stay grouped according to your understanding of a record. To move the selected identifier column to the first position:

* Click the dropdown menu at the top of your identifier column
* Choose `Edit columns->Move column to beginning`
