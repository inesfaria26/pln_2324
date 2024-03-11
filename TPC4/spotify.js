const tokenUrl = 'https://accounts.spotify.com/api/token';
accessToken = tokenUrl
function getTrackInfo(trackUrl, accessToken) {
    const url = new URL(trackUrl);
    const trackId = url.pathname.split('/')[2];

    const trackInfoUrl = `https://api.spotify.com/v1/tracks/${trackId}`;
    const headers = { "Authorization": `Bearer ${accessToken}` };

    fetch(trackInfoUrl, { headers })
        .then(response => response.json())
        .then(data => {
            const albumArtUrl = data.album.images[0].url;
            const albumName = data.album.name;
            const artistName = data.artists[0].name;
            const trackName = data.name;
            const trackDuration = new Date(data.duration_ms).toISOString().substr(14, 5);

            const albumArt = document.querySelector(".album-art");
            albumArt.style.backgroundImage = `url('${albumArtUrl}')`

            const albumNameElement = document.querySelector(".album-name");
            albumNameElement.textContent = albumName;

            const artistNameElement = document.querySelector(".artist-name");
            artistNameElement.textContent = artistName;

            const trackNameElement = document.querySelector(".track-name");
            trackNameElement.textContent = trackName;

            const trackDurationElement = document.querySelector(".track-duration");
            const minutes = Math.floor(data.duration_ms / 60000);
            const seconds = Math.floor((data.duration_ms % 60000) / 1000);
            trackDurationElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        })
}

getTrackInfo('https://open.spotify.com/intl-pt/track/2panDc4TAcmDOU0sbCwQz3?si=2974eda820854c8e', 'access-token');