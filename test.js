// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQAzvUmhAvL33Itgp8RZcf5Q58Fuolqx2q2S3BS1sqqY8wPagswPDVOMa6i_spZvKbeXJDm01smWv8TWPqH8cbjzwUKQavIPkQvcpPEMCx-IS0yVjidBjXVBTC4kxgFwAVRoG_Y7we8zvZOegcjD9bRwjJ5wlq8NNpaXbvf5nJLCmUvwEGcY_7fy3L9OpiTouJOKAxKvzcmN7TJ-DVB09XhUzXt9AimV2N2hiSAKJdtDvirlDjgQal55Bbe1CEkCMalGGUb2bmNhz3Z1D-lxQaJoeEaVKq12PhxVnf-90Ozw6VAbG-32u4iFHrGc6TCdfzK9D6PF';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
  )).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);