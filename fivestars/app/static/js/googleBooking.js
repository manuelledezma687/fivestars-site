
var request = {
    query: 'search query',
    fields: ['place_id', 'name', 'formatted_address'],
    types: ['(cities)', '(address)']
};




var options = {
    componentRestrictions: { country: 'us' },
    types:request,
    strictBounds: true,
    bounds: new google.maps.LatLngBounds(
        new google.maps.LatLng(33.588310, -84.549723),
        new google.maps.LatLng(34.307274, -84.041351)
    )
};

var originInput = document.getElementById('pick_up_location');
var originAutocomplete = new google.maps.places.Autocomplete(originInput, options);

var destinationInput = document.getElementById('drop_off_location');
var destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput, options);


var origin = originInput.value;
var destination = destinationInput.value;