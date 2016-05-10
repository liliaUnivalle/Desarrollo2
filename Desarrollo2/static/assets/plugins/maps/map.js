var map;

function initialize(seism, stations) {
  var mapDiv = document.getElementById('map');
  var mapOptions = {
    center: {
      lat: seism.latitude,
      lng: seism.longitude
    },
    zoom: 8
  };

  // Creating the map
  map = new google.maps.Map(mapDiv,mapOptions);


  // getting the stations information
  var station_icon = 'http://osso.univalle.edu.co/apps/poseidon/geoseismo/images/corto.png';
  var epicenter_icon = {
    url: 'http://osso.univalle.edu.co/apps/poseidon/geoseismo/images/sismo.gif',
    // This marker is 132 pixels wide by 132 pixels high.
    size: new google.maps.Size(132, 132),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is 66 from the center to the middle
    anchor: new google.maps.Point(66, 66)
  };

  // Adding epicenter location on the map
  var seism_info = getSeismHtml(seism);

  addMarkerToMap(
    epicenter_icon,
    seism_info,
    seism.latitude,
    seism.longitude
  );

  // Adding stations locations on the map
  for(i = 0; i < stations.length; i++){
    var html_info = getStationHtml(stations[i]);
    addMarkerToMap(
      station_icon,
      html_info,
      stations[i].fields.latitude,
      stations[i].fields.longitude
    );
  };


  google.maps.event.addDomListener(map, "resize", function() {
   var center = map.getCenter();
   google.maps.event.trigger(map, "resize");
   map.setCenter(center);
  });



};


function addMarkerToMap(icon,html,lat,lng){
  // Creating the market
  var marker = new google.maps.Marker({
    position: { lat: lat, lng: lng },
    map: map,
    icon: icon,
    optimized: false
  });

  // Creating the info window to the corresponding market
  var info = new google.maps.InfoWindow({
    content:html,
    maxWidth: 350 // infor window maximun size
  });

  marker.addListener('click',function(){
    info.open(map,marker);
  });

  // Event that closes the Info Window with a click on the map
  google.maps.event.addListener(map, 'click', function() {
    info.close();
  });
};


function getSeismHtml(seism){
  var html = "";
  html += '<div id="iw-container">';
  html += '<div class="iw-title">Porcelain Factory of Vista Alegre</div>';
  html += '<div class="iw-content">';
  html += '<div class="iw-subTitle">History</div>';
  html += "<p>Latitud: " + seism.latitude + "</p>";
  html += "<p>Longitud: " + seism.longitude + "</p>";
  html += "<p>Profundida: " + seism.depth + "</p>";
  html += "<p>Magnitud: " + seism.magnitude + "</p>";
  html += "<p>GAP: " + seism.gap + "</p>";
  html += "<p>Capital más Cercana: " + seism.nearest_capital + "</p>";
  html += "</div>";
  html += "</div>";

  return html;
};


function getStationHtml(station){
  var html = "";
  html += "<p>Estación: " + station.pk + "</p>";
  html += "<p>Propietario: " + station.fields.owner + "</p>";
  html += "<p>Operador: " + station.fields.operator + "</p>";
  html += "<p>Localización: " + station.fields.location + "</p>";
  html += "<p>Departamento: " + station.fields.department + "</p>";
  html += "<p>Longitud: " + station.fields.longitude + "</p>";
  html += "<p>Latitud: " + station.fields.latitude + "</p>";
  html += "<p>Altura: " + station.fields.height + "</p>";
  html += "<p>Sensor: " + station.fields.sensor + "</p>";
  html += "<p>Digitalizador: " + station.fields.digitizer + "</p>";
  html += "<p>Tipo de Estación: " + station.fields.station_type + "</p>";
  html += "<p># de Canales: " + station.fields.number_of_channels + "</p>";
  html += "<p>Geologia: " + station.fields.geology + "</p>";
  html += "<p>Tipografía: " + station.fields.typography + "</p>";
  html += "<p>Estado: " + station.fields.status + "</p>";

  return html;
};

/* Application Controller
------------------------------------------------ */
var MapController = function () {
	"use strict";

	return {
		//main function
		init: initialize
  };
}();
