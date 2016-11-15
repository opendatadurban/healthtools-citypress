(function ($, exports) {
    if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
    var Dexter = exports.Dexter;

    Dexter.Maps = function () {
        var self = this;

        self.MAPIT_TYPES = {
            'province': 'PR',
            'municipality': 'MN',
            'ward': 'WD',
        };

        self.init = function () {
            if ($('#slippy-map').length === 0) {
                return;
            }

            self.map = L.map('slippy-map');
            self.map.setView({lat: -28.4796, lng: 24.698445}, 5);

            var osm = new L.TileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                minZoom: 1,
                maxZoom: 16,
                attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
            });
            self.map.addLayer(osm);

            self.loadAndDrawPlaces();
        };

        self.invalidate = function () {
            self.map.invalidateSize(false);
        };

        self.placesUrl = function () {
            var url = document.location;

            if (document.location.search === "") {
                url = url + "?";
            } else {
                url = url + "&";
                url = url.replace(/format=[^&]*&/, '');
            }

            return url + "format=places-json";
        };

        self.loadAndDrawPlaces = function () {
            $.getJSON(self.placesUrl(), self.drawPlaces);
        };

        self.drawPlaceMarker = function (place, coords, radius) {
            L.circleMarker(coords, {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5
            })
                .setRadius(radius)
                .addTo(self.map)
                .bindPopup(place.full_name + " (" + place.documents.length + ")");
        };

        self.drawPlaces = function (data) {
            var total = data.document_count;

            _.each(data.mentions, function (place) {
                // radius is between 5 and 25, based on the %age of all documents
                // this place relates to
                var radius = 5 + 30 * (place.documents.length / total);

                if (place.type == 'point') {
                    // it's a point
                    self.drawPlaceMarker(place, place.coordinates, radius);
                } else {
                    // it's a region, get the centroid
                    d3.json('http://mapit.code4sa.org/area/MDB:' + place.code + '/feature.geojson?generation=1&type=' + self.MAPIT_TYPES[place.level], function (error, region) {
                        if (!region)
                            return;

                        var coords = d3.geo.centroid(region);
                        self.drawPlaceMarker(place, [coords[1], coords[0]], radius);
                    });
                }
            });
        };
    };
})(jQuery, window);

$(function () {
    Dexter.maps = new Dexter.Maps();
    Dexter.maps.init();
});
