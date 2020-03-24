// // import the data from data.js
// const tableData = data;

// // Reference the HTML table using d3
// var tbody = d3.select("tbody");
// function buildTable(data) {
//     // First, clear out any existing data
//     tbody.html("");
//     // Next, loop through each object in the data
//     // and append a row and cells for each value in the row
//     data.forEach((dataRow) => {
//       // Append a row to the table body
//       let row = tbody.append("tr");
//       // Loop through each field in the dataRow and add
//       // each value as a table cell (td)
//       Object.values(dataRow).forEach((val) => {
//         let cell = row.append("td");
//         cell.text(val);
//         }
//       );
//     });
//   }
  // function handleClick() {
  //   // Grab the datetime value from the filter
  //   let date = d3.select("#datetime").property("value");
  //   let filteredData = tableData;
  //   // Check to see if a date was entered and filter the
  //   // data using that date.
  //   if (date) {
  //     // Apply `filter` to the table data to only keep the
  //     // rows where the `datetime` value matches the filter value
  //     filteredData = filteredData.filter(row => row.datetime === date);
  //   }
  //   // Rebuild the table using the filtered data
  //   // @NOTE: If no date was entered, then filteredData will
  //   // just be the original tableData.
  //   buildTable(filteredData);
  // }
  // // Attach an event to listen for the form button
  // d3.selectAll("#filter-btn").on("click", handleClick);
  // // Build the table when the page loads
  // // buildTable(tableData);

function userdata(){
  let builtyear= d3.select("#datetime").property("value");
  let zipcode= d3.select("#zipcode").property("value");
  let floodzone= d3.select("#floodzone").property("value");
  d3.selectAll("#filter-btn").on("click", handleClick);
  predict();
}

function predict(){
  d3.json("http://127.0.0.1:5000/payout/"+builtyear+"/"+"/"+zipcode+"/"+"/"+floodzone+"/",function(data) {
    console.log(data);
    var i = document.getElementById("Payout");
    // console.log(i);
    // i = i;
    // i.setAttribute("value", data);
    i.value= data;
    // i.setAttribute("value", "Other Stuff");
    // d3.select("#Payout").value(data);
    
  })  
}

