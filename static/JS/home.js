
function init() {
    d3.json("/beers", function (data) {
        keys = data;
        console.log(data);

        start();
        // createAvgBarChart();
        
        d3.select('#submit_btn').on('click', runModel);
    });
}

function findInput() {

    var url = `/input`;
    listBeers(data);
}

//Setup and render the autocomplete
function start() {
    var mc = autocomplete(document.getElementById('beer_1'))
        .keys(keys)
        .dataField("beerlist")
        .placeHolder("90 Minute IPA")
        .width(960)
        .height(500)
        .render();
    
    var mc2 = autocomplete(document.getElementById('beer_2'))
        .keys(keys)
        .dataField("beerlist")
        .placeHolder("Founders Breakfast Stout")
        .width(960)
        .height(500)
        .render();
    
    var mc3 = autocomplete(document.getElementById('beer_3'))
        .keys(keys)
        .dataField("beerlist")
        .placeHolder("Stella Artois")
        .width(960)
        .height(500)
        .render();
}

// Changes names of autocomplete inputs
function runModel() { 
    d3.select("#beer_1 input").attr("name", "beer1");
    d3.select("#beer_2 input").attr("name", "beer2");
    d3.select("#beer_3 input").attr("name", "beer3");
    }
d3.select("#my-form").on("submit", function () {
    d3.event.preventDefault();
    runModel();
    this.submit();
});

// Calls initial function
var chosenBeers = d3.selectAll('input').values;
console.log(d3.selectAll('input').values);
init();