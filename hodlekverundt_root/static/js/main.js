// Initialize the map
const map = L.map('map').setView([51.505, -0.09], 13);

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Create an elevation plot
const elevation = L.control.elevation({
  position: "bottomright",
  theme: "steelblue-theme",
  width: 600,
  height: 200,
  margins: {
    top: 10,
    right: 20,
    bottom: 30,
    left: 50
  },
  useHeightIndicator: false,
  interpolate: false
});
elevation.addTo(map);

// Load a GPX track and add it to the map
const gpxUrl = 'path/to/your/gpx-file.gpx'; // Replace with your GPX file URL
const gpxTrack = new L.GPX(gpxUrl, {
  async: true
}).on('loaded', function(e) {
  map.fitBounds(e.target.getBounds());
  elevation.loadGPX(e.target);
});

gpxTrack.addTo(map);

// Create a marker for displaying the current position
const currentPosMarker = L.marker([0, 0], {
  icon: L.divIcon({
    className: 'current-pos-icon',
    html: '<i class="fas fa-map-marker-alt"></i>', // You can use any HTML content here
    iconSize: [25, 41],
    iconAnchor: [12, 41]
  }),
  draggable: false
});

// Update marker position on mouseover
elevation.on('eledata_hover', function(e) {
  const latlng = L.latLng(e.data.lat, e.data.lng);
  currentPosMarker.setLatLng(latlng);
  if (!map.hasLayer(currentPosMarker)) {
    currentPosMarker.addTo(map);
  }
});

// Remove marker on mouseout
elevation.on('eledata_clear', function() {
  if (map.hasLayer(currentPosMarker)) {
    map.removeLayer(currentPosMarker);
  }
});