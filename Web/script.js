function OpenPlaylist(oldelement, playlist_name) {
    var playlist_element = document.createElement("div")
    playlist_element.className = "playlist_page";
    var old_element = document.getElementById(oldelement)
    old_element.replaceWith(playlist_element)

}

