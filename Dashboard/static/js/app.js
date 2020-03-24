<<<<<<< HEAD
// // import the data from data.js
// const tableData = data;
=======
// import the data from data.js
const tableData = data;
// API key
const API_KEY = "pk.eyJ1IjoiaGJvc3RhbmNoaSIsImEiOiJjazUyeXdqNXgwMzM2M21udHBydGJ4OHllIn0.VJBG1JKQpfECTt3vM5Qgxw";
>>>>>>> Halleh

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
<<<<<<< HEAD
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
=======
  // Build the table when the page loads
  // buildTable(tableData);
>>>>>>> Halleh




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
  let earthquakes = new L.layerGroup();
  let plates = new L.layerGroup();

  var heat = L.heatLayer(
    data.features.map(feature=>{
      //TODO: add a weight value (here I used hard-coded 1; )
      var intensity_multiplier = 10;
      return feature.geometry.coordinates.reverse().concat([1*intensity_multiplier]); //feature.properties.precipitation]);
    })
    //[
    //[50.5, 30.5, 0.2], // lat, lng, intensity
    //[50.6, 30.4, 0.5],
  
  //]
  , {radius: 25})

  // We define an overlay that contains the overlays. This overlay will be visible all the time.
  let overlays = {
      Earthquakes: earthquakes, // TODO: change variables to reflect "payout"
      Plates: plates, // TODO: remove
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
  
  // Retrieve the flood GeoJSON Data.
  // d3.json("https://api.nationalflooddata.com").then(function(data) {
    // data
      console.log(data);
  
      // This function returns the style data for each of the earthquakes we plot on the map.
      // We pass the magnitude of the earthquake into two separate functions to calculate the color and radius.
      function styleInfo(feature) {
        
        var amountpaidsize = feature.properties.amountpaidonbuildingclaim/100000;
          return {
              opacity: 1,
              fillOpacity: 1,
              fillColor: getColor(amountpaidsize),
              color: "#000000",
              radius: getRadius(amountpaidsize),
              stroke: true,
              weight: 0.5
          };
      }
  
      // This function determines the color of the circle based on the magnitude of the earthquake.
      function getColor(magnitude) {
          if (magnitude > 5) {
              return "#ea2c2c";
          }
          if (magnitude > 4) {
              return "#ea822c";
          }
          if (magnitude > 3) {
              return "#ee9c00";
          }
          if (magnitude > 2) {
              return "#eecc00";
          }
          if (magnitude > 1) {
              return "#d4ee00";
          }
          return "#98ee00";
      }
  
      //This function determines the radius of the earthquake marker based on its magnitude.
      // Earthquakes with a magnitude of 0 will be plotted with a radius of 1.
      function getRadius(magnitude) {
          if (magnitude === 0) {
              return 1;
          }
          return magnitude * 4;
      }
  
      // Creating a GeoJSON layer with the retrieved data.
      L.geoJson(data, {
          // We turn each feature into a circleMarker on the map.
          pointToLayer: function(feature, latlng) {
              //console.log(data);
              return L.circleMarker(latlng);
          },
          // We set the style for each circleMarker using our styleInfo function.
          style: styleInfo,
          // We create a popup for each circleMarker to display the magnitude and location
          // of the earthquake after the marker has been created and styled.
          onEachFeature: function(feature, layer) {
              layer.bindPopup("Magnitude: " + feature.properties.amountpaidonbuildingclaim + "<br>Location: " + feature.properties.place);
          }
      }).addTo(earthquakes);
  
      // Then we add the earthquake layer to our map.
      // earthquakes.addTo(map);
      heat.addTo(map);
  
      // Create a legend control object.
      let legend = L.control({
          position: "bottomright"
      });
      // Then add all the details for the legend.
      legend.onAdd = function() {
          let div = L.DomUtil.create("div", "info legend");
          const magnitudes = [0, 1, 2, 3, 4, 5];
          const colors = [
              "#98ee00",
              "#d4ee00",
              "#eecc00",
              "#ee9c00",
              "#ea822c",
              "#ea2c2c"
          ];
          // Looping through our intervals to generate a label with a colored square for each interval.
          for (var i = 0; i < magnitudes.length; i++) {
              console.log(colors[i]);
              div.innerHTML +=
                  '<i style="background: ' + colors[i] + '"></i> ' + magnitudes[i] + (magnitudes[i+1] ? '&ndash;' + magnitudes[i+1] + '<br>' : '+');
          }
          return div;
      };
      legend.addTo(map);
  // });
  
  // Create a style for the plate lines.
  let myStyle = {
      color: 'red',
      weight: 2
  };
    