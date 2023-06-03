window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, latlng) {
            const i = L.icon({
                iconUrl: `https://cdn4.iconfinder.com/data/icons/standard-free-icons/139/Checkin01-512.png`,
                iconSize: [40, 40]
            });
            return L.marker(latlng, {
                icon: i
            });
        }
    }
});