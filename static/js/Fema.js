// import the data from data.js
const tableData = data;

// Reference the HTML table using d3
var tbody = d3.select("tbody");
function buildTable(data) {
    // First, clear out any existing data
    tbody.html("");
    // Next, loop through each object in the data
    // and append a row and cells for each value in the row
    data.forEach((dataRow) => {
      // Append a row to the table body
      let row = tbody.append("tr");
      // Loop through each field in the dataRow and add
      // each value as a table cell (td)
      Object.values(dataRow).forEach((val) => {
        let cell = row.append("td");
        cell.text(val);
        }
      );
    });
  }
//keep track of all the filters
var filters = {}
// This function will replace your handleClick function
function updateFilters() {

// grab all values from form inputs
let FilteredData = tableData;
let Built Year = d3.select("#datetime").property("value");
let Zip Code = d3.select("#city").property("value");
let Flood Zone = d3.select("#state").property("value");




// if a form input exists, filter it
if ( Built Year) {
  // Apply `filter` to the table data to only keep the
  // rows where the `datetime` value matches the filter value
  FilteredData = FilteredData.filter(row => row.datetime === date);
}
if (Zip Code ) {
  // Apply `filter` to the table data to only keep the
  // rows where the `datetime` value matches the filter value
  FilteredData = FilteredData.filter(row => row.city === city);
}
if (Flood Zone) {
  // Apply `filter` to the table data to only keep the
  // rows where the `datetime` value matches the filter value
  FilteredData = FilteredData.filter(row => row.state === state);
}


// when finished filtering, rebuild the table with filtered data
buildTable(FilteredData);

}

d3.selectAll("#filter-btn").on("click", updateFilters);

// Build the table when the page loads
buildTable(tableData);

