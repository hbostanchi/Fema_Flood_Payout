d3.json("http://127.0.0.1:5000/payout/1988/4/a",function(data) {
    console.log(data);
    var i = document.getElementById("Payout");
    // console.log(i);
    // i = i;
    // i.setAttribute("value", data);
    i.value= data;
    // i.setAttribute("value", "Other Stuff");
    // d3.select("#Payout").value(data);
    
})

