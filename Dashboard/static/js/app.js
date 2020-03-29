// import the data from data.js
const tableData = data;
// API key
//accessToken: API_KEY

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
  function handleClick() {
    // Grab the datetime value from the filter
    let date = d3.select("#datetime").property("value");
    let filteredData = tableData;
    // Check to see if a date was entered and filter the
    // data using that date.
    if (date) {
      // Apply `filter` to the table data to only keep the
      // rows where the `datetime` value matches the filter value
      filteredData = filteredData.filter(row => row.datetime === date);
    }
    // Rebuild the table using the filtered data
    // @NOTE: If no date was entered, then filteredData will
    // just be the original tableData.
    buildTable(filteredData);
  }
  // Attach an event to listen for the form button
  d3.selectAll("#filter-btn").on("click", handleClick);
  // Build the table when the page loads
  // buildTable(tableData);




// We create the street view tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
  });
  
  // We create the satellite street view tile layer that will be an option for our map.
  let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      accessToken: API_KEY
  });
  
  // We create the dark view tile layer that will be the background of our map.
  let dark = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v10/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
  });
  
  // Create a base layer that holds all three maps.
  let baseMaps = {
      "Streets": streets,
      "Satellite Streets": satelliteStreets,
      "Dark map": dark
  };
  
  // Create the earthquake and tectonic plate layers for our map.
  // let earthquakes = new L.layerGroup(); 
  // let plates = new L.layerGroup();
  let payout = new L.layerGroup();

  var heat = L.heatLayer(
    data.features.map(feature=>{
      //TODO: add a weight value (here I used hard-coded 1; )
      var intensity_multiplier = 10;
      return feature.geometry.coordinates.reverse().concat([1*intensity_multiplier]); //feature.properties.precipitation]);
    })
  , {radius: 25})



  // We define an overlay that contains the overlays. This overlay will be visible all the time.
  let overlays = {
      // Earthquakes: earthquakes, // TODO: change variables to reflect "payout"
      Payout: payout ,
      // Plates: plates, // TODO: remove
      Heat: heat //TODO: change variables to reflect "precipitation"
      
  };
  
  // Create the map object with a center and zoom level.
  let map = L.map("mapid", {
      center: [39.5, -98.5],
      zoom: 3,
      layers: [streets]
  });
  

  // Then we add a control to the map that will allow the user to change which layers are visible.
  L.control.layers(baseMaps, overlays).addTo(map);
  console.log(circleData)
  circleData.forEach(function (report) {
    L.circleMarker([report.latitude, report.longitude], 
      {'radius': report.amountpaidonbuildingclaim/30000}).addTo(map)
      .bindPopup("Amount Paid: " + report.amountpaidonbuildingclaim + " <br> ZipCode: " + report.reportedzipcode)
  })
      heat.addTo(map);
      
  
      // Create a legend control object.
      let legend = L.control({
          position: "bottomright"
      });
      // Then add all the details for the legend.
      // legend.onAdd = function() {
      //     let div = L.DomUtil.create("div", "info legend");
      //     const magnitudes = [0, 1, 2, 3, 4, 5];
      //     const colors = [
      //         "#98ee00",
      //         "#d4ee00",
      //         "#eecc00",
      //         "#ee9c00",
      //         "#ea822c",
      //         "#ea2c2c"
      //     ];
          // Looping through our intervals to generate a label with a colored square for each interval.
      //     for (var i = 0; i < magnitudes.length; i++) {
      //         console.log(colors[i]);
      //         div.innerHTML +=
      //             '<i style="background: ' + colors[i] + '"></i> ' + magnitudes[i] + (magnitudes[i+1] ? '&ndash;' + magnitudes[i+1] + '<br>' : '+');
      //     }
      //     return div;
      // };
      // legend.addTo(map);
  // });
  
  // Create a style for the plate lines.
  let myStyle = {
      color: 'red',
      weight: 2
  };
    